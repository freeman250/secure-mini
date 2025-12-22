from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    bucket = os.environ.get("S3_BUCKET", "")
    key = os.environ.get("S3_BANNER_KEY", "banner.png")
    region = os.environ.get("AWS_REGION", "us-east-1")

    banner_url = ""
    if bucket:
        banner_url = f"https://{bucket}.s3.{region}.amazonaws.com/{key}"

    return render_template("index.html", banner_url=banner_url)


@app.route("/tips")
def tips():
    tips_list = [
        "Use strong and unique passwords",
        "Enable MFA on important accounts",
        "Avoid clicking unknown links",
        "Keep your system updated",
        "Use secure Wi-Fi networks"
    ]
    return render_template("tips.html", tips=tips_list)

@app.route("/checklist")
def checklist():
    checklist_items = [
        "Do I change passwords regularly?",
        "Is MFA enabled on my accounts?",
        "Do I avoid public Wi-Fi?",
        "Do I update my devices?",
        "Do I back up my files?"
    ]
    return render_template("checklist.html", checklist=checklist_items)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Cloud9 default
    app.run(host="0.0.0.0", port=port, debug=True)

