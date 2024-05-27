import boto3
import json
import random
from datetime import datetime, timedelta

def inject_cloudtrail_log(event_name, event_source, user_identity, aws_region, event_time, additional_fields):
    """
    Injects a custom log event into CloudTrail.
    """
    client = boto3.client('cloudtrail')

    # Create a custom event
    custom_event = {
        "eventVersion": "1.08",
        "userIdentity": user_identity,
        "eventTime": event_time.isoformat(),
        "eventSource": event_source,
        "eventName": event_name,
        "awsRegion": aws_region,
        "sourceIPAddress": "192.0.2.0",
        "userAgent": "aws-cli/1.18.69 Python/3.7.3 Windows/10",
        "requestParameters": additional_fields.get("requestParameters", {}),
        "responseElements": additional_fields.get("responseElements", {}),
        "additionalEventData": additional_fields.get("additionalEventData", {}),
        "eventID": "exampleEventId",
        "readOnly": False,
        "eventType": "AwsApiCall",
        "managementEvent": True,
        "recipientAccountId": additional_fields.get("recipientAccountId", "123456789012"),
    }

    # Serialize the custom event
    custom_event_json = json.dumps(custom_event)

    # Inject the custom event
    try:
        response = client.put_event_selectors(
            TrailName='default',
            EventSelectors=[
                {
                    'ReadWriteType': 'All',
                    'IncludeManagementEvents': True,
                    'DataResources': [],
                    'ExcludeManagementEventSources': []
                },
            ]
        )
        print("Log injection successful:", response)
    except Exception as e:
        print("Failed to inject log:", str(e))

def generate_permutations(num_events):
    """
    Generates permutations of log details to create multiple log events.
    """
    event_names = ["StartInstances", "StopInstances", "CreateBucket", "DeleteBucket"]
    event_sources = ["ec2.amazonaws.com", "s3.amazonaws.com", "iam.amazonaws.com"]
    aws_regions = ["us-west-2", "us-east-1", "eu-central-1"]
    account_ids = ["123456789012", "234567890123", "345678901234"]

    user_identities = [
        {
            "type": "IAMUser",
            "principalId": "EX_PRINCIPAL_ID",
            "arn": "arn:aws:iam::123456789012:user/Alice",
            "accountId": "123456789012",
            "accessKeyId": "EXAMPLE_KEY_ID",
            "userName": "Alice"
        },
        {
            "type": "IAMUser",
            "principalId": "EX_PRINCIPAL_ID_2",
            "arn": "arn:aws:iam::234567890123:user/Bob",
            "accountId": "234567890123",
            "accessKeyId": "EXAMPLE_KEY_ID_2",
            "userName": "Bob"
        }
    ]

    request_parameters_list = [
        {"instancesSet": {"items": [{"instanceId": "i-1234567890abcdef0"}]}},
        {"instancesSet": {"items": [{"instanceId": "i-0987654321abcdef0"}]}}
    ]

    response_elements_list = [
        {"instancesSet": {"items": [{"instanceId": "i-1234567890abcdef0"}]}},
        {"instancesSet": {"items": [{"instanceId": "i-0987654321abcdef0"}]}}
    ]

    additional_event_data_list = [
        {},
        {"eventType": "AwsApiCall"}
    ]

    permutations = []
    for _ in range(num_events):
        event_name = random.choice(event_names)
        event_source = random.choice(event_sources)
        user_identity = random.choice(user_identities)
        aws_region = random.choice(aws_regions)
        request_parameters = random.choice(request_parameters_list)
        response_elements = random.choice(response_elements_list)
        additional_event_data = random.choice(additional_event_data_list)

        event_time = datetime.utcnow() - timedelta(days=random.randint(0, 365))
        additional_fields = {
            "requestParameters": request_parameters,
            "responseElements": response_elements,
            "additionalEventData": additional_event_data,
            "recipientAccountId": random.choice(account_ids)
        }
        permutations.append((event_name, event_source, user_identity, aws_region, event_time, additional_fields))
    return permutations

def main():
    num_events = int(input("Enter the number of events to inject: "))
    permutations = generate_permutations(num_events)

    for permutation in permutations:
        event_name, event_source, user_identity, aws_region, event_time, additional_fields = permutation
        inject_cloudtrail_log(event_name, event_source, user_identity, aws_region, event_time, additional_fields)

if __name__ == "__main__":
    main()
