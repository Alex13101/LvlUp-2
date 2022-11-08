from email_validator import validate_email, EmailNotValidError


def is_email_valid(email):
    try:
        email = validate_email(email).email
        return True
    except EmailNotValidError as e:
        return False