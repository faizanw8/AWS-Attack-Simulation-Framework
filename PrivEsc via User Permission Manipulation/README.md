# AWS-Attack-Framework


Deployment Steps:
Make sure you have set up your AWS environment, configured the AWS CLI, and have the necessary IAM user credentials with appropriate permissions.

Modify privilege_escalation_scenario.json with the target AWS account ID and the IAM user or role to escalate privileges for.
Run aws_attack_simulation_framework.py script to execute the privilege escalation attack scenario.

The script will manipulate the IAM policy for the specified user or role, simulating the privilege escalation attack within the AWS environment.

Please ensure to review and test these scripts thoroughly in a controlled environment before using them in production or against any real AWS resources. Additionally, always follow AWS security best practices and guidelines when manipulating IAM policies or any other AWS resources.



#SCRIPT_WORK

The scripts provided should work as intended given that:

AWS Credentials: You have configured the AWS CLI with appropriate credentials that have permissions to manipulate IAM policies and other required AWS services.

Python Environment: You have Python installed on your system, and the necessary Python packages (such as boto3) are installed. You can install boto3 using pip: pip install boto3.

IAM Policy and Resource Names: The scripts assume the existence of an IAM policy named "ExamplePolicy" attached to the target user. Make sure that such a policy exists in your AWS account. Additionally, ensure that the target user specified in privilege_escalation_scenario.json exists and is accessible by the IAM credentials you are using.

File Paths: The file paths used in the scripts (privilege_escalation_scenario.json, privilege_escalation_attack.py, and aws_attack_simulation_framework.py) are relative to the current working directory. Ensure that the scripts are located in the correct directory, or modify the file paths accordingly.

Network Connectivity: Ensure that your system has network connectivity to communicate with AWS services. This is necessary for the Boto3 SDK to make API calls to AWS.

Error Handling: The provided scripts do not include extensive error handling. It's a good practice to implement error handling to gracefully handle exceptions and errors that may occur during script execution.

Testing and Validation: Before running the scripts in a production environment or against real AWS resources, it's essential to thoroughly test and validate them in a controlled environment. This helps ensure that the scripts behave as expected and do not cause any unintended consequences.