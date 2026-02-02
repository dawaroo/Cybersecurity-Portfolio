# Log File Analysis (Python Automation)

## Overview
This script performs basic security log analysis by reading a log file containing login attempts and extracting IP addresses for further inspection.

The goal is to identify potential suspicious activity such as repeated login attempts from the same IP address.

## Security Relevance
Log analysis is a fundamental task in Security Operations Centers (SOC). Automating log parsing helps analysts quickly detect patterns that may indicate brute-force attacks, unauthorized access attempts, or misconfigured systems.

## What the Script Does
- Reads a log file containing login events
- Extracts IP addresses from each log entry
- Counts how many times each IP appears
- Flags IP addresses with multiple login attempts

## Skills Demonstrated
- File handling in Python
- String parsing and data extraction
- Dictionaries for counting events
- Security-focused automation logic

## Files
- `log_analysis.py` — Python script for basic log analysis

