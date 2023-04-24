import openpyxl as openpyxl
from telethon import TelegramClient, events
import xlsxwriter
import logging
from telethon.tl.types import MessageEntityTextUrl
from datetime import datetime, timedelta

api_id = 27348907
api_hash = 'f6a5b11160bb0efd31fc297d10a6864d'

client = TelegramClient('anon', api_id, api_hash)
client.start()

chat_id = -1001237045898
words = ['сука', 'пішов нахуй', 'ти', 'блять', 'qq']


@client.on(events.ChatAction(chats=chat_id))
@client.on(events.NewMessage(chats=chat_id))
async def filterr(event):
    for i in words:
        if i in str(event.raw_text).lower():
            user = event.sender
            await event.message.delete()
            await event.reply(f"@{user.username}, використання матерних слів не є прийнятним. Будь ласка, поводьтеся адекватно.")


@client.on(events.ChatAction(chats=chat_id))
@client.on(events.NewMessage(chats=chat_id))
async def my_event_handler(event):
    if 'hello' in str(event.raw_text).lower():
        await event.reply('hi!')


@client.on(events.ChatAction(chats=chat_id))
@client.on(events.NewMessage(chats=chat_id))
async def main(event):
    channel = await client.get_entity(chat_id)

    messages = await client.get_messages(channel, limit=1)

    for message in messages:
        info = str(message.text)
        print(info)


    book = xlsxwriter.Workbook(r"/home/st_pavlo/PycharmProjects/tltn/data.xlsx")
    page = book.add_worksheet("message")

    row = 0
    column = 0

    page.set_column("A:A", 50)


    page.write(row, column, info)
    book.close()

    #     clean_info = info.replace('*', '')
    #
    #     # print(clean_info)
    #
    #     title = clean_info[:clean_info.index('💵')]
    #     print(title.replace('\n', ''))
    #
    #     start_index = clean_info.index("💵")
    #     end_index = clean_info.index("🏢", start_index)
    #     salary = clean_info[start_index:end_index]
    #     print(salary.replace('\n', ''))
    #
    #     start_index = clean_info.index("📱")
    #     end_index = clean_info.index("\n", start_index)
    #     phone = clean_info[start_index:end_index]
    #     print(phone.replace('\n', ''))
    #
    #     if isinstance(message.entities[1], MessageEntityTextUrl):
    #         web = message.entities
    #         url = str(web[1].url)
    #         print(url)
    #     else:
    #         pass
    # else:
    #     pass

client.run_until_disconnected()
