
import boto3
from botocore.client import Config



from pprint import pprint

def lambda_handler(event, context):

    s3 = boto3.client("s3")

    bucket = "testsuc"

    key = "filename.txt"

    file = s3.get_object(Bucket = bucket, Key = key)

    paragraph = str(file['Body'].read())
    comprehend = boto3.client("comprehend")
    sayi = 5
  
    isim = "Mustafa Kemal"
    print (paragraph+isim)

