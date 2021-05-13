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
        print("Connection is now in IDLE mode, send yourself an email or quit with ^c")

        while True:
            try:
                # Wait for up to 30 seconds for an IDLE response
                response= server.idle_check(timeout=5)
                if response != [] :
                    response=  response[0][1]

                if response == b'EXISTS':
                    new_email = read.read_mail()
                    print(new_email)
                    minio_storage.main(new_email)

                else :
                    print("No New Messages Yet...")

            except KeyboardInterrupt:
                break

        server.idle_done()
        print("\nIDLE mode done")
        server.logout()

if __name__ == '__main__':
    scheduler()

