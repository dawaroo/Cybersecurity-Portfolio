# IP Validation Script
# This script checks whether IP addresses follow a basic IPv4 format

ip_addresses = [
    "192.168.1.10",
    "10.0.0.5",
    "256.168.1.1",
    "192.168.1",
    "abc.def.ghi.jkl"
]

valid_ips = []
invalid_ips = []

for ip in ip_addresses:
    parts = ip.split(".")

    # Check if IP has four parts
    if len(parts) != 4:
        invalid_ips.append(ip)
        continue

    is_valid = True

    for part in parts:
        if not part.isdigit():
            is_valid = False
        elif int(part) < 0 or int(part) > 255:
            is_valid = False

    if is_valid:
        valid_ips.append(ip)
    else:
        invalid_ips.append(ip)

# Display results
print("Valid IP addresses:\n")
for ip in valid_ips:
    print(ip)

print("\nInvalid IP addresses:\n")
for ip in invalid_ips:
    print(ip)
