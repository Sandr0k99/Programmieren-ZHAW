first_char = 'x'
second_char = '.'
start_indexes = [0, 1, 2]
lines = []

def evaluate_line():
    line = ''
    for i in range(1, 16):
        if i in start_indexes:
            line += second_char
        else:
            line += first_char
    return line


for i in range(15):
    lines.append(evaluate_line())
    start_indexes = [x+1 for x in start_indexes]


for line in lines:
    print(line)


