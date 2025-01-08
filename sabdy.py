

import requests
import json
import argparse
from termcolor import colored

# Make to add your SecurityTrails API key here
APIKEY = "YOUR_API_KEY_HERE"

parser = argparse.ArgumentParser(description='Retrieve subdomains from securitytrails.com')
parser.add_argument("-d", "--domain", help="Domain name", required=True)
parser.add_argument("-o", "--output", help="Save the output in file")
args = parser.parse_args()

headers = {"Accept": "application/json", "APIKEY": APIKEY}

def save(subdomain, output):
    with open(output, 'a') as txt:
        txt.write(subdomain + "\n")

def get_subdomains(domain):
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    response = requests.get(url, headers=headers)
    return json.loads(response.content)["subdomains"]

subdomains = get_subdomains(args.domain)
unique_subdomains = set(f"{sub}.{args.domain}" for sub in subdomains)

for sub in unique_subdomains:
    print(colored(f"[INFO]     ", "cyan", attrs=['bold']) + colored(sub, "green", attrs=['bold']))
    if args.output:
        save(sub, args.output)

# Print an empty line 
print()

# Print total unique subdomains
total_count = len(unique_subdomains)
print(colored(f"[INFO]     TOTAL UNIQUE SUBDOMAINS: {total_count}", "yellow", attrs=['bold']))
