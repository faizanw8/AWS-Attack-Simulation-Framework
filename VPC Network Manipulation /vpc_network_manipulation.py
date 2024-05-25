import boto3
import argparse

def add_route_to_route_table(route_table_id, destination_cidr_block, target_id):
    """
    Add a route to a specified route table.
    
    Args:
    - route_table_id: ID of the route table to manipulate.
    - destination_cidr_block: The CIDR block for the new route.
    - target_id: The target (e.g., internet gateway or instance) for the route.
    """
    ec2_client = boto3.client('ec2')
    
    try:
        ec2_client.create_route(
            RouteTableId=route_table_id,
            DestinationCidrBlock=destination_cidr_block,
            GatewayId=target_id  # You can change this to InstanceId, NatGatewayId, etc.
        )
        print(f"Route added to route table '{route_table_id}': {destination_cidr_block} -> {target_id}")
    except Exception as e:
        print(f"Failed to add route to route table: {e}")

def update_security_group(security_group_id, port, protocol='tcp'):
    """
    Update a security group to allow ingress traffic from any IP address on a specified port.
    
    Args:
    - security_group_id: ID of the security group to manipulate.
    - port: The port to allow traffic on.
    - protocol: The protocol (default is 'tcp').
    """
    ec2_client = boto3.client('ec2')
    
    try:
        ec2_client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {
                    'IpProtocol': protocol,
                    'FromPort': port,
                    'ToPort': port,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )
        print(f"Ingress traffic allowed on port {port} for security group '{security_group_id}'")
    except Exception as e:
        print(f"Failed to update security group: {e}")

def main():
    parser = argparse.ArgumentParser(description='VPC Network Manipulation Script')
    
    # Route Table Manipulation Arguments
    parser.add_argument('--route-table-id', help='ID of the route table to manipulate')
    parser.add_argument('--destination-cidr', help='Destination CIDR block for the new route')
    parser.add_argument('--target-id', help='Target ID for the route (e.g., Internet Gateway ID)')
    
    # Security Group Manipulation Arguments
    parser.add_argument('--security-group-id', help='ID of the security group to manipulate')
    parser.add_argument('--port', type=int, help='Port to allow ingress traffic on')
    
    args = parser.parse_args()
    
    if args.route_table_id and args.destination_cidr and args.target_id:
        add_route_to_route_table(args.route_table_id, args.destination_cidr, args.target_id)
    
    if args.security_group_id and args.port:
        update_security_group(args.security_group_id, args.port)

if __name__ == "__main__":
    main()
