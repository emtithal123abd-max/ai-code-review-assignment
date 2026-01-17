# corrected implementation for Task 2.
def count_valid_emails(emails):
    count = 0
    if not emails:
        return 0 

    for email in emails:
        if not isinstance(email, str):
            continue
        email = email.strip()
        if email.count("@") != 1:
            continue
        if " " in email :
            continue 
        username, host = email.split("@")
        if not username or not host :
            continue 
        if "." not in host or host.startswith(".") or host.endswith("."):
            continue

        count += 1  

    return count
