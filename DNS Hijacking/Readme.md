## This script accepts the following command-line arguments:

--zone-id: The ID of the Route 53 hosted zone containing the domain to be hijacked.
--domain: The domain name to be hijacked.
--malicious-ip: The malicious IP address to which traffic will be redirected.

To use the script, run it from the command line with the required arguments. For example:

`python dns_hijacking.py --zone-id Z1234567890123 --domain example.com --malicious-ip 192.0.2.123`

**Replace Z1234567890123, example.com, and 192.0.2.123 with the actual Route 53 hosted zone ID, domain name, and malicious IP address, respectively.**

This script demonstrates how an attacker could hijack DNS records to redirect traffic from a legitimate domain to a malicious IP address, potentially facilitating various types of attacks, such as phishing or man-in-the-middle attacks.

Prerequisites:
1. AWS Credentials: Ensure you have AWS credentials configured that have sufficient permissions to modify Route 53 records. You can configure AWS credentials using the AWS CLI by running aws configure.

2. Permissions: The IAM user or role running this script must have permissions for the following actions:

    route53:ListResourceRecordSets
    route53:ChangeResourceRecordSets


