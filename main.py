# pip install cryptography
# pip install gspread
# pip install oauth2client
# pip install bcrypt


# for hashing passwords:
import bcrypt
# for encrypting messages and files:
import cryptography
from cryptography.fernet import Fernet
# to connect, obtain data and send data to google sheets
from oauth2client.service_account import ServiceAccountCredentials
import gspread
# for getting information related to time:
import datetime
import time

fkey = open("file_key.txt")
key = fkey.read()
cipher = Fernet(key)

scope = ["https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('Credentials.json', scope)
client = gspread.authorize(credentials)
bulk_sheet = client.open('Encrypted Communication Software').sheet1
accounts = client.open('PrivateMessaging: Accounts').sheet1





account_username = input("""
What is your account name?
- Shane
- Cedric
- Leo
>""").lower()

try:
    locate_username = accounts.find(account_username)
except gspread.exceptions.CellNotFound:
    print("Invalid Username. Are you Shane, Cedric, or Leo?")
signed_in = False
while not signed_in:
    the_account = str(accounts.find(account_username))
    row = int(the_account[7])
    col = 2
    hashed = accounts.cell(row, col).value
    hashed = hashed.encode("utf-8")
    # original_text = cipher.decrypt(hashed).decode()
    # original_text = original_text.encode("utf-8")
    unverified = input("What is your password?").encode("utf-8")
    if bcrypt.checkpw(unverified, hashed):
        print("It matches")
        signed_in = True
    else:
        print("failure")
        # raise ValueError

# raise InvalidToken
# cryptography.fernet.InvalidToken

# raise CellNotFound(query)
# gspread.exceptions.CellNotFound:

found_id = True


def send():
    if True:
        username = account_username
        while True:
            print("message:")
            input_message = input(">").encode("utf-8")
            encrypted_text = cipher.encrypt(input_message)
            noByte_message = encrypted_text.decode()
            message_id = int(bulk_sheet.cell(2, 3).value)
            actual_message_id = message_id + 1
            actual_message_id = str(actual_message_id)

            time = datetime.datetime.now()

            seconds = time.strftime("%S")
            minutes = time.strftime("%M")
            hour = time.strftime("%I")
            convention = time.strftime("%p")
            day = time.strftime("%d")
            month = time.strftime("%m")
            year = time.strftime("%Y")

            the_time = f"{hour}:{minutes} {convention} ({month}/{day}/{year})"

            try:
                bulk_sheet.find(actual_message_id)
            except gspread.exceptions.CellNotFound:
                found_id = False
            while found_id:
                actual_message_id += 1
                # the lines 6 above to one below is not needed.
            if not found_id:
                print(f" The ID of this message is {actual_message_id}")
                new_user = [username, noByte_message, actual_message_id, the_time]
                bulk_sheet.insert_row(new_user, 2)
                print("complete")


def id():
    requested_id = input("What is the ID of the message?:")
    integer_requested_id = int(requested_id)
    find_id = bulk_sheet.find(requested_id)
    str_full = str(find_id)
    # returns in R1C1 format
    row = int(str_full[7])
    col = int(str_full[9])
    col = 2
    final = bulk_sheet.cell(row, col).value
    final1 = final.encode()
    original_text = cipher.decrypt(final1).decode()

    col1 = 1
    user_name = bulk_sheet.cell(row, col1).value
    print(f"""
the message is: 
"{original_text}", which was sent by {user_name}
          """)


def read():
    the_id = int(input("""How many of the latest messages you want to read?:
>"""))
    message_id = int(bulk_sheet.cell(2, 3).value)
    message_id += 1
    difference = message_id - the_id
    if the_id > message_id:
        print("There isn't enough messages to go back that far")
    else:
        for i in range(difference, message_id):
            print("obtaining messages...")
            i1 = str(i)
            find_id = bulk_sheet.find(i1)
            str_full = str(find_id)
            # returns in R1C1 format
            row = int(str_full[7])
            # ignore: col = int(str_full[9])
            col = 2
            final = bulk_sheet.cell(row, col).value
            final1 = final.encode()
            original_text = cipher.decrypt(final1).decode()

            col_time = 4
            time = bulk_sheet.cell(row, col_time).value

            col1 = 1
            user_name = bulk_sheet.cell(row, col1).value
            print(f"""{user_name} said "{original_text}" at {time}
""")


def encrypt():
    if True:
        user_name = account_username
        while True:
            fkey = open("file_key.txt", "rb")
            key = fkey.read()
            cipher = Fernet(key)
            file_name = input("""
What is the exact name of the file you wish to encrypt?
>""")
            with open(file_name, "rb") as f:
                e_file = f.read()
            encrypted_file = cipher.encrypt(e_file)
            print("processing")
            no_byte_encrypted_file = encrypted_file.decode()
            # with open(file_name + " (encrypted)", "wb") as ef:
            # ef.write(encrypted_file)

            time = datetime.datetime.now()
            seconds = time.strftime("%S")
            minutes = time.strftime("%M")
            hour = time.strftime("%I")
            convention = time.strftime("%p")
            day = time.strftime("%d")
            month = time.strftime("%m")
            year = time.strftime("%Y")
            the_time = f"{hour}:{minutes} {convention} ({month}/{day}/{year})"

            message_id = int(bulk_sheet.cell(2, 3).value)
            actual_message_id = message_id + 1
            actual_message_id = str(actual_message_id)

            string = str(no_byte_encrypted_file)

            string_count = (len(encrypted_file))
            if len(string) > 2450000:
                print("File is too large to be encrypted")
            else:
                pass
            print(f"the file has been encrypted to {string_count} characters")

            # b_initial = string[0]
            b1 = string[0:50000]
            b2 = string[50000:100000]
            b3 = string[100000:150000]
            b4 = string[150000:200000]
            b5 = string[200000:250000]
            b6 = string[250000:300000]
            b7 = string[300000:350000]
            b8 = string[350000:400000]
            b9 = string[400000:450000]
            b10 = string[450000:500000]
            b11 = string[500000:550000]
            b12 = string[550000:600000]
            b13 = string[600000:650000]
            b14 = string[650000:700000]
            b15 = string[700000:750000]
            b16 = string[750000:800000]
            b17 = string[800000:850000]
            b18 = string[850000:900000]
            b19 = string[900000:950000]
            b20 = string[950000:1000000]
            b21 = string[1000000:1050000]
            b22 = string[1050000:1100000]
            b23 = string[1100000:1150000]
            b24 = string[1150000:1200000]
            b25 = string[1200000:1250000]
            b26 = string[1250000:1300000]
            b27 = string[1300000:1350000]
            b28 = string[1350000:1400000]
            b29 = string[1400000:1450000]
            b30 = string[1450000:1500000]
            b31 = string[1500000:1550000]
            b32 = string[1550000:1600000]
            b33 = string[1600000:1650000]
            b34 = string[1650000:1700000]
            b35 = string[1700000:1750000]
            b36 = string[1750000:1800000]
            b37 = string[1800000:1850000]
            b38 = string[1850000:1900000]
            b39 = string[1900000:1950000]
            b40 = string[1950000:2000000]
            b41 = string[2000000:2050000]
            b42 = string[2050000:2100000]
            b43 = string[2100000:2150000]
            b44 = string[2150000:2200000]
            b45 = string[2200000:2250000]
            b46 = string[2250000:2300000]
            b47 = string[2300000:2350000]
            b48 = string[2350000:2400000]
            b49 = string[2400000:2450000]

            file_message = input("""
leave a comment:
>""")
            input_message = file_message.encode("utf-8")
            encrypted_text = cipher.encrypt(input_message)
            noByte_message = encrypted_text.decode()
            try:
                bulk_sheet.find(actual_message_id)
            except gspread.exceptions.CellNotFound:
                found_id = False
            while found_id:
                actual_message_id += 1
                # the lines 6 above to one below is not needed.
            if not found_id:
                print(f"   - The ID of this message is {actual_message_id}")
                new_user = [user_name, noByte_message, actual_message_id, the_time, b1, b2, b3, b4, b5, b6, b7, b8, b9,
                            b10, b11,
                            b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29,
                            b30, b31, b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42, b43, b44, b45, b46, b47,
                            b48, b49]
                bulk_sheet.insert_row(new_user, 2)
                print("""
The file has been uploaded to the database
""")


def decrypt():
    requested_id = input("What is the ID of the message?:")
    integer_requested_id = int(requested_id)
    find_id = bulk_sheet.find(requested_id)
    print("obtaining data from database...")
    str_full = str(find_id)
    # returns in R1C1 format
    row = int(str_full[7])
    col = int(str_full[9])

    p1_data = bulk_sheet.cell(row, 5).value
    p2_data = bulk_sheet.cell(row, 6).value
    p3_data = bulk_sheet.cell(row, 7).value
    p4_data = bulk_sheet.cell(row, 8).value
    p5_data = bulk_sheet.cell(row, 9).value
    p6_data = bulk_sheet.cell(row, 10).value
    p7_data = bulk_sheet.cell(row, 11).value
    p8_data = bulk_sheet.cell(row, 12).value
    p9_data = bulk_sheet.cell(row, 13).value
    p10_data = bulk_sheet.cell(row, 14).value
    p11_data = bulk_sheet.cell(row, 15).value
    p12_data = bulk_sheet.cell(row, 16).value
    p13_data = bulk_sheet.cell(row, 17).value
    p14_data = bulk_sheet.cell(row, 18).value
    p15_data = bulk_sheet.cell(row, 19).value
    p16_data = bulk_sheet.cell(row, 20).value
    p17_data = bulk_sheet.cell(row, 21).value
    p18_data = bulk_sheet.cell(row, 22).value
    p19_data = bulk_sheet.cell(row, 23).value
    p20_data = bulk_sheet.cell(row, 24).value
    p21_data = bulk_sheet.cell(row, 25).value
    p22_data = bulk_sheet.cell(row, 26).value
    p23_data = bulk_sheet.cell(row, 27).value
    p24_data = bulk_sheet.cell(row, 28).value
    p25_data = bulk_sheet.cell(row, 29).value
    p26_data = bulk_sheet.cell(row, 30).value
    p27_data = bulk_sheet.cell(row, 31).value
    p28_data = bulk_sheet.cell(row, 32).value
    p29_data = bulk_sheet.cell(row, 33).value
    p30_data = bulk_sheet.cell(row, 34).value
    p31_data = bulk_sheet.cell(row, 35).value
    p32_data = bulk_sheet.cell(row, 36).value
    p33_data = bulk_sheet.cell(row, 37).value
    p34_data = bulk_sheet.cell(row, 38).value
    p35_data = bulk_sheet.cell(row, 39).value
    p36_data = bulk_sheet.cell(row, 40).value
    p37_data = bulk_sheet.cell(row, 41).value
    p38_data = bulk_sheet.cell(row, 42).value
    p39_data = bulk_sheet.cell(row, 43).value
    p40_data = bulk_sheet.cell(row, 44).value
    p41_data = bulk_sheet.cell(row, 45).value
    p42_data = bulk_sheet.cell(row, 46).value
    p43_data = bulk_sheet.cell(row, 47).value
    p44_data = bulk_sheet.cell(row, 48).value
    p45_data = bulk_sheet.cell(row, 49).value
    p46_data = bulk_sheet.cell(row, 50).value
    p47_data = bulk_sheet.cell(row, 51).value
    p48_data = bulk_sheet.cell(row, 52).value
    p49_data = bulk_sheet.cell(row, 53).value

    raw_data = p1_data + p2_data + p3_data + p4_data + p5_data + p6_data + p7_data + p8_data + p9_data + p10_data \
               + p11_data + p12_data + p13_data + p14_data + p15_data + p16_data + p17_data + p18_data + p19_data \
               + p20_data + p21_data + p22_data + p23_data + p24_data + p25_data + p26_data + p27_data + p28_data \
               + p29_data + p30_data + p31_data + p32_data + p33_data + p34_data + p35_data + p36_data + p37_data \
               + p38_data + p39_data + p40_data + p41_data + p42_data + p43_data + p44_data + p45_data + p46_data \
               + p47_data + p48_data + p49_data
    raw_data1 = bytes(raw_data, 'utf -8')

    with open("encrypted_data", "wb") as ef:
        ef.write(raw_data1)
    with open("encrypted_data", "rb") as df:
        encrypted_data = df.read
    assigned = input("""
what would you like to call the decrypted file that was retrieved from database? 
    - Remember to include ".png", ".jpg" or ".txt" at the end 
>""")

    decrypted_file = cipher.decrypt(raw_data1)
    with open(assigned, "wb") as df:
        df.write(decrypted_file)


def all_messages():
    freeze = int(input("""
How long do you want the downtime to be between messages? 
ex: an input of "5" will allow you to read twenty messages, however, you will have to wait 5 seconds per message.
The higher of a number you type in, the more messages you will be able to read.
So, what should it be?:
>"""))
    id = bulk_sheet.cell(2, 3).value
    int_id = int(id)
    count = 0
    col_value = 2
    while count < int_id:

        username = bulk_sheet.cell(col_value, 1).value
        message = bulk_sheet.cell(col_value, 2).value
        message_id = bulk_sheet.cell(col_value, 3).value
        message_time = bulk_sheet.cell(col_value, 4).value
        find_file1 = bulk_sheet.cell(col_value, 5).value
        short_file1 = find_file1[0:5]
        if short_file1 == "gAAAA":
            short_file1 = "True"
        else:
            short_file1 = "False"
        count += 1
        col_value += 1

        final = message
        final1 = final.encode()
        try:
            original_text = cipher.decrypt(final1).decode()
            original_text = """ " """ + original_text + """ " """
        except cryptography.fernet.InvalidToken:
            original_text = " *no message attached*"

        print(f"""
{username} said {original_text} at {message_time}. The message ID is {message_id}.
File attached: {short_file1}
""")
        time.sleep(freeze)


service_type = input("""
Commands:
"Send" - send messages
"Read" - Read messages 
"ID" - If you wish to obtain message through ID number
"All" - Read all messages. Time restrictions apply
(these messages are not case sensitive)
>""")

if service_type.lower() == "send":
    send()
if service_type.lower() == "id":
    id()
if service_type.lower() == "read":
    read()
if service_type.lower() == "encrypt":
    encrypt()
if service_type.lower() == "decrypt":
    decrypt()
if service_type.lower() == "all":
    all_messages()
