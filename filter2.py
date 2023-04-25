from telethon import TelegramClient, events
import xlsxwriter
import logging
from telethon.tl.types import MessageEntityTextUrl
from datetime import datetime, timedelta
import pandas as pd
from openpyxl import load_workbook


api_id = 27348907
api_hash = 'f6a5b11160bb0efd31fc297d10a6864d'

client = TelegramClient('anon', api_id, api_hash)
client.start()

chat_id = -1001237045898
words = ['сука', 'пішов нахуй', 'блять', 'qq']

row = 0

@client.on(events.ChatAction(chats=chat_id))
@client.on(events.NewMessage(chats=chat_id))
async def filterr(event):
    for i in words:
        if i in str(event.raw_text).lower():
            user = event.sender
            await event.message.delete()
            await event.reply(f"@{user.username}, використання матерних слів не є прийнятним. Будь ласка, поводьтеся адекватно.")
            return

    channel = await client.get_entity(chat_id)
    messages = await client.get_messages(channel, limit=1)

    data = []
    for message in messages:
        text = str(message.text)

        # data = text.split('\n')
        data.append(text)
        print(data)

    if 'hello' in str(event.raw_text).lower():
        await event.reply('hi!')
        # print(event.raw_text)



# @client.on(events.ChatAction(chats=chat_id))
# @client.on(events.NewMessage(chats=chat_id))
# async def my_event_handler(event):
#     if 'hello' in str(event.raw_text).lower():
#         await event.reply('hi!')
#
#
# @client.on(events.ChatAction(chats=chat_id))
# @client.on(events.NewMessage(chats=chat_id))
# async def main(event):
#     global row
#     channel = await client.get_entity(chat_id)
#
#     messages = await client.get_messages(channel, limit=1)
#
#     data = []
#     for message in messages:
#         text = str(message.text)
#
#         # data = text.split('\n')
#         data.append(text)
#         print(data)



    # excel_file = 'test2.xlsx'
    #
    # # Відкриття конкретного листа
    # excel_sheet = 'test'
    #
    # # Завантаження даних з листа
    # wb = load_workbook(excel_file)
    # ws = wb[excel_sheet]
    #
    # # Додавання нових даних до листа
    # # new_data = [['Column1', 'Column2'], [1, 4], [2, 5], [3, 6]]
    # # for row in data:
    # # ws.append(text)
    # #
    # # # Збереження змін до Excel файлу
    # # wb.save(excel_file)
    #
    # # new_data = [['Column1', 'Column2']]
    # # for row in data:
    # #     new_data.append(row.split(','))  # перетворення рядка на список даних
    #
    # new_data = [['Column1', 'Column2'], [1, 4], [2, 5], [3, 6]]
    # for row in new_data:
    #     ws.append(row)
    #
    # # Збереження змін до Excel файлу
    # wb.save(excel_file)







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
