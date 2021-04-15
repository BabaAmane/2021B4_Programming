input = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

propcessing_input = input.replace(',',' ')
propcessing_input = propcessing_input.replace('.','')
strings = propcessing_input.split()
strings_len = []

for word in strings:
    strings_len.append(len(word))

print(strings_len)