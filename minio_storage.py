from minio import Minio
from minio.error import S3Error
import read_mail_for_hrithik as rushil


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )
    
    inbox=rushil.read_mail_fast()

    print(type(inbox["attachment"]))
    for i in range(len(inbox)):
        
        # Make 'asiatrip' bucket if not exist.
        
        found = client.bucket_exists(inbox["username"])
        if not found:
            client.make_bucket(inbox["username"].lower())
        else:
            print("Bucket",inbox["username"],"already exists")

        # Upload '/home/user/Photos/asiaphotos.zip' as object name
        # 'asiaphotos-2015.zip' to bucket 'asiatrip'.

        
        client.fput_object(
            inbox["username"],"invoice details",inbox["attachment"])
        print(
            "the invoice detials are already uploaded"
        )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)