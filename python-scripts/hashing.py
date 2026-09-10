# hashing_demo.py
# Hashing: one-way function. Same input -> same output.

import hashlib

# SHA-256 on one password

password = "monkey100?"                      # fake password
# hashlib needs bytes, not str. tandard rule for turning text characters into bytes
data = password.encode("utf-8")           
digest = hashlib.md5(data).hexdigest()

print(f"Password: {password}")
print(f"Hash:  {digest}") # 256 bits

print()

same_passwords = ["monkey100?", "monkey100?", "monkey100?", "monkey100?",] 

for p in same_passwords: 
    data = p.encode("utf-8") #converts plaintext to raw bytes        
    # Try different algos by replacing sha256() with md5, sha512 on many passwords 
    digest = hashlib.sha256(data).hexdigest() #hexdigest makes the stored hash human-readable
    print(f"Password: {p}")
    print(f"Hash:  {digest}", "\n") # 256 bits
    

print() 
# note that monkey100? is the same hash as before 
diff_passwords = ["monkey100?", "donkey4u!", "doggiewoggie2", "a"]

for p in diff_passwords: 
    data = p.encode("utf-8") #converts plaintext to raw bytes        
    # Try different algos by replacing sha256() with md5, sha512 on many passwords 
    digest = hashlib.sha256(data).hexdigest() #hexdigest makes the stored hash human-readable
    print(f"Password: {p}")
    print(f"Hash:  {digest}", "\n") # 256 bits

