# salting_demo.py
# Salt: random bytes added to a password before hashing.
# Same password + different salt -> different hash.

import hashlib
import os

plaintext_password = "monkey100?"
password = plaintext_password.encode("utf-8") # pw converted into bytes

#1 no salt: two users, same password -> identical hashes (easy to spot/crack)
hash_a = hashlib.sha256(password).hexdigest()
hash_b = hashlib.sha256(password).hexdigest()

print("No salt:")
print(f"  User A: {hash_a}")
print(f"  User B: {hash_b}")

# 2 With salt: each user gets their own random salt -> different hashes
salt_a = os.urandom(16) # 16 random bytes from operating system, unreadable
salt_b = os.urandom(16)

salt_a_hex = salt_a.hex() # hex() just makes it human-readable
salt_b_hex = salt_b.hex()

# apply cryptography function:
salt_hash_a = hashlib.sha256(salt_a + password).hexdigest() #hexdigest() makes it human-readable
salt_hash_b = hashlib.sha256(salt_b + password).hexdigest()

print("\nWith salt:")
print(f"  User A salt: {salt_a_hex}")
print(f"  User A hash: {salt_hash_a}")
print(f"  User B salt: {salt_b_hex}")
print(f"  User B hash: {salt_hash_b}")

# 3. Login check: each user's salt + hash is stored, then reused to verify
database = {
    "user_a": {"salt": salt_a, "hash": salt_hash_a},
    "user_b": {"salt": salt_b, "hash": salt_hash_b},
}

logins = [("user_a", "monkey100?"), ("user_b", "monkey100?")]   # different users, same pw

print("\nLogin attempts:")
for username, attempt in logins:
    stored_salt = database[username]["salt"]
    stored_hash = database[username]["hash"]
    stored_salt_hex = stored_salt.hex()

    attempt_bytes = attempt.encode("utf-8")
    attempt_hash = hashlib.sha256(stored_salt + attempt_bytes).hexdigest()

    print(f"\n  {username}")
    print(f"    Password:     {attempt}")
    print(f"    Salt:         {stored_salt_hex}")
    print(f"    Stored hash:  {stored_hash}")
    print(f"    Attempt hash: {attempt_hash}")

    if attempt_hash == stored_hash:
        print("    -> Login successful")
    else:
        print("    -> Login failed")