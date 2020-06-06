"""74. Write a Python program to hash a word."""
#hashlib — Secure hashes and message digests
import hashlib
import uuid
print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

def hash_a_word(word):   
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + word.encode()).hexdigest() + ':' + salt

print(hash_a_word('love'))
print(hash_a_word('time'))