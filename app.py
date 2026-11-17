
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = "CloudOps Status Portal"
APP_VERSION = "1.0.0"


@app.route("/")
def home():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "message": "Reliable deployments start with visibility.",
        "description": (
            "A demonstration application for learning "
            "Docker, CI/CD, and Kubernetes."
        ),
        "endpoints": {
            "home": "/",
            "health": "/health",
            "info": "/info"
        }
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": APP_NAME
    }), 200


@app.route("/info")
def info():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": "development"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
