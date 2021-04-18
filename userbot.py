from telethon.sync import TelegramClient, events
from config import api_hash,api_id

with TelegramClient('anon', api_id, api_hash) as client:

   @client.on(events.NewMessage(pattern=r'\.hi'))
   async def handler(event):
      await event.edit("Hello")
   client.run_until_disconnected()
