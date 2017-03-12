import hashlib


input_data = None
with open("input.dat", "rb") as data:
    input_data = data.read()

character = 0
password = ""
condition = True
index = 0
while condition:
    data = input_data + str(index).encode()
    hash_builder = hashlib.md5()
    hash_builder.update(data)
    hashed = hash_builder.hexdigest()
    index += 1
    if hashed[0:5] == '00000':
        password += hashed[5]
        character += 1
        if character == 8:
            condition = False

print(password)