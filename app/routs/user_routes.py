import uuid
from flask import Blueprint, request, jsonify
from app.models.user import User
from app.utils.dynamodb import add_user_to_dynamodb
from app.services import UserService
#rom app.services.email_service import send_confirmation_email 
from datetime import datetime

##user_blueprint = Blueprint('user', __name__)
user_bp = Blueprint('user_routes', __name__)

@user_bp.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.json
        # Generate unique ID and timestamp
        user_id = str(uuid.uuid4())  # Ensure it's a string, not a list
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Ensure it's a single string, not a list

        new_user = User(
            full_name=data['full_name'],
            age=data['age'],
            occupation= data['occupation'],
            nationality=data['nationality'],
            marital_status = data['marital_status'],
            email=data['email'],
            created_at=timestamp,
            id = user_id,
            student_id = str(uuid.uuid4())
        )
        
        user_dict = new_user.to_dict()
        print(user_dict)
        add_user_to_dynamodb(user_dict)
            # send_confirmation_email(new_user.email)
        return jsonify({'message': 'User added successfully', 'data': user_dict, 'code': str(201)}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@user_bp.route('/user/{id}', methods=['GET'])
def getSingleUserAsync(id):
    try:
        # Use UserService to get the user by student_id
        userService =  UserService()
        user =  userService.get_user_by_id(id)
      
        
        if user == None:
           return jsonify({
            "code": "404",
            "message": 'User not found'
        }), 404

        return jsonify({
                "code": "200",
                "data": user,
                "message": "User fetched successfully"
            }), 200
        
    except Exception as e:
        return jsonify({
            "code": "500",
            "error": str(e)
        }), 500