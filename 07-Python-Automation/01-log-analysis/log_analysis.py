# Log Analysis Script
# This script extracts IP addresses from a login log file

log_file = "login.txt"

# Read the log file
with open(log_file, "r") as file:
    log_data = file.read()

# Split log data into individual elements
log_entries = log_data.split()

ip_addresses = []

# Identify and extract IP addresses
for entry in log_entries:
    if entry.count(".") == 3:
        ip_addresses.append(entry)

# Display extracted IP addresses
print("Extracted IP addresses:\n")

for ip in ip_addresses:
    print(ip)
