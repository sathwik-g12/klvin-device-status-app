from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Allow URLs with and without trailing slash
    app.url_map.strict_slashes = False

    from routes.companies import companies_bp
    from routes.devices import devices_bp

    app.register_blueprint(companies_bp, url_prefix="/companies")
    app.register_blueprint(devices_bp, url_prefix="/devices")

    @app.route("/")
    def home():
        return {"message": " Backend Running"}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
