import requests
from bs4 import BeautifulSoup
import re
import time
from get_request_module import send_get_request  # Import get_request_module

# Updated payload list with advanced SQL injection payloads
with open('payloads.txt', 'r') as file:
    payload_list=file.readlines()
    paload_list=[payload.strip() for payload in payload_list]
#with open('payloads.txt', 'r') as file:
    #payload_list=file.readlines()
    #payload_list=[payload.strip() for payload in payload_list]

# Website URL and form setup
url = input("Enter the URL of the website: ")
html_content = send_get_request(url)
soup = BeautifulSoup(html_content, 'html.parser')
form = soup.find('form')
if not form:
    print("No form found on the page.")
    exit()

input_fields = form.find_all(['input', 'textarea'])
field_names = [field.get('name') for field in input_fields if field.get('name')]

print("Found input fields:", field_names)

# Define regex patterns for detecting SQL errors
error_patterns = [
    re.compile(r'syntax.*mysql', re.IGNORECASE),
    re.compile(r'unclosed quotation mark', re.IGNORECASE),
    re.compile(r'syntax.*postgresql', re.IGNORECASE),
    re.compile(r'ORA-\d+', re.IGNORECASE)
]

# Function to analyze response for SQL errors
def is_vulnerable(response):
    for pattern in error_patterns:
        if pattern.search(response.text):
            return True
    return False

# Attempt payloads and check for vulnerabilities
for payload in payload_list:
    for field_name in field_names:
        data = {field: "test" for field in field_names}
        data[field_name] = payload

        start_time = time.time()
        response = requests.post(url, data=data)
        end_time = time.time()
        
        # Debugging output for each attempt
        print(f"Testing payload: {payload} in field: {field_name}")
        print(f"Status Code: {response.status_code}")
        #print("Response snippet:", response.text[:200])  # First 200 chars of response
        

        # Check for error-based vulnerability
        if is_vulnerable(response):
            print(f"Vulnerable to SQL Injection! Payload: {payload} caused a SQL error.")
        
        # Check for time-based vulnerability (significant delay in response)
        elif end_time - start_time > 5:
            print(f"Potential time-based SQL Injection vulnerability! Payload: {payload}")

        else:
            print(f"Payload: {payload} - No vulnerability detected.")
