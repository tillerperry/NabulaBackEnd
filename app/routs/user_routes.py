import random
import uuid
from flask import Blueprint, request, jsonify
from app.models.user import User
from app.utils.dynamodb import add_user_to_dynamodb
from app.services.userService import UserService
#rom app.services.email_service import send_confirmation_email 
from datetime import datetime

##user_blueprint = Blueprint('user', __name__)
user_bp = Blueprint('user_routes', __name__)

@user_bp.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.json
        # Generate unique ID and timestamp
       
 
        new_user = User(
            fullName = data['fullName'],
            age=data['age'],
            occupation= data['occupation'],
            nationality=data['nationality'],
            maritalStatus =  data['maritalStatus'],
            email=data['email'],
            cohort = data['cohort'],
            createdAt =None,
            id=None,
            student_id=None
        )
        
     
        user_dict = new_user.to_dict()
       
        add_user_to_dynamodb(user_dict)
            # send_confirmation_email(new_user.email)
        return jsonify({'message': 'User added successfully', 'data': user_dict, 'code': str(201)}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@user_bp.route('/user/<id>', methods=['GET'])
def getSingleUserAsync(id):
    try:
        # Use UserService to get the user by student_id
        userService =  UserService()
        user =  userService.get_user_by_id(id)
      
        
        if user == None:
           return jsonify({
            "code": "404",
            "message": 'User not found',
            "data": None
            
        }), 404

        return jsonify({
                "code": "200",
                "data": user,
                "message": "User fetched successfully"
            }), 200
        
    except Exception as e:
        return jsonify({
            "code": "500",
            "data": None,
            "error": str(e)
        }), 500
        
@user_bp.route('/users', methods=['GET'])
def getAllUsersAsync():
    try:
        # Use UserService to get all users
        userService =  UserService()
        users =  userService.get_all_users()
        if users == None:
            return jsonify({
                "code": "404",
                "message": 'No users found',
                "data": None
                
            }), 404

        return jsonify({
                "code": "200",
                "data": users,
                "message": "Users fetched successfully"
            }), 200
        
    except Exception as e:
        return jsonify({
            "code": "500",
            "data": None,
            "error": str(e)
        }), 500