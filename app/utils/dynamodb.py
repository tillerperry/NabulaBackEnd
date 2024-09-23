import boto3 

dynamodb = boto3.resource('dynamodb')
user_table = dynamodb.Table('StudentRecords')

def  add_user_to_dynamodb(user_data):
    user_table.put_item(Item=user_data)

def get_all_users():
    response = user_table.scan()
    return response['Items']


def GetSingleUserById(student_id):
  #get single user
    try:
        response = user_table.get_item(
            Key={
                'student_id': student_id
            }
        )
        return response.get('Item')
    except Exception as e:
        raise Exception(f"Error fetching user: {str(e)}")
        return None
    
    
    
    
def GetSingleUserByEmail(email):
  #get single user
    try:
        response = user_table.get_item(
            Key={
                'email': email
            }
        )
        return response.get('Item')
    except Exception as e:
        raise Exception(f"Error fetching user: {str(e)}")
        return None