import requests

# List of common directories to check
common_dirs = ['admin', 'login', 'backup', 'config', 'uploads']

def check_website(url):
    try:
        response = requests.get(url)
        print(f"[INFO] {url} is up! Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"[ERROR] Could not reach {url}. Error: {e}")

def check_directories(url):
    print(f"\n[INFO] Checking common directories on {url} ...")
    for directory in common_dirs:
        full_url = url.rstrip('/') + '/' + directory
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"[FOUND] {full_url} (Status: {response.status_code})")
            else:
                print(f"[NOT FOUND] {full_url} (Status: {response.status_code})")
        except requests.RequestException as e:
            print(f"[ERROR] Could not reach {full_url}. Error: {e}")

def main():
    url = input("Enter the website URL (include http:// or https://): ").strip()
    check_website(url)
    check_directories(url)

if __name__ == "__main__":
    main()
