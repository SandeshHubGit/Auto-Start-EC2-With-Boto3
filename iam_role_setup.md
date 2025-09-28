# 🔐 Task 2: IAM Role Setup for Lambda Function

In this step, we will create an IAM role that allows your Lambda function to start and stop EC2 instances.

---

## ✅ 1. Go to IAM Console

- Visit the [IAM Dashboard](https://console.aws.amazon.com/iam/).
- Click on **Roles** → **Create role**.

---

## ✅ 2. Choose Trusted Entity

- Select **AWS Service**
- Use Case: **Lambda**
- Click **Next**

---

## ✅ 3. Attach Policy

Choose:  
🔹 `AmazonEC2FullAccess` (for simplicity — can be scoped later for security)

➡️ Click **Next**

---

## ✅ 4. Name and Create Role

- Role Name: `LambdaEC2ManagementRole`
- (Optional) Add a description: `Allows Lambda to start/stop EC2 instances based on tags`

➡️ Click **Create Role**

---

## ✅ 5. Note ARN

- After creation, go to the role and **copy the Role ARN**
- You'll need this when creating the Lambda function

---

## 🔐 Optional (Advanced): Use Least Privilege

Instead of full access, use a custom inline policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": "*"
    }
  ]
}
```

Attach this via **Add inline policy** to follow best practices.

---

🎯 Your Lambda now has the permissions required to manage EC2 instances.