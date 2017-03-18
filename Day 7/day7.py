input_data = None
with open("input.dat", "rb") as data:
    input_data = data.readlines()

def is_abba(in_str):
    return in_str[0] == in_str[3] and in_str[1] == in_str[2] and in_str[0] != in_str[1]

def contains_abba(in_str):
    current_pos = 0
    found_abba = False
    while current_pos + 3 < len(in_str) and not found_abba:
        sliced = in_str[current_pos:current_pos+4]
        if is_abba(sliced):
            found_abba = True
        current_pos += 1
    return found_abba

def slice(in_str):
    start = 0
    end = 0
    slices = []
    bracket_slices = []
    for i in range(len(in_str)):
        if(in_str[i] == "["):
            slices.append(in_str[start:i])
            start = i+1
        elif(in_str[i] == "]"):
            bracket_slices.append(in_str[start:i])
            start = i+1
        elif(in_str[i] == "\n"):
            slices.append(in_str[start:len(in_str)-1])
    return slices, bracket_slices


def search_for_abba(slices):
    found_abba = False
    for i in range(len(slices)):
        if contains_abba(slices[i]):
            found_abba = True
            break
    return found_abba

count = 0
for line in input_data:
    slices, bracket_slices = slice(line)
    if not search_for_abba(bracket_slices):
        if search_for_abba(slices):
            count += 1

print (count)