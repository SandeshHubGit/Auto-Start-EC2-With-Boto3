# Auto-Start-EC2-With-Boto3

## 🚀 AWS Lambda EC2 Instance Automation with Boto3

This project uses AWS Lambda + Boto3 (Python) to automate **starting and stopping EC2 instances** based on their tags (`Auto-Start`, `Auto-Stop`).

---

## 📁 Project Structure

```
.
├── 01_ec2_setup/             # EC2 instance tagging instructions
├── 02_iam_lambda_role/       # IAM role setup for Lambda
├── 03_lambda_function/       # Boto3 Lambda function
├── 04_documentation/         # README
```

---

## ✅ Task-by-Task Breakdown

### 🖥️ Task 1: EC2 Setup

1. Launch 2 EC2 instances (e.g., t2.micro).
2. Apply these tags:
   - Instance 1: `Action=Auto-Stop`
   - Instance 2: `Action=Auto-Start`
3. Confirm tags under EC2 → Instances → Tags tab.

📸 _Screenshot to include:_
- EC2 instances page showing `Auto-Stop` and `Auto-Start` tags

---

### 🔐 Task 2: IAM Role for Lambda

1. Create IAM Role for Lambda
2. Attach `AmazonEC2FullAccess` or minimal policy
3. Note the IAM Role ARN

📸 _Screenshot to include:_
- IAM role permissions summary
- IAM role attached to Lambda

---

### 🐍 Task 3: Lambda Function

- Use Python 3.x + Boto3 to manage EC2 instances.
- File: `03_lambda_function/lambda_ec2_manager.py`

✅ What it does:
- Starts EC2s tagged `Auto-Start` (if `stopped`)
- Stops EC2s tagged `Auto-Stop` (if `running`)

📸 _Screenshot to include:_
- Lambda code editor with Python script pasted
- Successful log output from test run

---

### 🧪 Task 4: Manual Invocation & Test

1. Go to **Lambda Console**
2. Click **Test** → Configure a test event → Choose `Hello World` → Save
3. Click **Test** again to invoke the function
4. View log output in CloudWatch
5. Confirm EC2 instances changed state:
   - `Auto-Stop` instance is now stopped
   - `Auto-Start` instance is now running

---
