inputs = []
with open('input.txt', 'r') as input:
    for number in input:
        inputs.append(int(number.rsplit()[0]))


for first_value in inputs:
    if first_value < 2020:
        for second_value in inputs:
            if second_value < 2020:
                for third_value in inputs:
                    if first_value + second_value + third_value == 2020:
                        print('Your value is: ')
                        print (first_value * second_value * third_value)
                        exit(0) 
