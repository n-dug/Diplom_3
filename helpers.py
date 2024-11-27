import random
import string


class Helpers:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_random_email(domain="gmail.com", username_prefix="dugaeva_11"):
        random_number = random.randint(0, 9999)
        login = f"{username_prefix}{random_number}"
        email = f"{login}@{domain}"
        return email

    def generate_data(self):
        email = self.generate_random_email()
        name = self.generate_random_string(10)
        password = self.generate_random_string(10)
        return email, name, password
