from minio import Minio
from minio.error import S3Error
import read_mail as rushil


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "play.min.io",
        access_key="hrithik107",
        secret_key="rushil107",
    )
    
    inbox=rushil.read_mail_fast()
      
    for i in inbox.loc[:,["username"]]:
        
        # Make 'asiatrip' bucket if not exist.
        found = client.bucket_exists(i)
        if not found:
            client.make_bucket(i)
        else:
            print("Bucket",i,"already exists")

        # Upload '/home/user/Photos/asiaphotos.zip' as object name
        # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
        client.fput_object(
            i,"invoice details", inbox.loc[0,["attachment","Date","username"]] )
        print(
            "the invoice detials are already uploaded"
        )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)