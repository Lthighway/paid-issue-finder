import base64
import binascii
import hashlib
import re

B58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def base58decode(s):
    n = 0
    for c in s:
        n = n * 58 + B58.index(c)
    return b'\0' * (len(s) - len(s.lstrip('1'))) + n.to_bytes((n.bit_length()+7)//8, 'big')

def bitcoin_valid(a):
    if a.startswith(('1','3')):
        b = base58decode(a)
        return len(b)==25 and b[0] in (0,5) and hashlib.sha256(hashlib.sha256(b[:-4]).digest()).digest()[:4]==b[-4:]
    if a.lower()!=a and a.upper()!=a:
        return False
    a=a.lower()
    if not a.startswith('bc1') or not 14<=len(a)<=90:
        return False
    alphabet='qpzry9x8gf2tvdw0s3jn54khce6mua7l'
    v=[alphabet.index(c) for c in a[3:]]
    chk=1
    for d in [3,3,0,2,3]+v:
        top=chk>>25
        chk=((chk&0x1ffffff)<<5)^d
        for i,g in enumerate([0x3b6a57b2,0x26508e6d,0x1ea119fa,0x3d4233dd,0x2a1462b3]):
            if (top>>i)&1: chk^=g
    if not v or v[0]>16 or chk!=(1 if v[0]==0 else 0x2bc830a3):return False
    acc=bits=0; decoded=[]
    for d in v[1:-6]:
        acc=(acc<<5)|d; bits+=5
        while bits>=8:
            bits-=8; decoded.append((acc>>bits)&255)
    return bits<5 and not ((acc<<(8-bits))&255) and 2<=len(decoded)<=40 and (v[0]!=0 or len(decoded) in (20,32))

def validate(network,address):
    try:
        if network=='bitcoin':ok=bitcoin_valid(address)
        elif network=='evm':ok=bool(re.fullmatch(r'0x[0-9a-fA-F]{40}',address))
        elif network=='solana':ok=len(base58decode(address))==32
        elif network=='stellar':
            b=base64.b32decode(address)
            ok=len(b)==35 and b[0]==48 and binascii.crc_hqx(b[:-2],0).to_bytes(2,'little')==b[-2:]
        else:return False,'Rede desconhecida'
        return ok, 'Formato válido' if ok else 'Endereço inválido: formato/comprimento/checksum; não consultado'
    except (ValueError,binascii.Error):return False,'Endereço inválido: caracteres/checksum'
