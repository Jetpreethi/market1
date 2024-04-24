import boto3
import json

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('sns')

sns_topic_arn = 'arn:aws:sns:ap-south-1:590184140312:market'

def send_sns(messages, subject):
    try:
        client = boto3.client('sns')
        message = "\n".join(messages)  # Concatenate all messages into a single string
        result = client.publish(TopicArn=sns_topic_arn, Message=message, Subject=subject)
        if result['ResponseMetadata']['HTTPStatusCode'] == 200:
            print("Notification sent successfully")
            return True
    except Exception as e:
        print("Error in sending notification:", str(e))
        return False

def lambda_handler(event, context):
    try:
        messages = []  # Accumulator for message bodies

        # Query DynamoDB table to retrieve stored messages
        response = table.scan()
        items = response.get('Items', [])
        
        for item in items:
            message_body = {
                'timestamp': item['timestamp'],
                'symbol': item.get('symbol', ''),
                'dayHigh': str(item.get('dayHigh', '')),
                'dayLow': str(item.get('dayLow', '')),
                'lastPrice': str(item.get('lastPrice', ''))
            }
            # Convert message body to JSON string
            message_json = json.dumps(message_body)
            # Append message body to the accumulator
            messages.append(message_json)

        # Send accumulated messages as one notification
        if messages:
            subject = "Process completion notification"
            if send_sns(messages, subject):
                print("Notification sent.")
                return {
                    'statusCode': 200,
                    'body': json.dumps('Messages processed successfully!')
                }
            else:
                print("Failed to send notification.")
                return {
                    'statusCode': 500,
                    'body': json.dumps('Failed to send notification.')
                }
        else:
            print("No messages to process.")
            return {
                'statusCode': 200,
                'body': json.dumps('No messages to process.')
            }
    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps('Internal server error.')
        }

            
          
            
