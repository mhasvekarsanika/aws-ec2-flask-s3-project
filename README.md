In this project, we deployed a Flask web application on an AWS EC2 instance using Amazon Linux OS.
The app allows users to upload files via browser, which are then stored in an Amazon S3 bucket.
For secure access, we used an IAM Role attached to EC2 instead of root credentials.
Tools Used:
AWS EC2 (Amazon Linux 2023)
Amazon S3 (File Storage)
IAM Role (S3 Access)
Flask (Python web framework)
Boto3 (AWS SDK for Python)
PuTTY (for SSH connection from Windows)
Flow:
User (Browser) → EC2 Instance (Flask App) → S3 Bucket (File Storage)
1. Launch EC2 Instance
Open AWS Console → EC2 → Launch Instance
AMI: Amazon Linux 2023
Instance Type: t2.micro (Free Tier)
Key Pair: Download .pem file
Security Group Rules:
SSH (22) → My IP
HTTP (80) → Anywhere
Custom TCP (5000) → Anywhere

2.Connect EC2 using PuTTY
Convert .pem to .ppk using PuTTYgen
Load → Save private key → my-key.ppk
Open PuTTY → Hostname:
ec2-user@<Your-EC2-Public-IP>
In PuTTY → Connection → SSH → Auth → Browse → Select .ppk file

3. Update & Install Dependencies
Inside PuTTY (EC2 shell):
sudo dnf update -y
sudo dnf install python3 -y
sudo dnf install python3-pip -y
pip3 install flask boto3

Open → login as: ec2-user
✅ Now you are connected to EC2 server.

5. Create S3 Bucket
Go to AWS Console → S3 → Create bucket
Name: flask-app-s3-bucket-<yourname> (must be unique)
Region: same as EC2
Default settings → Create

6. Create IAM Role for S3 Access
IAM → Roles → Create Role
Trusted entity: EC2
Attach policy: AmazonS3FullAccess
Role name: EC2-S3FullAccess-Role

Go to EC2 → Select Instance → Actions → Security → Modify IAM Role → Attach this role
