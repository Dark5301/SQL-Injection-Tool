import requests

def send_get_request(url, data=None, method='GET'):
    # Send GET or POST request based on method and data provided
    if method == 'POST' and data:
        response = requests.post(url, data=data)
    else:
        response = requests.get(url, params=data)
    return response.text
