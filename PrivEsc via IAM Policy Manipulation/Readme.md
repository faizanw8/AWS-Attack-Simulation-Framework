PrivEsc Via IAM Policy Manipulatuion:


#### This script makes use of the following modules:

1. argparse: For parsing command-line arguments.
2. boto3: The AWS SDK for Python to interact with AWS services.
3. json: For handling JSON data.

This script makes use of the following schema:

#### add_policy_permissions Function:

##### Parameters:
1. policy_arn: The ARN of the IAM policy to be manipulated.
2. new_permissions: A list of new permissions to add to the policy.

##### Logic:
1. Retrieve the current policy version.
2. Retrieve the policy document.
3. Add new permissions to the policy document.
4. Create a new policy version with the updated permissions and set it as the default version.


#### Example Usage

`python iam_policy_manipulation.py --policy-arn arn:aws:iam::123456789012:policy/ExamplePolicy --permissions s3:ListBucket s3:GetObject`

Replace arn:aws:iam::123456789012:policy/ExamplePolicy with the actual policy ARN and specify the permissions you want to add.