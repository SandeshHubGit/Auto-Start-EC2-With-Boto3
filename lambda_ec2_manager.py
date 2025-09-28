import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')

    # -------- Auto-Stop Instances --------
    stop_response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Action',
                'Values': ['Auto-Stop']
            },
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )

    stop_ids = [
        instance['InstanceId']
        for reservation in stop_response['Reservations']
        for instance in reservation['Instances']
    ]

    if stop_ids:
        print(f"Stopping instances: {stop_ids}")
        ec2.stop_instances(InstanceIds=stop_ids)
    else:
        print("No instances to stop.")

    # -------- Auto-Start Instances --------
    start_response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Action',
                'Values': ['Auto-Start']
            },
            {
                'Name': 'instance-state-name',
                'Values': ['stopped']
            }
        ]
    )

    start_ids = [
        instance['InstanceId']
        for reservation in start_response['Reservations']
        for instance in reservation['Instances']
    ]

    if start_ids:
        print(f"Starting instances: {start_ids}")
        ec2.start_instances(InstanceIds=start_ids)
    else:
        print("No instances to start.")

    return {
        'stopped_instances': stop_ids,
        'started_instances': start_ids
    }