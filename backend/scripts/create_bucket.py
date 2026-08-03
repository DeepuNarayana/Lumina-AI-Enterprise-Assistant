import boto3

from botocore.exceptions import ClientError

BUCKET_NAME =  "lumina-ai-deepu-834948484949"

s3= boto3.client("s3", region_name="ap-south-1")

try:
    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={
            "LocationConstraint": "ap-south-1"
        }
    )
    print(f"Bucket'{BUCKET_NAME}' created successfully")

except ClientError as e:
    print("error")
    print(e)
