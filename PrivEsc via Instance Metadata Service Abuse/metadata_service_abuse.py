import requests

def get_instance_metadata():
    """
    Retrieve IAM role credentials from the EC2 instance metadata service.
    """
    try:
        # Fetch the IAM role name
        role_name_response = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/')
        if role_name_response.status_code != 200:
            raise Exception(f"Failed to retrieve IAM role name. HTTP Status Code: {role_name_response.status_code}")
        
        role_name = role_name_response.text.strip()
        if not role_name:
            raise Exception("Failed to retrieve IAM role name. No data returned.")
        
        print(f"IAM Role Name: {role_name}")
        
        # Fetch the IAM role credentials
        role_credentials_url = f'http://169.254.169.254/latest/meta-data/iam/security-credentials/{role_name}'
        credentials_response = requests.get(role_credentials_url)
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
    get_instance_metadata()

if __name__ == "__main__":
    main()


##Error Handling Imporoved