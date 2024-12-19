import requests
import warnings
from urllib3.exceptions import InsecureRequestWarning
from termcolor import colored
import time
import os


warnings.filterwarnings("ignore", category=InsecureRequestWarning)


SECURITY_HEADERS = {
    "Strict-Transport-Security": "HSTS",
    "Content-Security-Policy": "CSP",
    "X-Content-Type-Options": "XCTO",
    "X-Frame-Options": "XFO",
    "X-XSS-Protection": "XXP",
    "Referrer-Policy": "RP",
    "Feature-Policy": "FP",
    "Permissions-Policy": "PP"
}

def display_banner():
    symbols = ["|", "/", "-", "\\"]
    banner_static = "Security Headers Scanner\nPowered by CiCi_Team\nVersion 1.0"

    for _ in range(10):  
        for symbol in symbols:
            os.system("cls" if os.name == "nt" else "clear")
            print(colored(f"{symbol * 50}\n{banner_static}\n{symbol * 50}", 'cyan'))
            time.sleep(0.1)

def scan_headers(url):
    try:
        response = requests.get(url, verify=False)
        headers = response.headers

        
        print("\n--- Raw Headers ---")
        for header, value in headers.items():
            print(f"{header}: {value}")

        found_headers = {}
        missing_headers = []

        for header in SECURITY_HEADERS:
            if header in headers:
                found_headers[header] = headers[header]
            else:
                missing_headers.append(header)

        print("\n--- Security Headers Təhlili ---")
        for header, description in SECURITY_HEADERS.items():
            if header in found_headers:
                print(colored(f"✔ {header}: Found ({found_headers[header]})", 'green'))
            else:
                print(colored(f"✖ {header}: Not Found", 'red'))

        print("\n---\ Nəticə /---")
        print(f"Security Headers (tapıldı): {len(found_headers)}")
        print(f"Security Headers (çatışmayan): {len(missing_headers)}")

    except requests.exceptions.RequestException as error:
        print(colored(f"An error occurred: {error}", 'yellow'))

    print("\nBəzən eyni nəticə verməyə bilər. Əlavə olaraq bu saytdan yoxlayın: https://securityheaders.com/")

if __name__ == "__main__":
    display_banner()
    target_url = input("URL daxil edin -- (e.g., https://example.com): ")
    scan_headers(target_url)
