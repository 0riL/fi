from flask import Flask
import os

app = Flask(__name__)

# 👇 Your existing routes and logic go here

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
