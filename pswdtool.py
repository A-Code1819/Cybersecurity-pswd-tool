import random
import string
import hashlib
import math

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def calculate_entropy(password):
    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += 32

    entropy = len(password) * math.log2(charset)
    return round(entropy,2)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_policy(password):

    issues = []

    if len(password) < 12:
        issues.append("Minimum 12 characters")

    if not any(c.isupper() for c in password):
        issues.append("Add uppercase letters")

    if not any(c.isdigit() for c in password):
        issues.append("Add numbers")

    if not any(c in string.punctuation for c in password):
        issues.append("Add special characters")

    return issues


def dictionary_attack(hash_target, wordlist):

    with open(wordlist,"r") as file:

        for word in file:

            word = word.strip()

            hashed = hashlib.sha256(word.encode()).hexdigest()

            if hashed == hash_target:
                return word

    return None