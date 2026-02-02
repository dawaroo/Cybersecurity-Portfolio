# Allow List Management (Python Automation)

## Overview
This script automates the management of an IP allow list used to control access to restricted resources.

It reads an existing allow list from a text file, removes IP addresses that are no longer authorized, and rewrites the updated allow list back to the file.

## Security Relevance
Allow lists are commonly used in security controls such as firewalls, access control systems, and network segmentation. Automating allow list updates helps reduce human error and ensures access policies remain up to date.

## Skills Demonstrated
- File handling in Python (`read`, `write`)
- String and list manipulation
- Conditional logic
- Basic automation for security operations

## Files
- `allow_list_manager.py` — Python script that performs allow list updates
