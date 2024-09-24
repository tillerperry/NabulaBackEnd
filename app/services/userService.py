import uuid
from datetime import datetime
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
        
        
      
