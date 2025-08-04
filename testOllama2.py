import requests
import json
from urlparse import urlparse

def test_ollama_connection(api_url, timeout=5):
    try:
        # Parse the URL to extract host and path
        parsed_url = urlparse(api_url)
        
        # Define the full URL for the API endpoint
        url = api_url + "api/generate"  # Ensure trailing slash is present
        
        # Prepare the request payload
        data = {
            "model": "llama3.2",  # Set the model type to llama3.2
            "prompt": "Hello! How can I assist you today?",
            "max_length": 50,
            "temperature": 1.0,
            "stream": False
        }
        
        headers = {
            "Content-Type": "application/json"
        }

        # Send a POST request
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=timeout)

        # Print the full request details for debugging
        print("Request URL:", url)
        print("Headers:", headers)
        print("Payload:", data)
        
        if response.status_code == 200:
            response_text = response.text
            data = json.loads(response_text)
            actual_response = data["response"]
            print("Ollama server at %s is responding successfully." % api_url)
            print(actual_response)
        else:
            print("Ollama server at %s responded with status code: %d" % (api_url, response.status_code))
            print("Error:", response.text)

    except Exception as e:
        # Handle any errors that occurred during the request
        print("Request failed: %s" % e)

if __name__ == "__main__":
    ollama_server_url = "http://192.168.1.22:11434/"  # Example IP and port

    test_ollama_connection(ollama_server_url)
