import read_mail as read
from imapclient import IMAPClient
import minio_storage

HOST = 'imap.gmail.com'
username = "abcd12ghijk@gmail.com"
password = "abcd@1234"

def scheduler():
        server = IMAPClient(HOST)
        server.login(username,password)
        server.select_folder('inbox')

        # Start IDLE mode
        server.idle()
        print("Connection is now in IDLE mode, send yourself an email")

        while True:
            try:
                # Wait for up to 5 seconds for an IDLE response
                response= server.idle_check(timeout=5)
                if response != [] :
                    response=  response[0][1]
                
                #check if new mail received, if received call read_mail and send data to minio
                if response == b'EXISTS':
                    new_email,attachment = read.read_mail()
                    print(new_email)
                    minio_storage.main(new_email,attachment)

                else :
                    print("No New Messages Yet...")

            except KeyboardInterrupt:
                break

        server.idle_done()
        print("\nIDLE mode done")
        server.logout()

if __name__ == '__main__':
    scheduler()

