import requests
import time


def report_tiktok_account(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    while True:
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print(f"Reporting @{username}... Report sent successfully.")
            else:
                print(f"Error while reporting @{username}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error while reporting @{username}: {str(e)}")
        time.sleep(10)  # Report every 10 seconds

if __name__ == "__main__":
    username = input("Enter the TikTok username to report: ")
    report_tiktok_account(username)
