import re

def email_separation(email):
    RE_EMAIL = re.compile(r'(?P<username>[\w]+)@(?P<domain>[^%]+\.\w+)', re.IGNORECASE)
    if not RE_EMAIL.match(email):
        raise ValueError(f'incorrect email: {email}')
    print(RE_EMAIL.match(email).groupdict())

for i in ['someone@geekbrains.ru', 'someone@geekbrainsru']:
    try:
        email_separation(i)
    except ValueError as err:
        print(err)