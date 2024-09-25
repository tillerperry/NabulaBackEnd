import uuid
from datetime import datetime
from app.utils import dynamodb
from app.utils.dynamodb import add_user_to_dynamodb, GetSingleUserById,get_all_users


class UserService:
    
    @staticmethod
    def generate_uuid():
        """Generate a string UUID."""
        return str(uuid.uuid4())

    @staticmethod
    def get_current_timestamp():
        """Return current timestamp as a formatted string."""
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def create_user(self, user_data):
        """Create a user object and add it to DynamoDB."""
        # Generate unique IDs
        user_id = self.generate_uuid()
        student_id = self.generate_uuid()

        # Get current timestamp
        timestamp = self.get_current_timestamp()

        # Create the user object
        new_user = {
            'student_id': student_id,
            'full_name': user_data['full_name'],
            'age': user_data['age'],
            'occupation': user_data['occupation'],
            'nationality': user_data['nationality'],
            'marital_status': user_data['marital_status'],
            'email': user_data['email'],
            'created_at': timestamp,
            'id': user_id,
            'cohort': user_data['cohort']
        }

        # Add the user to DynamoDB
        add_user_to_dynamodb(new_user)
        return new_user
    
 
        
    def get_user_by_id(self,student_id):
        """Retrieve a user from DynamoDB by their student_id."""
        try:
            user = GetSingleUserById(student_id)
            if user:
                return user
        except Exception as e:
            print(e.response['Error']['Message'])
            return None
        
        
    def get_all_users(self):
        """Retrieve all users from DynamoDB."""
        try:
            users = get_all_users()
            return users
        except Exception as e:
            print(e.response['Error']['Message'])
            return None
        
        
    def authenticate_user(email, password):
        """
        Authenticates the user by email and password.
        For simplicity, we assume password is stored in plaintext.
        In production, use hashed passwords.
        """
        user_table = dynamodb.Table('Users')
        response = user_table.scan(
            FilterExpression="email = :email",
            ExpressionAttributeValues={":email": email}
        )

        if response['Items']:
            user = response['Items'][0]
            # Verify the password (in production, check hashed passwords)
            if user.get('password') == password:
                return user
        return None

    @staticmethod
    def update_logged_in_time(student_id, logged_in_at):
        """
        Updates the LoggedInAt field of the user with the given student_id.
        """
        user_table = dynamodb.Table('Users')
        user_table.update_item(
            Key={'student_id': student_id},
            UpdateExpression="SET LoggedInAt = :loggedInAt",
            ExpressionAttributeValues={":loggedInAt": logged_in_at}
        )  
      
