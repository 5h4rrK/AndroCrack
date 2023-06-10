import hashlib 
import sys
import itertools

def salt_To_Hex(integer_value=545359896771541034):
    hex_value = hex(integer_value)[2:]  
    if len(hex_value) % 2 != 0: hex_value = '0' + hex_value  
    return hex_value

GESTURE_KEY = open(f"{sys.argv[1]}","rb").read().hex()
print("Gesture Key --> ",GESTURE_KEY)
# GESTURE_KEY = b'92414b4c5a3f08da2be670918f33104e4bfb235ff1165a07f152417ec28c6a5c24effe65'
# GESTURE_KEY = b'6c1d006e3e146d4ee8af5981b8d84e1fe9e38b6c' # No Salt 
salt_password = salt_To_Hex(545359896771541034)

def to_hex(data):
    return data.hex()


def calc_the_Hash_NoSalt(pass_int):
    sha1_hash = hashlib.sha1(pass_int).hexdigest()
    return bytes((sha1_hash ).encode())

def calc_the_Hash(pass_int, salt_hex = salt_password):

    mergedPass = ((pass_int + salt_hex)).encode()
    # print('Merged Pass - ',mergedPass)

    sha1_hash = hashlib.sha1(mergedPass).digest()

    md5_hash = hashlib.md5(mergedPass).digest()
    
    return bytes((to_hex(sha1_hash) + to_hex(md5_hash)).encode())
    # return bytes((to_hex(sha1_hash)).encode())



# print(salt_password)
def compare_the_Hash(calc_hash, gen_hash = GESTURE_KEY):
    # print("Calc Hash : ",calc_hash)
    return calc_hash == gen_hash

# pass_combinations = [str(i1) + str(i2) + str(i3) + str(i4) + str(i5) for i1 in range(10) for i2 in range(10) for i3 in range(10) for i4 in range(10) for i5 in range(10)]
pass_combinations = [''.join(_) for _ in itertools.product('0123456789', repeat=5)]

for _ in pass_combinations:
    if(compare_the_Hash(calc_hash=calc_the_Hash(_))): 
        print('Found ==> ', _)
        break

# for _ in pass_combinations:
#     if(compare_the_Hash(calc_hash=calc_the_Hash_NoSalt(_.encode()))): 
#         print('Found ==> ', _)
#         break


