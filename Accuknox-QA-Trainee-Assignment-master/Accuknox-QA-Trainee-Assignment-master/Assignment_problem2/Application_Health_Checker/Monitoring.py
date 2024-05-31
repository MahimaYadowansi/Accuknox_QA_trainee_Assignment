import time
import requests

url = "http://127.0.0.1:5000/health"

def check_server():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("up")
        else:
            print("down")
    except requests.exceptions.RequestException:
        print("down")

if __name__ == '__main__':
    while True:
        check_server()
        time.sleep(2)