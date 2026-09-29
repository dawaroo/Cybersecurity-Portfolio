# Log Analysis (Python Automation)

## Overview
This project analyzes a login log file to extract IP addresses, validate them, and flag IPs with repeated failed login attempts that may indicate a brute-force attack.

## Security Relevance
Log analysis is a fundamental task in cybersecurity. Counting failed logins per source IP is one of the most common ways SOC analysts detect brute-force and password-guessing attacks. Validating IPs also helps spot malformed or tampered log entries.

## What the Script Does
- Reads a log file line by line and parses its `key=value` fields
- Extracts the source IP address of each login attempt
- Validates each IP with Python's `ipaddress` module (e.g. rejects `999.168.1.10`)
- Counts failed login attempts per IP
- Flags IPs that reach a configurable failure threshold as suspicious

## Example Output
Running the script against the included `login.txt`:

```
Extracted IP addresses:
  10.0.0.55
  192.168.1.10
  192.168.1.23
  203.0.113.45

Invalid IP addresses (possible log tampering or parsing errors):
  999.168.1.10

Failed login attempts per IP:
  203.0.113.45: 5
  10.0.0.55: 1

Suspicious IPs (3+ failed attempts, possible brute force):
  [ALERT] 203.0.113.45 - 5 failed attempts
```

## How to Run
```bash
python3 log_analysis.py
```

## Skills Demonstrated
- Reading and parsing files with Python
- String manipulation and dictionaries
- Input validation with the `ipaddress` module
- Brute-force detection logic for security monitoring

## Files
- `log_analysis.py` — Script that extracts, validates, and analyzes IP addresses
- `login.txt` — Sample login log (fictional data) for testing

## Lab Context
Based on a lab from the **Google Cybersecurity Professional Certificate**, extended with IP validation and brute-force detection.
