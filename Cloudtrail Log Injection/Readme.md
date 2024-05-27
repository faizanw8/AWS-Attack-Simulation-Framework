## User Inputs:
#### The script now prompts the user to input the necessary variables:
1. event_name: The name of the event (e.g., "StartInstances").
2. event_source: The source of the event (e.g., "ec2.amazonaws.com").
3. user_identity: A dictionary with details about the user identity.
4. aws_region: The AWS region where the event took place.
5. additional_fields: A dictionary with additional fields such as requestParameters, responseElements, additionalEventData, and recipientAccountId.

#### Datetime Handling:
The event_time is automatically set to the current UTC time using datetime.utcnow().

#### JSON Input Handling:

additional_fields components (requestParameters, responseElements, additionalEventData) are expected as JSON strings from the user, which are then converted to dictionaries using json.loads().


## Running the Script

#### Install Required Libraries:
1. Ensure you have the AWS SDK for Python (boto3) installed
`pip install boto3`


#### Configure AWS CLI:

1. Make sure the AWS CLI is configured with appropriate credentials:

`aws configure`


#### Run the Script:

1. Execute the script using Python:

`python3 cloudtrail_log_injection.py`


#### Provide Inputs:

When prompted, enter the required details. Example inputs might look like this:

`Enter the event name: StartInstances`
`Enter the event source (e.g., ec2.amazonaws.com): ec2.amazonaws.com`
`Enter the user identity type (e.g., IAMUser): IAMUser`
`Enter the principal ID: EX_PRINCIPAL_ID`
`Enter the ARN: arn:aws:iam::123456789012:user/Alice`
`Enter the account ID: 123456789012`
`Enter the access key ID: EXAMPLE_KEY_ID`
`Enter the user name: Alice`
`Enter the AWS region (e.g., us-west-2): us-west-2`
`Enter request parameters as JSON string: {"instancesSet": {"items": [{"instanceId": "i-1234567890abcdef0"}]}}`
`Enter response elements as JSON string: {"instancesSet": {"items": [{"instanceId": "i-1234567890abcdef0"}]}}`
`Enter additional event data as JSON string: {}`
`Enter the recipient account ID: 123456789012`




**Permissions: Ensure that the IAM user or role running these scripts has sufficient permissions to interact with CloudTrail.**
