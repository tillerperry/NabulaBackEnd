from app.utils.dynamodb import get_all_users
from collections import Counter
from datetime import datetime

class DashboardService:
   
    def get_dashboard_stats():
        # Fetch all users
        users = get_all_users()

        # Number of users
        total_users = len(users)

        # Extract login timestamps
        login_timestamps = [user['createdAt'] for user in users]

        # Nationality counts
        nationalities = [user['nationality'] for user in users]
        nationality_counts = Counter(nationalities)

        return {
            "total_users": total_users,
            "login_timestamps": login_timestamps,
            "nationality_counts": nationality_counts
        }
