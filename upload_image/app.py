import json
import boto3
import uuid
from urllib.parse import unquote_plus
import os


s3 = boto3.client('s3',endpoint_url="http://localhost.localstack.cloud:4566",aws_access_key_id='test',aws_secret_access_key='test',aws_session_token='test',region_name='us-east-1')
dynamodb = boto3.resource('dynamodb',endpoint_url="http://localhost.localstack.cloud:4566",aws_access_key_id='test',aws_secret_access_key='test',aws_session_token='test',region_name='us-east-1')
table = dynamodb.Table(os.environ['IMAGE_METADATA_TABLE_NAME'])


def handler(event, context):
    try:
        print(f'incoming event -> {event}')
        metadata = json.loads(event['body'])['metadata']
        image_key = str(uuid.uuid4())
        s3.put_object(
            Bucket=os.environ['IMAGE_S3_BUCKET_NAME'],
            Key=image_key,
            Body=unquote_plus(json.loads(event['body'])['file']),
            ContentEncoding='base64',
            ContentType='image/jpeg'
        )

        table.put_item(Item={
            'image_id': image_key,
            'username': metadata['username'],
            'filename': metadata['filename'],
            's3Url': ''
        })

        response = {
            'statusCode': 200,
            'body': json.dumps('Image uploaded successfully')
        }
    except Exception as e:
        response = {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

    return response
