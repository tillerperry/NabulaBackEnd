from flask import Flask

def create_app():
    app = Flask(__name__)

    # Initialize configurations, database, routes, etc.
    app.config.from_object('config.Config')  # Load configurations (optional)

    # Import Blueprints
    from app.routs.user_routes import user_bp
    #from app.routs.dashboard_routes import dashboard_blueprint

    # Register Blueprints
    app.register_blueprint(user_bp)
  ##  app.register_blueprint(dashboard_blueprint)

    return app
