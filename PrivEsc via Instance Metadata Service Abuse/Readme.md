the metadata_service_abuse.py script is designed to be run from within an AWS EC2 instance. This is because it leverages the EC2 instance metadata service, which is only accessible from within the instance itself. The metadata service provides information about the instance and its associated IAM role credentials, and it is available at a well-known URL (http://169.254.169.254/latest/meta-data/).


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
