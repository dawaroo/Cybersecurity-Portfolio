# File Automation Script
# This script writes and reads security-related information from a file

file_name = "security_notes.txt"

security_notes = (
    "Security Automation Notes\n"
    "-------------------------\n"
    "• Logs should be reviewed regularly\n"
    "• Allow lists must be kept up to date\n"
    "• Invalid data should not be trusted\n"
)

# Write information to file
with open(file_name, "w") as file:
    file.write(security_notes)

# Read the file to verify contents
with open(file_name, "r") as file:
    content = file.read()

# Display the file contents
print(content)

