import boto3
import json
from datetime import datetime

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

def main():
    event_name = input("Enter the event name: ")
    event_source = input("Enter the event source (e.g., ec2.amazonaws.com): ")
    user_identity = {
        "type": input("Enter the user identity type (e.g., IAMUser): "),
        "principalId": input("Enter the principal ID: "),
        "arn": input("Enter the ARN: "),
        "accountId": input("Enter the account ID: "),
        "accessKeyId": input("Enter the access key ID: "),
        "userName": input("Enter the user name: ")
    }
    aws_region = input("Enter the AWS region (e.g., us-west-2): ")
    event_time = datetime.utcnow()
    additional_fields = {
        "requestParameters": json.loads(input("Enter request parameters as JSON string: ")),
        "responseElements": json.loads(input("Enter response elements as JSON string: ")),
        "additionalEventData": json.loads(input("Enter additional event data as JSON string: ")),
        "recipientAccountId": input("Enter the recipient account ID: ")
    }

    inject_cloudtrail_log(event_name, event_source, user_identity, aws_region, event_time, additional_fields)

if __name__ == "__main__":
    main()
