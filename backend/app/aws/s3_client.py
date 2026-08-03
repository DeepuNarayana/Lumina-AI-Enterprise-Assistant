import boto3
from app.config.settings import settings
from typing import Optional

from botocore.exceptions import ClientError

class S3Client:

    def __init__(self):
        self.client=boto3.client(
            "s3",
            region_name=settings.AWS_REGION
        )
        self.bucket_name=settings.S3_BUCKET_NAME

    def upload_document(
        self,
        local_file: str,

        object_key: str
    )->bool:
        try:

            self.client.upload_file(
                Filename=local_file,
                Bucket=self.bucket_name,
                Key=object_key
            )
            return True
        except ClientError as e:
            print(e)
            return False

    def generate_download_url(
        self,
        object_key: str,
        expires_in: int = 3600
    )->Optional[str]:

        try:
            url = self.client.generate_presigned_url(
            ClientMethod = "get_object",
            Params = {

                "Bucket": self.bucket_name,
                "Key": object_key
                },
             ExpiresIn = expires_in,
            )

            return url

        except ClientError as e:

            print(e)
            return None

    def delete_document(
        self,
        object_key: str
    ):
        try:
            self.client.delete_object(
                Bucket= self.bucket_name,
                Key = object_key
            )

            return True
        except ClientError as e:
            print(e)
            return False