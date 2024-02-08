import json
import boto3
import os

s3 = boto3.client('s3', endpoint_url="http://localhost.localstack.cloud:4566")
bucket_name = os.environ['IMAGE_S3_BUCKET_NAME']

def handler(event, context):
    try:
        image_id = event['pathParameters']['image_id']
        image_url = get_image_url_from_dynamodb(image_id)
        if not image_url:
            return {
                'statusCode': 404,
                'body': json.dumps('Image not found')
            }
        response = s3.get_object(
            Bucket=bucket_name,
            Key=image_id
        )
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/octet-stream'},
            'body': response['Body'].read()
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

def get_image_url_from_dynamodb(image_id):
    return "https://{}/{}".format(os.environ['IMAGE_S3_BUCKET_NAME'], image_id)
