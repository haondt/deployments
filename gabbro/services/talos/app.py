import logging
from flask import Flask, request

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/wh', methods=['POST'])
def pipeline_webhook():
    # Log request details
    logger.info("Received request:")
    logger.info(f"URL: {request.url}")
    logger.info(f"Requester IP: {request.remote_addr}")
    logger.info(f"Headers: {dict(request.headers)}")
    logger.info(f"Body: {request.get_json()}")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
