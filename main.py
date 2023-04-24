from telethon import TelegramClient, events
import logging

api_id = 27348907
api_hash = 'f6a5b11160bb0efd31fc297d10a6864d'

client = TelegramClient('anon', api_id, api_hash)

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'hello' in str(event.raw_text).lower():
        await event.reply('hi!')

@client.on(events.NewMessage(pattern=r'.*heck'))
async def handler(event):
    await event.delete()

@client.on(events.NewMessage)
async def handlers(event):
    # Good
    chat = await event.get_chat()
    sender = await event.get_sender()
    chat_id = event.chat_id
    sender_id = event.sender_id
    print(chat)
    print(sender)
    print(chat_id)
    print(sender_id)


client.start()
client.run_until_disconnected()




async def main():
    # Getting information about yourself
    me = await client.get_me()
    # me = await client.get_entity("vburdyk")

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me)
    # print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    username = me.username
    print(username)
    print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

    # # # You can send messages to yourself...
    # await client.send_message('me', 'Hello, myself!')
    # # ...to some chat ID
    # for i in range(1, 101):
    #     await client.send_message(-1001237045898, 'шо ви?')
    # # ...to your contacts
    # await client.send_message('+380 66 600 58 68', 'Hello, friend!')
    # # # ...or even to any username
    # await client.send_message('vburdyk', 'Testing Telethon!')

    # You can, of course, use markdown in your messages:
    # message = await client.send_message(
    #     'me',
    #     'This message has **bold**, `code`, __italics__ and '
    #     'a [nice website](https://www.youtube.com/)!',
    #     link_preview=False
    # )

    # # Sending a message returns the sent message object, which you can use
    # print(message.raw_text)
    #
    # # You can reply to messages directly if you have a message object
    # await message.reply('Cool!')
    #
    # # # Or send files, songs, documents, albums...
    # await client.send_file('me', '/home/st_pavlo/Зображення/me.jpg')
    #
    # # You can print the message history of any chat:
    # async for message in client.iter_messages('me'):
    #     print(message.id, message.text)
    #
    #     # You can download media from messages, too!
    #     # The method will return the path where the file was saved.
    #     if message.photo:
    #         path = await message.download_media()
    #         print('File saved to', path)  # printed after download is done

with client:
    client.loop.run_until_complete(main())