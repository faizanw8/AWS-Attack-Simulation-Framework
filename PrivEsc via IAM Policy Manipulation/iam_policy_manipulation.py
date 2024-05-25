import argparse
import boto3

def add_policy_permissions(policy_arn, new_permissions):
    """
    Add new permissions to an existing IAM policy.
    
    Args:
    - policy_arn: ARN of the IAM policy to manipulate.
    - new_permissions: List of new permissions to add to the policy.
    """
    iam_client = boto3.client('iam')
    
    try:
        # Get the current policy version
        policy = iam_client.get_policy(PolicyArn=policy_arn)
        policy_version_id = policy['Policy']['DefaultVersionId']
        
        # Get the policy document
        policy_version = iam_client.get_policy_version(
            PolicyArn=policy_arn,
            VersionId=policy_version_id
        )
        policy_document = policy_version['PolicyVersion']['Document']
        
        # Add new permissions to the policy document
        if 'Statement' not in policy_document:
            policy_document['Statement'] = []
        
        policy_document['Statement'].append({
            "Effect": "Allow",
            "Action": new_permissions,
            "Resource": "*"
        })
        
        # Create a new policy version with the updated permissions
        iam_client.create_policy_version(
            PolicyArn=policy_arn,
            PolicyDocument=json.dumps(policy_document),
            SetAsDefault=True
        )
        
        print(f"Added new permissions to policy '{policy_arn}': {new_permissions}")
    except Exception as e:
        print(f"Failed to add permissions to policy: {e}")

def main():
    parser = argparse.ArgumentParser(description='IAM Policy Manipulation Script')
    parser.add_argument('--policy-arn', required=True, help='ARN of the IAM policy to manipulate')
    parser.add_argument('--permissions', required=True, nargs='+', help='New permissions to add to the policy')
    args = parser.parse_args()
    
    # Add permissions to the specified IAM policy
    add_policy_permissions(args.policy_arn, args.permissions)

if __name__ == "__main__":
    main()
