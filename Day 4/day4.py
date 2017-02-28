import re
import itertools

input_data = None
with open("input.dat") as data:
    input_data = data.readlines()


def shift_letter(letter, number):
    if letter == "-":
        return " "
    else:
        current_num = ord(letter) - 97
        new_num = (current_num + number) % 26 + 97
        return chr(new_num)

regexp = re.compile(r"^(?P<name>[a-z\-]+)\-(?P<sector>\d+)\[(?P<checksum>\w+)\]$")

sectors_sum = 0
for line in input_data:
    matched = regexp.match(line)
    name, sector, checksum = matched.groups()
    name_wo_dashes = name.replace("-", "")
    letters = {}
    for letter in name_wo_dashes:
        num = letters.get(letter, 0)
        letters[letter] = num + 1
    sorted_letters = list(sorted(list(letters.items()), key=lambda pair: pair[1], reverse=True))
    grouped = itertools.groupby(sorted_letters, key=lambda pair: pair[1])
    checksum_letters = []

    for count, grouped_letters in itertools.islice(grouped, 5):
        letter_count = len(checksum_letters)
        group = list(grouped_letters)
        group_sorted = [l[0] for l in sorted(group, key=lambda pair: pair[0])]
        checksum_letters.extend(group_sorted[:5-letter_count])
    calculated_checksum = "".join(checksum_letters)
    if calculated_checksum == checksum:
        sectors_sum += int(sector)
        decoded_name = "".join([shift_letter(letter, int(sector)) for letter in name])
        if decoded_name.find("north") >= 0:
            print(decoded_name, sector)
print (sectors_sum)