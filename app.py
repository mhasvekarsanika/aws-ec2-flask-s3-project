from flask import Flask, request, render_template_string
import boto3

app = Flask(__name__)

# Use the IAM role (no need for keys)
s3 = boto3.client("s3")
BUCKET_NAME = "flask-app-s3-bucket-sanika"  

# Simple HTML form
html_form = """
    <h2>Upload File to S3</h2>
    <form method="post" enctype="multipart/form-data" action="/upload">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
   """

@app.route("/")
def index():
    return html_form

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    s3.upload_fileobj(file, BUCKET_NAME, file.filename)
    return f"✅ File {file.filename} uploaded to S3 bucket {BUCKET_NAME}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
