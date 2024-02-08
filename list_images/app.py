import json
import os
import boto3

dynamodb = boto3.resource('dynamodb',endpoint_url="http://localhost.localstack.cloud:4566",aws_access_key_id='test',aws_secret_access_key='test',aws_session_token='test',region_name='us-east-1')
table = dynamodb.Table(os.environ['IMAGE_METADATA_TABLE_NAME'])

def handler(event, context):
    try:
        response = table.scan()
        image_list = response.get('Items', [])
        return {
            'statusCode': 200,
            'body': json.dumps(image_list)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
