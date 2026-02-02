# Allow List Management Script

import_file = "allow_list.txt"

remove_list = [
    "192.168.97.225",
    "192.168.158.170",
    "192.168.201.40",
    "192.168.58.57"
]

# Read the allow list from file
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert string to list
ip_addresses = ip_addresses.split()

# Remove unauthorized IP addresses
for ip in ip_addresses:
    if ip in remove_list:
        ip_addresses.remove(ip)

# Convert list back to string
updated_allow_list = " ".join(ip_addresses)

# Rewrite the allow list file
with open(import_file, "w") as file:
    file.write(updated_allow_list)
