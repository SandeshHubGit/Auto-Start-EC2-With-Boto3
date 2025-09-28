# 🖥️ Task 1: EC2 Setup and Tagging

This task walks you through launching and tagging two EC2 instances to be managed automatically by an AWS Lambda function using Boto3.

---

## ✅ 1. Launch Two EC2 Instances

1. Navigate to the **EC2 Dashboard** in AWS Console.
2. Click **Launch Instance** → Choose:
   - Name: `AutoManage-Stop`
   - AMI: Amazon Linux 2 or Ubuntu (Free Tier)
   - Instance type: `t2.micro` (Free Tier eligible)
   - Key Pair: Create or select existing one
   - Allow HTTP (optional) + SSH (recommended)
3. Repeat to create a second instance:  
   - Name: `AutoManage-Start`

---

## ✅ 2. Apply Tags

Tag the instances with the following key-value pair:

| Instance         | Tag Key | Tag Value   |
|------------------|---------|-------------|
| AutoManage-Stop  | Action  | Auto-Stop   |
| AutoManage-Start | Action  | Auto-Start  |

Steps:
- Select the instance → `Tags` tab → `Manage Tags` → `Add Tag`
- Key = `Action`, Value = `Auto-Stop` or `Auto-Start`

---

## ✅ 3. Verify

- Go to **Instances > Tags** and confirm both instances have the appropriate tags.

You are now ready to write the Lambda function that will stop and start these instances automatically based on their tags!