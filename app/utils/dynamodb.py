import boto3 

dynamodb = boto3.resource('dynamodb')
user_table = dynamodb.Table('GoldGridUsers')

def add_user_to_dynamodb(user_data):
    user_table.put_item(Item=user_data)

def get_all_users():
    response = user_table.scan()
    return response['Items']
