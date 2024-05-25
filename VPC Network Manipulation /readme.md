Explanation
Imports:

argparse: For parsing command-line arguments.
boto3: The AWS SDK for Python to interact with AWS services.
add_route_to_route_table Function:

Adds a new route to a specified route table.
Arguments:
route_table_id: The ID of the route table to modify.
destination_cidr_block: The CIDR block for the new route.
target_id: The target (e.g., an internet gateway ID) for the route.
update_security_group Function:

Updates a security group to allow ingress traffic from any IP address on a specified port.
Arguments:
security_group_id: The ID of the security group to modify.
port: The port to allow traffic on.
protocol: The protocol to allow (default is 'tcp').
main Function:

Sets up argument parsing.
Checks if the necessary arguments are provided for route table manipulation and security group manipulation.
Calls the appropriate functions based on the provided arguments.
Running the Script
Save the script as vpc_network_manipulation.py and run it from the command line. Example usage:

To add a route to a route table:

python vpc_network_manipulation.py --route-table-id rtb-12345678 --destination-cidr 0.0.0.0/0 --target-id igw-12345678

To update a security group to allow ingress traffic on port 80:

python vpc_network_manipulation.py --security-group-id sg-12345678 --port 80


Prerequisites
AWS Credentials: Ensure you have AWS credentials configured with sufficient permissions to modify route tables and security groups. Configure AWS credentials using the AWS CLI (aws configure).

Permissions: The IAM user or role running this script must have permissions for the following actions:

ec2:CreateRoute
ec2:AuthorizeSecurityGroupIngress

Important Considerations

Testing Environment: Always test such scripts in a safe and controlled environment. Unauthorized use of these techniques can be illegal and unethical.
Ethical Usage: Ensure that you have proper authorization to perform such actions on the target AWS account. This script is for educational and authorized testing purposes only.
