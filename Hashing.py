import ecdsa
import hashlib

# Generate a private key
sk = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)

# Serialize the private key
private_key = sk.to_string()

# Get the public key
vk = sk.get_verifying_key()

# Serialize the public key
public_key = vk.to_string()

# Sign the message
message = b"Hello, World!"
hash_message = hashlib.sha256()
hash_message.update(message)

hex_hash = hash_message.hexdigest()

signature = sk.sign(message)
signer = private_key

 #Verify the signature
vk.verify(signature, message)

print(public_key)
print(signer)
print (signature)
