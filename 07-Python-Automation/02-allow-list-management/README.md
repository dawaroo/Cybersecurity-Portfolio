# Allow List Management (Python Automation)

## Overview
This project automates the management of an IP allow list used to control access to restricted systems.

The script reads an existing allow list from a file, removes IP addresses that are no longer authorized, and rewrites the updated allow list back to the file.

## Security Relevance
Allow lists are commonly used in security controls such as firewalls, access control mechanisms, and network security policies. Automating allow list updates helps reduce human error and maintain consistent access rules.

## What the Script Does
- Reads an allow list from a text file
- Converts the data into a list of IP addresses
- Removes IP addresses that should no longer be authorized
- Writes the updated allow list back to the file

## Skills Demonstrated
- File handling in Python
- String and list manipulation
- Conditional logic
- Basic security automation

## Files
- `allow_list_manager.py` — Script for updating an IP allow list
