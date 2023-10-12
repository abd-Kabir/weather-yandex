import hashlib
import time

# Your login and password
login = "umarov-kk"
password = "Kabir1230"
timestamp = str(int(time.time()))


md5_hash = hashlib.md5(password.encode()).hexdigest()

combined_str = f"{md5_hash}:{timestamp}"

sha1_hash = hashlib.sha1(combined_str.encode()).hexdigest()


print("SHA-1 Hash:", sha1_hash)

print("RESULT: ", login + ":" + sha1_hash + ":" + timestamp)
