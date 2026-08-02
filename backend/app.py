from flask import Flask
from flask_cors import CORS
from backend.routes.search import search_bp
from backend.routes.predict import predict_bp


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register route blueprints
    app.register_blueprint(search_bp, url_prefix="/api/search")
    app.register_blueprint(predict_bp, url_prefix="/api/predict")

    @app.route("/")
    def health():
        return {"status": "ok"}

    return app


if __name__ == "__main__":
    create_app().run(debug=True, host='0.0.0.0', port=5000)
