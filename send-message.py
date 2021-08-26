from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, FloodWaitError, UsernameNotOccupiedError, UserChannelsTooMuchError, PhoneNumberBannedError, UsernameInvalidError, UserNotMutualContactError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import sys
import csv
import traceback
import time
import random
import pandas as pd

dataAPIs = []
allDataAPI = []
with open("Apikey.csv", encoding='UTF-8') as f:  #Enter your file name
    rowss = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rowss, None)
    for row in rowss:
        dataAPIs.append(row)
        dataAPI = {}
        dataAPI['api_id']  =  row[0]
        dataAPI['api_hash'] = row[1]
        dataAPI['phone'] = row[2]
        allDataAPI.append(dataAPI)
for dataAPI in allDataAPI:
    api_id = dataAPI['api_id']                           #enter here api_id 6305419
    api_hash = dataAPI['api_hash'] #Enter here api_hash id e48908e1e2c1cd9f1db222ce809f268e
    phone = dataAPI['phone']  #enter here phone number with country code +84 377200557
    client = TelegramClient(phone, api_id, api_hash).start()
    async def main():
        # Now you can use all client methods listed below, like for example...
        await client.send_message('me', 'Hello !!!!!')


    SLEEP_TIME_1 = 100
    SLEEP_TIME_2 = 100
    with client:
        client.loop.run_until_complete(main())
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))
    chats = []
    last_date = None
    chunk_size = 200
    groups = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.megagroup == True:
                groups.append(chat)
        except:
            continue

    users = []
    allUser = []
    with open("data.csv", encoding='UTF-8') as f:  #Enter your file name
        rows = csv.reader(f,delimiter=",",lineterminator="\n")
        next(rows, None)
        for row in rows:
            allUser.append(row)
            user = {}
            user['phone'] = row[0]
            user['chatID'] = int(row[1])
            users.append(user)
    for user in users:
        print(user['chatID'])
        entity=client.get_entity(user['chatID'])
        client.send_file(entity, './photos/photo.png', caption="Viết message vào đây")
        print("Sending wait for 10 Seconds...")
        time.sleep(random.randrange(10, 15))
        # client.send_message(entity=entity,message="Hi")