from flask import Flask
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    
   

    # Initialize Swagger
   # Swagger(app, config=swagger_config)
   # Swagger(app, config=swagger_config, template=swagger_template)

    # Initialize configurations, database, routes, etc.
    app.config.from_object('config.Config')  # Load configurations (optional)

    # Import Blueprints
    from app.routs.user_routes import user_bp
    from app.routs.dashboardRoutes import dashboard_bp

    # Register Blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(dashboard_bp)


    return app
