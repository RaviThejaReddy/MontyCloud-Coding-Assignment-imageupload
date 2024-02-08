import json
import boto3
import os

s3 = boto3.client('s3', endpoint_url="http://localhost.localstack.cloud:4566")
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost.localstack.cloud:4566")
table_name = os.environ['IMAGE_METADATA_TABLE_NAME']
bucket_name = os.environ['IMAGE_S3_BUCKET_NAME']
table = dynamodb.Table(table_name)

def handler(event, context):
    try:
        image_id = event['pathParameters']['image_id']
        response = table.delete_item(
            Key={'image_id': image_id}
        )
        s3.delete_object(
            Bucket=bucket_name,
            Key=image_id
        )
        return {
            'statusCode': 204,
            'body': json.dumps('Image successfully deleted')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
