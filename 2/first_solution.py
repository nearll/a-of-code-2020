valid_count = 0
inputs = []
with open('input.txt', 'r') as input:
    for pw in input:
        inputs.append(pw.rsplit())

for value in inputs:
    first_location = int(value[0].split('-')[0]) - 1
    second_location = int(value[0].split('-')[1]) - 1
    pw_char = value[1].split(':')[0]
    pw = value[2]
    if ((pw[first_location] == pw_char and 
        pw[second_location] !=  pw_char) or 
        (pw[first_location] != pw_char and 
        pw[second_location] == pw_char)):

            valid_count += 1

print('You found ' + str(valid_count) + ' valid passwords.')

