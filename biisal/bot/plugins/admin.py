# (c) @adarsh-goel
# (c) @biisal
import os
import time
import string
import random
import asyncio
import aiofiles
import datetime
from biisal.utils.broadcast_helper import send_msg
from biisal.utils.database import Database
from biisal.bot import StreamBot
from biisal.vars import Var
from pyrogram import filters, Client
from pyrogram.types import Message
db = Database(Var.DATABASE_URL, Var.name)
Broadcast_IDs = {}

@StreamBot.on_message(filters.command("users") & filters.private )
async def sts(c: Client, m: Message):
    user_id=m.from_user.id
    if user_id in Var.OWNER_ID:
        total_users = await db.total_users_count()
        await m.reply_text(text=f"Total Users in DB: {total_users}", quote=True)
        
@StreamBot.on_message(filters.command("ban") & filters.private & filters.user(Var.OWNER_ID))
async def sts(b, m: Message):
    id = m.text.split("/ban ")[-1]
    if not await db.is_user_banned(int(id)):
        await db.ban_user(int(id))
        await db.delete_user(int(id))
        if await db.is_user_banned(int(id)):
            await m.reply_text(text=f"`{id}`** is Banned** ", parse_mode=ParseMode.MARKDOWN, quote=True)
            await b.send_message(
                chat_id=id,
                text="**Your Banned to Use The Bot**",
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True
            )
        else:
            await m.reply_text(text=f"**can't ban **`{id}`** something went wrong** ", parse_mode=ParseMode.MARKDOWN, quote=True)
    else:
        await m.reply_text(text=f"`{id}`** is Already Banned** ", parse_mode=ParseMode.MARKDOWN, quote=True)

@StreamBot.on_message(filters.command("unban") & filters.private & filters.user(Var.OWNER_ID))
async def sts(b, m: Message):

    id = m.text.split("/unban ")[-1]
    if await db.is_user_banned(int(id)):
        await db.unban_user(int(id))
        if not await db.is_user_banned(int(id)):
            await m.reply_text(text=f"`{id}`** is Unbanned** ", parse_mode=ParseMode.MARKDOWN, quote=True)
            await b.send_message(
                chat_id=id,
                text="**Your Unbanned now Use can use The Bot**",
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True
            )
        else:
            await m.reply_text(text=f"**can't unban **`{id}`** something went wrong** ", parse_mode=ParseMode.MARKDOWN, quote=True)
    else:
        await m.reply_text(text=f"`{id}`** is not Banned** ", parse_mode=ParseMode.MARKDOWN, quote=True)
      
@StreamBot.on_message(filters.command("broadcast") & filters.private  & filters.user(list(Var.OWNER_ID)))
async def broadcast_(c, m):
    user_id=m.from_user.id
    out = await m.reply_text(
            text=f"Broadcast initiated! You will be notified with log file when all the users are notified."
    )
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not Broadcast_IDs.get(broadcast_id):
            break
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    Broadcast_IDs[broadcast_id] = dict(
        total=total_users,
        current=done,
        failed=failed,
        success=success
    )
    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(
                user_id=int(user['id']),
                message=broadcast_msg
            )
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user['id'])
            done += 1
            if Broadcast_IDs.get(broadcast_id) is None:
                break
            else:
                Broadcast_IDs[broadcast_id].update(
                    dict(
                        current=done,
                        failed=failed,
                        success=success
                    )
                )
    if Broadcast_IDs.get(broadcast_id):
        Broadcast_IDs.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(
            text=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.",
            quote=True
        )
    else:
        await m.reply_document(
            document='broadcast.txt',
            caption=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.",
            quote=True
        )
    os.remove('broadcast.txt')
