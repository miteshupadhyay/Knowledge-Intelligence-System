import boto3
from botocore.exceptions import ClientError
from config import Config

class S3Storage:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id="testid"
            aws_secret_access_key="testid",
            region_name="us-east-1"
        )
        self.bucket_name = Config.S3_BUCKET_NAME

    def upload_file(self, file_obj, filename):
        try:
            self.s3.upload_fileobj(file_obj, self.bucket_name, filename)
            return True
        except ClientError as e:
            print(f"Error uploading file: {e}")
            return False
        
    def get_file(self, filename):
        try:
            response = self.s3.get_object(Bucket = self.bucket_name, Key = filename)
            return response['Body'].read()
        except ClientError as e:
            print(f"Error retrieving file: {e}")
            return None