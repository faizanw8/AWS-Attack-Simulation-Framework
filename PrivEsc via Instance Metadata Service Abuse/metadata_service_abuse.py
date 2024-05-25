import requests

def get_instance_metadata():
    """
    Retrieve IAM role credentials from the EC2 instance metadata service.
    """
    try:
        # Fetch the IAM role name
        role_name = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
        
        # Fetch the IAM role credentials
        role_credentials_url = f'http://169.254.169.254/latest/meta-data/iam/security-credentials/{role_name}'
        credentials = requests.get(role_credentials_url).json()
        
        print(f"Retrieved IAM role credentials: {credentials}")
    except Exception as e:
        print(f"Failed to retrieve instance metadata: {e}")

def main():
    get_instance_metadata()

if __name__ == "__main__":
    main()
