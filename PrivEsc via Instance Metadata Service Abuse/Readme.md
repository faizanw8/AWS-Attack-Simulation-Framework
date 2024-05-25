The metadata_service_abuse.py script is designed to be run from within an AWS EC2 instance against instances that rely on IMDSv1. This is because it leverages the EC2 instance metadata service, which is only accessible from within the instance itself. The metadata service provides information about the instance and its associated IAM role credentials, and it is available at a well-known URL (http://169.254.169.254/latest/meta-data/).

For Instances that  enforce IMDSv2, please run metadata_service_abuse_imdsv2.py
For IMDSv2, the process is a bit lengthy: 
#### Token Retrieval:

1. Added the get_token function to retrieve a session token from the EC2 instance metadata service (IMDSv2).
2. The token is requested with a specified TTL (Time to Live) of 21600 seconds (6 hours).

#### Using the Token:
1. Modified the get_instance_metadata_v2 function to use the session token when making requests to retrieve the IAM role name and credentials.
2. Added the necessary headers (X-aws-ec2-metadata-token) to the requests.

## Expected Output
If the script runs successfully, it will retrieve and print the IAM role credentials associated with the EC2 instance. The output will look something like this:

{
    "Code": "Success",
    "LastUpdated": "2024-05-25T12:34:56Z",
    "Type": "AWS-HMAC",
    "AccessKeyId": "ASIAEXAMPLE",
    "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "Token": "FQoGZXIvYXdzEAwaD...",
    "Expiration": "2024-05-25T18:34:56Z"
}
