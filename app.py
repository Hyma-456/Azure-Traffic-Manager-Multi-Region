
import os
from flask import Flask, jsonify

app = Flask(__name__)

REGION = os.environ.get("APP_REGION", "Local Development")

@app.route("/")
def home():
    return f"""
    <html>
      <head><title>Azure Multi-Region Routing</title></head>
      <body style="font-family:Arial;text-align:center;margin-top:80px">
        <h1>Azure Traffic Manager Demo</h1>
        <h2>Application Region: {REGION}</h2>
        <p>Multi-region routing and automatic failover</p>
        <p>Health endpoint: <a href="/health">Check Health</a></p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        region=REGION
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))