import boto3
import sys

def scale_ecs_service(cluster_name, service_name, desired_count):
    client = boto3.client('ecs')
    response = client.update_service(
        cluster=cluster_name,
        service=service_name,
        desiredCount=desired_count
    )
    return response

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python scale_service.py <cluster_name> <service_name> <desired_count>")
        sys.exit(1)
    
    cluster_name = sys.argv[1]
    service_name = sys.argv[2]
    desired_count = int(sys.argv[3])
    
    response = scale_ecs_service(cluster_name, service_name, desired_count)
    print(response)
