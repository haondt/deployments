import logging
from flask import Flask, request
import json

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
    headers_string = ""
    try:
        headers_string = json.dumps(dict(request.headers), indent=4)
    except:
        headers_string = str(dict(request.headers))
    logger.info(f"Headers: {headers_string}")
    body_string = ""
    try:
        body_string = json.dumps(request.get_json(), indent=4)
    except:
        body_string = request.get_data().decode('utf-8')
    logger.info(f"Body: {body_string}")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
