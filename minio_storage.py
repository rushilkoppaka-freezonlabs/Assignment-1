from minio import Minio
from minio.error import S3Error


import io


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1


def main(inbox, doc):
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )

    """
    print(type(doc[0]))
    print(len(inbox)) 
    print(type(inbox["username"][0]))
    bucket=inbox["username"][0].lower()
    object=inbox['file name'][0]
    print(type(object))
    """
    for i in range(len(inbox)):

        # Make 'asiatrip' bucket if not exist.

        found = client.bucket_exists(inbox["username"][i].lower())
        if not found:
            client.make_bucket(inbox["username"][i].lower())
        else:
            print("Bucket", inbox["username"][i], "already exists")

        # Upload '/home/user/Photos/asiaphotos.zip' as object name
        # 'asiaphotos-2015.zip' to bucket 'asiatrip'.

        # client.compose_object(inbox["username"][i], inbox['file name'][i], sources, sse=None, metadata=None, tags=None, retention=None, legal_hold=False)
        result = client.put_object(inbox["username"][i].lower(), listToString(inbox['file name'][i]).lower(),
                                   io.BytesIO(doc[i]), -1, part_size=10 * 1024 * 1024)
        print("the file", i, "  is uploaded")


if __name__ == "__main__":
    main()
