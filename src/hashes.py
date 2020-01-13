import time
import hashlib

n = 100000
key = b'Type'

for _ in range(10):
    print(int(hashlib.sha256(key).hexdigest(), 16) % 8)