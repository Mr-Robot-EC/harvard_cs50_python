import re
# docs.python.org/3/library/re.html
# 8.44

email = input("Enter your email: ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

# 2
"""
if username and "." in domain:
    print("Valid")
else:
    print("Invalid")
"""

# 1
"""
if "@" in email and "." in email:
    at_symbol = True
else:
    at_symbol = False
"""