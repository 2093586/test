import boto3
import os

def check_service_status(cluster_name, service_name):
    client = boto3.client('ecs')
    response = client.describe_services(
        cluster=cluster_name,
        services=[service_name]
    )
    
    if not response['services']:
        print(f"Service {service_name} not found in cluster {cluster_name}.")
        return
    
    service = response['services'][0]
    status = service['status']
    desired_count = service['desiredCount']
    running_count = service['runningCount']
    
    print(f"Service {service_name} status: {status}")
    print(f"Desired count: {desired_count}")
    print(f"Running count: {running_count}")
    
    if running_count > 0:
        print(f"Service {service_name} is running.")
    else:
        print(f"Service {service_name} is not running.")

if __name__ == "__main__":
    cluster_name = os.getenv('CLUSTER_NAME')
    service_name = os.getenv('SERVICE_NAME')
    
    check_service_status(cluster_name, service_name)
