import imaplib
import email
import pandas as pd
import requests
import json
host = 'imap.gmail.com'
username = "abcd12ghijk@gmail.com"
password = "abcd@1234"

attachment_dir = "/Users/rushilkoppaka/PycharmProjects/freezonlabs_internship"


def read_mail():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")

    _, search_data = mail.search(None, 'ALL')

    all_email = []

    for num in search_data[0].split():
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]

        email_message = email.message_from_bytes(b)
        if 'invoice' in email_message['Subject']:
            email_data = {'attachment': [], 'file name': [], 'Document type': []}

            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    email_data['Body'] = body.decode()
                    continue
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                file_name = part.get_filename()
                if bool(file_name):

                    encoded_string = str(part.get_payload(decode=True)).encode()
                    bytearray_string = bytearray(encoded_string)
                    email_data['attachment'].append(bytearray_string)

                    email_data['file name'].append(file_name)
                    email_data['Document type'].append(file_name.split('.')[1])
                    # file_path = attachment_dir + '/' + file_name
                    # with open(file_path, 'wb') as f:
                    #     f.write(part.get_payload(decode=True))
                    for header in ['Subject', 'To', 'From', 'Date']:
                        email_data[header] = email_message[header]
                    email_data['username'], email_data['email ID'] = email_message['From'].rsplit(' ',1)
                    all_email.append(email_data)

    data_frame = pd.DataFrame(all_email)
    return data_frame


# DataFrame columns format -> attachment, Subject, To, From, Date
# There maybe multiple attachments for single mail
# Each attachment will have its own row with all values.


if __name__ == '__main__':
    inbox = read_mail()
    print(inbox)
