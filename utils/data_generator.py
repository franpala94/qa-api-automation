import random

def generate_person_ids(n):
    return [random.randint(100, 999) for _ in range(n)]
