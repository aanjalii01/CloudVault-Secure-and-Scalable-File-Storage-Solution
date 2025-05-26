import boto3
from botocore.exceptions import ClientError
from flask import current_app

def get_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
        region_name=current_app.config['AWS_S3_REGION']
    )

def upload_file_to_s3(file_obj, filename) -> bool:
    s3 = get_s3_client()
    bucket = current_app.config['AWS_S3_BUCKET_NAME']
    try:
        s3.upload_fileobj(file_obj, bucket, filename)
        return True
    except ClientError as e:
        print(f"S3 Upload Error: {e}")
        return False

def download_file_from_s3(filename) -> bytes | None:
    s3 = get_s3_client()
    bucket = current_app.config['AWS_S3_BUCKET_NAME']
    try:
        file_obj = s3.get_object(Bucket=bucket, Key=filename)
        return file_obj['Body'].read()
    except ClientError as e:
        print(f"S3 Download Error: {e}")
        return None

def delete_file_from_s3(filename) -> bool:
    s3 = get_s3_client()
    bucket = current_app.config['AWS_S3_BUCKET_NAME']
    try:
        s3.delete_object(Bucket=bucket, Key=filename)
        return True
    except ClientError as e:
        print(f"S3 Delete Error: {e}")
        return False

def list_user_files_s3(prefix: str) -> list[str]:
    s3 = get_s3_client()
    response = s3.list_objects_v2(Bucket=current_app.config['AWS_S3_BUCKET_NAME'], Prefix=prefix)
    return [obj['Key'] for obj in response.get('Contents', []) if obj['Key'] != prefix]

def list_all_files_s3() -> list[str]:
    s3 = get_s3_client()
    response = s3.list_objects_v2(Bucket=current_app.config['AWS_S3_BUCKET_NAME'])
    return [obj['Key'] for obj in response.get('Contents', [])]
