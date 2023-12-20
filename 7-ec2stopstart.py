#Automate AWS EC2 Instance Start/Stop:

import boto3

def start_stop_ec2_instances(instance_ids, action):
    ec2 = boto3.client('ec2', region_name='your-region')

    if action == 'start':
        ec2.start_instances(InstanceIds=instance_ids)
        print(f"EC2 instances {instance_ids} started.")
    elif action == 'stop':
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"EC2 instances {instance_ids} stopped.")
    else:
        print("Invalid action. Use 'start' or 'stop'.")

# Example usage:
instance_ids_to_manage = ['i-1234567890abcdef0', 'i-0987654321abcdef1']
start_stop_ec2_instances(instance_ids_to_manage, action='start')
