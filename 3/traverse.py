inputs = []
with open('input.txt', 'r') as input:
    for path in input:
        inputs.append(path.rsplit())

location = 1
trees = 0

for levels in inputs:
    line = levels[0]
    line_width = len(levels[0])
    if location == 1:
        location += 3
        continue
    elif location > line_width:
        location = location - 31
    if line[location-1] == '#':
        trees += 1
    location += 3
            

print('You encountered ' + str(trees) + ' trees')
