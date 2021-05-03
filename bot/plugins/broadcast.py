from bot.hf.fic import vhkzuoi_repliz_handler
from bot.hf.flifi import uszkhvis_chats_ahndler
from bot.hf.stuf import get_tle_mof_t
from bot.sql.users_sql import get_user_id
from bot import AUTH_CHANNEL
@Client.on_message(broadcast ?(.*)", func=lambda e: e.sender_id == AUTH_CHANNEL)
async def broadcastmssg(event):
    msgtobroadcast = event.pattern_match.group(1)
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    for bdcast in userstobc:
        try:
            sent_count += 1
            await client.send_message(int(bdcast.chat_id), msgtobroadcast)
            await asyncio.sleep(0.2)
        except Exception as e:
            try:
                 logger.info(f"Error : {error_count}\nError : {e} \nUsers : {chat_id}"
                 )
            except:
                 pass
    await tgbot.send_message(
        event.chat_id,
        f"**Broadcast Successfull 🎉**\n\nSended to: {sent_count} users.\nFailed: {error_count} users.\n\nTotal: {len(userstobc)} users"
        )

                   
#Broadcast plugin complete credits belong to github.com/xditya
#Broadcast plugin code is from: https://www.github.com/xditya/NoPMsBot/tree/master/bot%2Fplugins%2Fbroadcast.py
