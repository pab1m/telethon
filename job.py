from telethon import TelegramClient, events
from telethon.tl.types import MessageEntityTextUrl, InputMessagesFilterDocument
from datetime import datetime, timedelta

api_id = 27348907
api_hash = 'f6a5b11160bb0efd31fc297d10a6864d'

client = TelegramClient('anon', api_id, api_hash)
client.start()


async def main():
    channel = await client.get_entity('https://t.me/WORKIN_LVIV')

    two_days_ago = datetime.now() - timedelta(days=2)

    messages = await client.get_messages(channel, limit=None, offset_date=two_days_ago)
    for message in messages:
        # print(message.stringify())
        print('-' * 100)
        data = message.date
        print(data)

        info = str(message.text)
        clean_info = info.replace('*', '')

        print(clean_info)

        # title = clean_info[:clean_info.index('💵')]
        # print(title.replace('\n', ''))
        #
        # start_index = clean_info.index("💵")
        # end_index = clean_info.index("🏢", start_index)
        # salary = clean_info[start_index:end_index]
        # print(salary.replace('\n', ''))
        #
        # start_index = clean_info.index("📱")
        # end_index = clean_info.index("\n", start_index)
        # phone = clean_info[start_index:end_index]
        # print(phone.replace('\n', ''))
        #
        # if isinstance(message.entities[1], MessageEntityTextUrl):
        #     web = message.entities
        #     url = str(web[1].url)
        #     print(url)
        # else:
        #     pass


with client:
    client.loop.run_until_complete(main())