import random
import datetime
import re

class UserUtil:
    @staticmethod
    def generate_user_id():
        year_prefix = str(datetime.date.today().year)[2:]
        random_digits = ''.join(random.choices("0123456789", k=7))
        return int(year_prefix + random_digits)

    @staticmethod
    def generate_password():
        while True:
            password = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*", k=8))
            if UserUtil.is_strong_password(password):
                return password

    @staticmethod
    def is_strong_password(password):
        return bool(re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password))

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        return bool(re.match(r'^[a-z]+\.[a-z]+@[a-z]+\.[a-z]+$', email))


