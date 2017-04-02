import hashlib


input_data = None
with open("input.dat", "rb") as data:
    input_data = data.read()


def hack1(input_data):
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


def hack2(input_data):
    def valid_location(n):
        valid = True
        try:
            n = int(n)
            if n < 0 or n > 7:
                valid = False
        except ValueError:
            valid = False
        return valid

    character = 0
    condition = True
    index = 0
    password_dict = {}
    while condition:
        data = input_data + str(index).encode()
        hash_builder = hashlib.md5()
        hash_builder.update(data)
        hashed = hash_builder.hexdigest()
        index += 1
        if hashed[0:5] == '00000':
            loc = hashed[5]
            if valid_location(loc):
                already_filled = True if password_dict.get(int(loc)) else False
                if not already_filled:
                    password_dict[int(loc)] = hashed[6]
                    character += 1
                    print (password_dict)
            if character == 8:
                condition = False


password = hack2(input_data)
print(password)