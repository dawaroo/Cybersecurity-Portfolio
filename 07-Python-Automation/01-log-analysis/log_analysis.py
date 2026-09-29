# Log Analysis Script
# Extracts IP addresses from a login log file, validates them, and flags
# IPs with repeated failed login attempts (possible brute-force activity).
#
# Based on a lab from the Google Cybersecurity Professional Certificate,
# extended with IP validation and brute-force detection.

import ipaddress

log_file = "login.txt"

# Number of failed attempts from one IP that is considered suspicious
failed_threshold = 3

valid_ips = []
invalid_ips = []
failed_attempts = {}

# Read the log file line by line
with open(log_file, "r") as file:
    for line in file:
        # Turn "key=value" pairs into a dictionary, e.g. {"ip": "10.0.0.5", "status": "failed"}
        fields = {}
        for word in line.split():
            if "=" in word:
                key, value = word.split("=", 1)
                fields[key] = value

        # Skip lines that don't record a login (e.g. system messages)
        if "ip" not in fields:
            continue

        ip = fields["ip"]

        # Check that the IP is real (each of the 4 numbers must be 0-255)
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            invalid_ips.append(ip)
            continue

        valid_ips.append(ip)

        # Count failed login attempts per IP
        if fields.get("status") == "failed":
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

# Display extracted IP addresses (each IP shown once)
print("Extracted IP addresses:")
for ip in sorted(set(valid_ips)):
    print(f"  {ip}")

print("\nInvalid IP addresses (possible log tampering or parsing errors):")
for ip in invalid_ips:
    print(f"  {ip}")

print("\nFailed login attempts per IP:")
for ip, count in failed_attempts.items():
    print(f"  {ip}: {count}")

print(f"\nSuspicious IPs ({failed_threshold}+ failed attempts, possible brute force):")
for ip, count in failed_attempts.items():
    if count >= failed_threshold:
        print(f"  [ALERT] {ip} - {count} failed attempts")
