
#importing the minio libaries
from minio import Minio
from minio.error import S3Error

#importing this for line 54
import io

"""
this funciton is use to convert the file name in inbox to str

because file name is stored in form of list in inbox dataframe and put_object(...) require str as input

"""
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1
# it is main function 

def main(inbox, doc):
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    
    """
    In this we are using the public server, in which we can see all data uploaded by people used it 
    anyone can access anyone's data 
    
    so we can make our own server and change the access key and secret key
    and make it more secure
    
    """
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )

    """
    this is to check the type and value which we are getting in inbox and doc
     
    you can uncommet it for your understanding for data insights
    
    print(type(doc[0]))
    print(len(inbox)) 
    print(type(inbox["username"][0]))
    bucket=inbox["username"][0].lower()
    object=inbox['file name'][0]
    print(type(object))
    """
    for i in range(len(inbox)):

        """
        now we are making bucket for each unique username 
       
        """

        found = client.bucket_exists(inbox["username"][i].lower())
        if not found:
            client.make_bucket(inbox["username"][i].lower())
        else:
            print("Bucket", inbox["username"][i], "already exists")

        """
        here we upload the data in form of btyearray 
        
        and the str parameters must in lowercase
        
        """
        result = client.put_object(inbox["username"][i].lower(), listToString(inbox['file name'][i]).lower(),
                                   io.BytesIO(doc[i]), -1, part_size=10 * 1024 * 1024)
        
        print("the file  ", listToString(inbox['file name'][i]) , "  is uploaded")


if __name__ == "__main__":
    main()
