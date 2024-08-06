import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('VisitorCounter')

def lambda_handler(event, context):
    response = table.update_item(
        Key={'id': 'visitor_count'},
        UpdateExpression='ADD #count :incr',
        ExpressionAttributeNames={'#count': 'count'},
        ExpressionAttributeValues={':incr': 1},
        ReturnValues='UPDATED_NEW'
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Visitor count updated to {}'.format(response['Attributes']['count']))
    }
