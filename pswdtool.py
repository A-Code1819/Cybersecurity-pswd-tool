import flask # type: ignore
import hashlib
import math
import requests # type: ignore

app = flask.Flask(__name__)

def entropy(password):
    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(not c.isalnum() for c in password):
        charset += 32

    if charset == 0:
        return 0.0  # Handle case where password is empty or has no valid characters

    return round(len(password) * math.log2(charset), 2)


@app.route("/entropy", methods=["POST"])
def entropy_api():
    password = flask.request.json["password"]

    e = entropy(password)

    return flask.jsonify({"entropy": e})


@app.route("/hash", methods=["POST"])
def hash_api():
    password = flask.request.json["password"]

    h = hashlib.sha256(password.encode()).hexdigest()

    return flask.jsonify({"hash": h})


@app.route("/pwned", methods=["POST"])
def pwned():
    password = flask.request.json["password"]

    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()

    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        res = requests.get(url)
        res.raise_for_status()  # Raise an error for bad responses
        hashes = res.text.splitlines()

        for line in hashes:
            h, count = line.split(":")
            if h == suffix:
                return flask.jsonify({"breached": True, "count": count})

        return flask.jsonify({"breached": False})
    except requests.RequestException:
        return flask.jsonify({"error": "Unable to check password breach status"}), 500


app.run(host="0.0.0.0", port=5000)

#craker.py is a password cracking tool that uses a dictionary attack to guess passwords. It takes a list of common passwords and hashes them using the same algorithm as the target password, then compares the hashes to find matches. This tool can be used to test the strength of passwords and identify weak ones. 
import hashlib
import time

def dictionary_attack(hash_target, wordlist):

    with open(wordlist) as f:

        for word in f:

            word = word.strip()

            hashed = hashlib.sha256(word.encode()).hexdigest()

            print("Testing:", word)

            time.sleep(0.05)

            if hashed == hash_target:

                print("Password Found:", word)

                return word

    return None
# Example usage
if __name__ == "__main__":
    target_hash = input("Enter the SHA-256 hash of the password to crack: ")
    wordlist_file = input("Enter the path to the wordlist file: ")

    result = dictionary_attack(target_hash, wordlist_file)

    if result:
        print("Password successfully cracked:", result)
    else:
        print("Password not found in the wordlist.")
        
