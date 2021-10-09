from examples import get_tron

acc = get_tron().create_account

print("private key", acc.private_key)
print("address", acc.address.base58)
