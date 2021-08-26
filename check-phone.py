from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.sync import TelegramClient
import csv

api_id = '6655774'                          #enter here api_id 6305419
api_hash = '42eecb98621882a65246fb3450191328' #Enter here api_hash id e48908e1e2c1cd9f1db222ce809f268e
myPhone = '+84 837601512'  #enter here phone number with country code +84 377200557
client = TelegramClient(myPhone, api_id, api_hash).start()
dataPhone = []
allDataPhone = []
with open("data-phone.csv", encoding='UTF-8') as f:  #Enter your file name
    rowss = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rowss, None)
    for row in rowss:
        dataPhone.append(row)
        dataAPI = {}
        dataAPI['phone']  =  row[0]
        allDataPhone.append(dataAPI)
allData = []
print('Saving In file...')
for sdt in allDataPhone:
    contact = InputPhoneContact(client_id=0, phone=sdt['phone'], first_name="", last_name="")
    result = client(ImportContactsRequest([contact]))
    usrDict = result.__dict__["users"]
    if usrDict:
        dataPhone = {}
        chatID = usrDict[0].__dict__["id"]
        phone = usrDict[0].__dict__["phone"]
        dataPhone['chatID'] = chatID
        dataPhone['phone'] = phone
        allData.append(dataPhone)
with open("data.csv","w",encoding='UTF-8') as f:#Enter your file name.
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['phone', 'chatID'])
    for user in allData:
        writer.writerow([user['phone'], user['chatID']])
print('Saved In file successfully.......')