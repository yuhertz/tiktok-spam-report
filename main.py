import requests
import threading

def report_tiktok_account(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    def send_report():
        while True:
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    print(f"Reporting @{username}... Report sent successfully.")
                else:
                    print(f"Error while reporting @{username}. Status code: {response.status_code}")
            except Exception as e:
                print(f"Error while reporting @{username}: {str(e)}")

    # Create multiple threads for lightning fast reporting
    for _ in range(10):  # Adjust the number of threads as needed
        t = threading.Thread(target=send_report)
        t.start()

if __name__ == "__main__":
    username = input("Enter the TikTok username to report: ")
    report_tiktok_account(username)
