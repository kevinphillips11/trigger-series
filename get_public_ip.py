import requests

def get_public_ip():
    try:
        # Use httpbin to get public IP
        response = requests.get("https://httpbin.org/ip")
        data = response.json()
        
        # Extract and print the public IP
        public_ip = data.get("origin", "Unable to retrieve public IP")
        print("Your public IP address is:", public_ip)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    get_public_ip()
