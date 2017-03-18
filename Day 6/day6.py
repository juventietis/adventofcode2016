input_data = None
with open("input.dat", "rb") as data:
    input_data = data.readlines()

messages = [list(i) for i in zip(*input_data)]
message = []
for letter in messages:
    frequency = {}
    for repeat in letter:
        freq = frequency.get(repeat, 0)
        freq += 1
        frequency[repeat] = freq
    choices = list(frequency.items())
    choices.sort(key=lambda x: x[1], reverse=True)
    real_letter = choices[0][0]
    message.append(real_letter)

print ("".join(message))