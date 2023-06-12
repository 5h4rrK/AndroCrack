import struct
import scrypt
import itertools

def crack_The_Pattern(signature, meta, salt, cost_N = 2**14, block_size = 8, parallelism=1) -> None:
    pattern = ''
    hash_val = meta
    mod = 0
    hash_val = scrypt.hash(hash_val, salt, cost_N, block_size , parallelism)
    pass_combinations = [''.join(_) for _ in itertools.product('987654310', repeat=5)]
    for i in range(0,len(pass_combinations)):
        pattern = pass_combinations[i]
        hash_val = meta
        hash_val += (pattern.encode())
        hash_val = scrypt.hash(hash_val, salt, cost_N, block_size, parallelism)
        mod += 1
        if (hash_val[0:32] == signature):
            print("Pattern ===> " + pattern)
            break
        if (mod % 1000)==0: 
            print(pattern)
            mod = 0
    


file = open('first_device/gatekeeper.pattern.key', 'rb')
s = struct.unpack('< 17s 8s 32s', file.read(57)) # Ignoring the last null byte ; If last byte is 01, not possible to crack
crack_The_Pattern(meta=s[0] , salt=s[1] , signature = s[2])   
