import boto3
from botocore.exceptions import NoCredentialsError
import os

def upload_to_s3(local_file_path, bucket_name, s3_key=None):
    if s3_key is None:
        s3_key = os.path.basename(local_file_path)
    # Create an S3 client
    s3 = boto3.client('s3')

    try:
        # Upload the file
        s3.upload_file(local_file_path, bucket_name, s3_key)
        print(f"File uploaded successfully to {bucket_name}/{s3_key}")

    except FileNotFoundError:
        print(f"The file {local_file_path} was not found.")

    except NoCredentialsError:
        print("Credentials not available")

# Example usage
local_file_path = "kp2.pem"
bucket_name = "anirudhraolearning"


upload_to_s3(local_file_path, bucket_name)
