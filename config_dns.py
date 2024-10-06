#!/usr/bin/env python3
import os, requests
from dotenv import load_dotenv
from cloudflare import Cloudflare

load_dotenv()

# Set variables needed to call cloudflare
api_token = os.getenv('CLOUDFLARE_API_TOKEN')
zone_id = os.getenv('CLOUDFLARE_ZONE_ID')
dns_record_id = os.getenv('CLOUDFLARE_DNS_RECORD_ID')

response = requests.get('https://api.ipify.org?format=json')
public_ip = response.json().get('ip')
print(f'Your public IP address is: {public_ip}')

client = Cloudflare(api_token=api_token)

dns_record = client.dns.records.get(dns_record_id=dns_record_id, zone_id=zone_id)
record_ip = dns_record.json().get('content')

if public_ip != record_ip:
    client.dns.records.edit(
        dns_record_id=dns_record_id,
        zone_id=zone_id,
        type="A"
    )