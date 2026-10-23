import sys
import requests
import argparse
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def enum(url):
    url = url.strip()
    if not urlparse(url).scheme:
        return "https://" + url
    return url

def check_url(base_url, word):
    # Strip whitespace/newlines from the wordlist entry
    word = word.strip()
    if not word:
        return None
        
    url = base_url + word
    try:
        res = requests.get(url, timeout=1)
        if res.status_code == 200:
            return url
    except requests.exceptions.Timeout:
        return (url, "Timeout")
    except requests.exceptions.ConnectionError: # Fixed: Corrected exception path
        return (url, "ConnError")
    except requests.exceptions.RequestException: # Added catch-all for other HTTP anomalies
        return (url, "ReqError")
    return None

def brute(base_url, wordlist):
    base_url = enum(base_url)
    if not base_url.endswith('/'):
        base_url += '/'

    found_urls = []

    print(r"""
██████╗  █████╗ ██████╗ ██╗  ██╗██████╗  ██████╗ ██╗   ██╗████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝██╔════╝
██║  ██║███████║██████╔╝█████╔╝ ██████╔╝██║   ██║██║   ██║   ██║   █████╗  
██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██╗██║   ██║██║   ██║   ██║   ██╔══╝  
██████╔╝██║  ██║██║  ██║██║  ██╗██║  ██║╚██████╔╝╚██████╔╝   ██║   ███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝
""")

    print(f"[*] Starting directory brute force on {base_url} with 25 workers...")
    with ThreadPoolExecutor(max_workers=25) as executor:
        futures = [executor.submit(check_url, base_url, word) for word in wordlist]
        
        for future in as_completed(futures):
            result = future.result()
            if isinstance(result, str):
                found_urls.append(result)
                print(f"[+] Found: {result}")
            elif isinstance(result, tuple): 
                print(f"[-] {result[1]} with {result[0]}")

    with open("darkroute.txt", "w") as f:
        for url in found_urls:
            f.write(url + '\n')
    print(f"[*] Run finished. Output saved to darkroute.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DarkRoute Directory Brute-Forcer")
    parser.add_argument("base_url", help="Target base URL (e.g., example.com)")
    args = parser.parse_args()

    # Read from standard input (stdin)
    wordlist = [line for line in sys.stdin if line.strip()] 
    
    if not wordlist:
        print("[-] Error: Wordlist provided via stdin is empty.")
        sys.exit(1)
        
    brute(args.base_url, wordlist)
