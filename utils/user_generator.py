import time


def generate_user():
    timestamp = str(time.time()).replace('.', '')
    return {
        "email": f"{timestamp}@hungry.ru",
        "password": f"Aa{timestamp}!",
        "name": f"User{timestamp}"
    }
