import re
import itertools

input_data = None
with open("test.dat") as data:
    input_data = data.readlines()

regexp = re.compile(r"^(?P<name>[a-z\-]+)\-(?P<sector>\d+)\[(?P<checksum>\w+)\]$")

for line in input_data:
    matched = regexp.match(line)
    name, sector, checksum = matched.groups()
    name_wo_dashes = name.replace("-", "")
    letters = {}
    for letter in name_wo_dashes:
        num = letters.get(letter, 0)
        letters[letter] = num + 1
    print(name, sector, checksum)
    print(letters)
    sorted_letters = sorted(letters.items(), key=lambda pair: pair[1], reverse=True)
    print(sorted_letters)
    grouped = list(itertools.groupby(sorted_letters, key=lambda pair: pair[1]))
    letter_count = 0
    checksum_letters = []
    print([list(group) for count, group in grouped])
    for count, grouped_letters in grouped[:5]:
        group = list(grouped_letters)
        print(count)
        print(group)
        if len(group) > 5 - letter_count:
            group_sorted = sorted(group, key=lambda pair: pair[0])
            checksum_letters.extend(group_sorted[:5-letter_count])
        else:
            checksum_letters.extend(group)
    print ("Checksum letters: {0}".format(checksum_letters))
    calculated_checksum = "".join([letter for letter, count in sorted_letters[0:5]])
    print (calculated_checksum)

