# The script has two functions

## add_route_to_route_table Function:
This function Adds a new route to a specified route table.
It requires following Arguments:
1. route_table_id: The ID of the route table to modify.
2. destination_cidr_block: The CIDR block for the new route.
3. target_id: The target (e.g., an internet gateway ID) for the route.


## update_security_group Function:

This function updates a security group to allow ingress traffic from any IP address on a specified port.

It requires following arguments:
1. security_group_id: The ID of the security group to modify.
2. port: The port to allow traffic on.
3. protocol: The protocol to allow (default is 'tcp').

## Running the Script

Save the script as vpc_network_manipulation.py and run it from the command line. Example usage:

### To add a route to a route table:

`python vpc_network_manipulation.py --route-table-id rtb-12345678 --destination-cidr 0.0.0.0/0 --target-id igw-12345678`

### To update a security group to allow ingress traffic on port 80:

`python vpc_network_manipulation.py --security-group-id sg-12345678 --port 80`


Prerequisites

AWS Credentials: Ensure you have AWS credentials configured with sufficient permissions to modify route tables and security groups. Configure AWS credentials using the AWS CLI (aws configure).

Permissions: The IAM user or role running this script must have permissions for the following actions:

ec2:CreateRoute
ec2:AuthorizeSecurityGroupIngress

