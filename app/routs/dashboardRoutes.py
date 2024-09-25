from flask import Blueprint, jsonify
from app.services.dashBoardService import DashboardService

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/api/dashboard', methods=['GET'])
def get_dashboard():
    try:
        stats = DashboardService.get_dashboard_stats()
        return jsonify({
            "code": 200,
            "data": stats,
            "message": "Dashboard data retrieved successfully"
        })
    except Exception as e:
        return jsonify({
            "code": 500,
            "message": f"Error retrieving dashboard data: {str(e)}"
        })
