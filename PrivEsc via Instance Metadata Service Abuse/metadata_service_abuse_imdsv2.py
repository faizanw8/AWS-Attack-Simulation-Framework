import requests

def get_token():
    """
    Retrieve a session token from the EC2 instance metadata service (IMDSv2).
    """
    try:
        print("Requesting IMDSv2 session token...")
        token_response = requests.put(
            'http://169.254.169.254/latest/api/token',
            headers={'X-aws-ec2-metadata-token-ttl-seconds': '21600'}  # Token valid for 6 hours
        )
        if token_response.status_code != 200:
            raise Exception(f"Failed to retrieve session token. HTTP Status Code: {token_response.status_code}")
        token = token_response.text
        print("Session token retrieved successfully.")
        return token
    except requests.exceptions.RequestException as e:
        print(f"HTTP request for token failed: {e}")
        return None

def get_instance_metadata_v2():
    """
    Retrieve IAM role credentials from the EC2 instance metadata service (IMDSv2).
    """
    try:
        # Get the session token
        token = get_token()
        if not token:
            raise Exception("Failed to obtain session token for IMDSv2.")

        # Fetch the IAM role name using the session token
        print("Requesting IAM role name...")
        role_name_response = requests.get(
            'http://169.254.169.254/latest/meta-data/iam/security-credentials/',
            headers={'X-aws-ec2-metadata-token': token}
        )
        if role_name_response.status_code != 200:
            raise Exception(f"Failed to retrieve IAM role name. HTTP Status Code: {role_name_response.status_code}")
        
        role_name = role_name_response.text.strip()
        if not role_name:
            raise Exception("Failed to retrieve IAM role name. No data returned.")
        
        print(f"IAM Role Name: {role_name}")
        
        # Fetch the IAM role credentials using the session token
        print("Requesting IAM role credentials...")
        role_credentials_url = f'http://169.254.169.254/latest/meta-data/iam/security-credentials/{role_name}'
        credentials_response = requests.get(
            role_credentials_url,
            headers={'X-aws-ec2-metadata-token': token}
        )
        if credentials_response.status_code != 200:
            raise Exception(f"Failed to retrieve IAM role credentials. HTTP Status Code: {credentials_response.status_code}")
        
        credentials = credentials_response.json()
        
        print(f"Retrieved IAM role credentials: {credentials}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed: {e}")
    except ValueError as e:
        print(f"Failed to parse JSON response: {e}")
    except Exception as e:
        print(f"Failed to retrieve instance metadata: {e}")

def main():
    get_instance_metadata_v2()

if __name__ == "__main__":
    main()
