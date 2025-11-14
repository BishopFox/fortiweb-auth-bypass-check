# FortiWeb Auth Bypass Check

FortiWeb auth bypass scanner by Bishop Fox

- Tests a target for authentication bypass CVE-2025-64446
- Only exploits a path traversal, does not exploit the actual auth bypass
- Does not perform any administrative actions on the target

For more information about this vulnerability, refer to the [Bishop Fox blog](https://bishopfox.com/blog).

## Setup

```sh
git clone https://github.com/BishopFox/fortiweb-auth-bypass-check
cd fortiweb-auth-bypass-check
python3 -m pip install requests
```

## Usage

```sh
python3 scan.py https://[TARGET]
```

## Examples

```sh
# Vulnerable target
$ python3 scan.py https://example1.com
[*] Testing https://example1.com
[!] Target is VULNERABLE - update immediately!

# Unaffected target
$ python3 scan.py https://example2.com
[*] Testing https://example2.com
[+] Target is not affected

# Invalid target
$ python3 scan.py https://example3.com
[*] Testing https://example3.com
[-] Target does not appear to be FortiWeb
```

## License

This code is distributed under an [MIT license](LICENSE).
