# Assignment-1


# TODO's:
 
  1. Read a email and check for attachments to process the data for extracting insights from the mail serveR
  2. Analyse and create a storage container in minio for storing the documents read from email server. Only for streaming inserts

## TASK 1:

   * We have  made a scheduler which constanty check our email for any mail subject **invoice**.
   * Once it figure out it is invoice mail it extract all the information from the mail.
   * It store the data in form of **dataframe** you can store it any form as you like to.
## TASK 2:
   
   * We have to store the data to minio and there is a format in which we store data into it.
   * The minio has concept of buckets and objects.
   ![minio architecture](https://www.google.com/search?q=minio+architecture+buckjet&tbm=isch&ved=2ahUKEwiPqubovMvwAhVu-DgGHa_RBLsQ2-cCegQIABAA&oq=minio+architecture+buckjet&gs_lcp=CgNpbWcQAzoECAAQHjoGCAAQCBAeULd-WIeIAWDGiwFoAHAAeACAAbgBiAHnCpIBAzAuOJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=9qGfYI_XFu7w4-EPr6OT2As&bih=749&biw=736#imgrc=E4--RBGit0MKKM)
   
   * **Suppose** there are 10 mail with of different companies now we cannot store all the invoice in one bucket 
   * It will be hard to retierve data and find its owner

   * We have this format
   * Username as **bucket name**
   * Object name = **file name**
