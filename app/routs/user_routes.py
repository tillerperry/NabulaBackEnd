from flask import Blueprint, request, jsonify
from app.models.user import User
from app.utils.dynamodb import add_user_to_dynamodb 
#rom app.services.email_service import send_confirmation_email 
from datetime import datetime



##user_blueprint = Blueprint('user', __name__)

user_bp = Blueprint('user_routes', __name__)

@user_bp.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(
        full_name=data['full_name'],
        age=data['age'],
        occupation=data['occupation'],
        nationality=data['nationality'],
        marital_status=data['marital_status'],
        email=data['email'],
        created_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    add_user_to_dynamodb(new_user.to_dict())
     # send_confirmation_email(new_user.email)
    return jsonify({'message': 'User added successfully'}), 201
