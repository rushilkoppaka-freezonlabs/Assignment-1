from minio import Minio
from minio.error import S3Error
import io
import requests

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def Extract(inbox):#,path=''+listToString(inbox['file name']).lower()):
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )

    for i in range(len(inbox)):
        found = client.bucket_exists(inbox["username"][i].lower())
        if not found:
            print('doesnt exist')
        else:
            print(inbox["username"][i].lower(),' ',listToString(inbox['file name'][i]).lower())
            result = client.fget_object("rushil", "cat.jpg", "input.jpg")
            #result = client.put_object(inbox["username"][i].lower(), listToString(inbox['file name'][i]).lower(),
             #                          io.BytesIO(doc[i]), -1, part_size=10 * 1024 * 1024)

            print('downloaded ', listToString(inbox['file name'][i]).lower())
