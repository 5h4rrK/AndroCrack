import hashlib 
import sys
import itertools

def salt_To_Hex(integer_value=8074783686056175940):
    hex_value = hex(integer_value)[2:]  
    if len(hex_value) % 2 != 0: hex_value = '0' + hex_value  
    return hex_value

GESTURE_KEY = open(f"{sys.argv[1]}","rb").read().lower()
print("Gesture Key --> ",GESTURE_KEY)
salt_password = salt_To_Hex()
print("Salt : ",salt_password)
def to_hex(data): return data.hex()

def calc_the_Hash_NoSalt(pass_int):
    sha1_hash = hashlib.sha1(pass_int).hexdigest()
    return bytes((sha1_hash ).encode())

def calc_the_Hash(pass_int, salt_hex = salt_password):
    mergedPass = ((pass_int + salt_hex)).encode()
    sha1_hash = hashlib.sha1(mergedPass).digest()
    md5_hash = hashlib.md5(mergedPass).digest()   
    return bytes((to_hex(sha1_hash) + to_hex(md5_hash)).encode())

def compare_the_Hash(calc_hash, gen_hash = GESTURE_KEY): return calc_hash == gen_hash

start = ''
count = 0
pass_combinations = open("/usr/share/wordlists/rockyou.txt","rb") 
while count < 14344391:
    try:
        start = pass_combinations.readline().decode().strip()
    except:
        count += 1
        continue
    _ = str(start)
    count += 1
    if compare_the_Hash(calc_hash=calc_the_Hash(_)):
        print('Found ==> ', _)
        break
pass_combinations.close()
