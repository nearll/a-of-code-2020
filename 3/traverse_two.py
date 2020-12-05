class Traverse:

    def traverse(across, down, inputs):
        location = 1 
        trees = 0
        level_number = 0
        for level in inputs:
            line = level[0]
            if level_number % down != 0:
                level_number += 1
                continue
            if location > 31:
                location = location - 31
            if line[location - 1] == '#':
                trees += 1
            location += across
            level_number += 1 
        return trees

    if __name__ == "__main__":
        inputs = []
        with open('input.txt', 'r') as input:
            for path in input:
                inputs.append(path.rsplit())
        first = traverse(1, 1, inputs)
        second = traverse(3, 1, inputs)
        third = traverse(5, 1, inputs)
        fourth = traverse(7, 1, inputs)
        fifth = traverse(1, 2, inputs)
        print('Traversal found the following number of trees:')
        print(first)
        print(second)
        print(third)
        print(fourth)
        print(fifth)
        print('The answer you seek is ' + 
          str(first * second * third * fourth* fifth))
