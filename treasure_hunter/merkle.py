from Crypto.Hash import keccak

def keccak256(data):return keccak.new(digest_bits=256,data=data).digest()
def verify_aave_claim(address,claim,root):
    leaf=keccak256(int(claim['index']).to_bytes(32,'big')+bytes.fromhex(address[2:])+int(claim['amountInWei']).to_bytes(32,'big'))
    for p in claim['proof']:
        sibling=bytes.fromhex(p.removeprefix('0x'))
        if len(sibling)!=32:return False
        leaf=keccak256(min(leaf,sibling)+max(leaf,sibling))
    return '0x'+leaf.hex()==root.lower()

def selector(signature):return keccak256(signature.encode())[:4].hex()
