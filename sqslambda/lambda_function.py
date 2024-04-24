import boto3
import requests
import json

# Initialize SQS client
sqs = boto3.client('sqs')
SQS_QUEUE_URL = 'https://sqs.ap-south-1.amazonaws.com/590184140312/best1'

def lambda_handler(event, context):
    try:
        # Fetch data from the API Gateway endpoint using the API key
        url = 'https://mn7w2qsxpa.execute-api.ap-south-1.amazonaws.com/alpha/myresource'
        headers = {'x-api-key': 'y6dgJee62n9hfH2wfmMci5WmZFdxzLnQ54irTVZD'}
        response = requests.get(url, headers=headers)
        
        response_data = response.json()

        # Extract data from the response
        data = response_data.get('body', []) 

        # Send the data to the SQS queue
        for item in data:
            sqs.send_message(QueueUrl=SQS_QUEUE_URL, MessageBody=json.dumps(item))

        return {
            'statusCode': 200,
            'body': json.dumps('Data sent to SQS successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
