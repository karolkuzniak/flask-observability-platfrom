import logging
from flask import Flask, Response
from prometheus_client import Counter, generate_latest

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

logger = logging.getLogger(__name__)
app = Flask(__name__)

REQUEST_COUNT = Counter(
    "flask_request_total",
    "Total number of HTTP requests"
)

ERROR_COUNT = Counter(
    "flask_errors_total",
    "Total number of application errors"
)


@app.before_request
def before_request():
    REQUEST_COUNT.inc()


@app.route('/')
def home():
    logger.info("Home endpoint called")
    return "Flask DevOps Platform"


@app.route("/simulate-error")
def simulate_error():
    logger.error("Simulated error")
    ERROR_COUNT.inc()

    return {"error": "Simulated error"}, 500


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")


if __name__ == "__main__":
    logger.info("Starting app...")

    app.run(host="0.0.0.0", port=5000)
