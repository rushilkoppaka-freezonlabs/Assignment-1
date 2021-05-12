import imaplib
import email
import pandas as pd

host= 'imap.gmail.com'
username = "abcd12ghijk@gmail.com"
password = "abcd@1234"

attachment_dir = "/Users/rushilkoppaka/PycharmProjects/freezonlabs_internship"

def read_mail():
        mail = imaplib.IMAP4_SSL(host)
        mail.login(username,password)
        mail.select("inbox")

        _, search_data = mail.search(None, 'ALL')

        all_email=[]

        for num in search_data[0].split() :
            _, data = mail.fetch(num, '(RFC822)')
            _,b = data[0]

            email_message = email.message_from_bytes(b)
            if 'invoice' in email_message['Subject']:
                    email_data = {'attachment': []}

                    for part in email_message.walk():
                        if part.get_content_type()=="text/plain" :
                            body= part.get_payload(decode=True)
                            email_data['Body'] = body.decode()
                            continue
                        if part.get_content_maintype() == 'multipart':
                            continue
                        if part.get('Content-Disposition') is None :
                            continue
                        file_name = part.get_filename()
                        if bool(file_name):
                            email_data['attachment'].append(part.get_payload(decode=True))
                            # file_path = attachment_dir + '/' + file_name
                            # with open(file_path, 'wb') as f:
                            #     f.write(part.get_payload(decode=True))

                    if bool(file_name):
                        for header in ['Subject', 'To', 'From', 'Date']:
                            email_data[header] = email_message[header]

                    all_email.append(email_data)
        data_frame = pd.DataFrame(all_email)
        return data_frame

if __name__ == '__main__':
    inbox = read_mail()
    print(inbox)
    #print(inbox.drop('attachment',axis=1))
