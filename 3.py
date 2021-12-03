with open('3.input') as file:
  lines = file.readlines()
  lines = [line.rstrip() for line in lines]

lines_second = lines[:]
gamma_rate = ''
beginning = ''

for i in range(len(lines[0])):
    ones = 0
    for line in lines:
        if(line[i] == '1'):
            ones += 1
        else:
            ones -= 1

    # There are more ones than zeros in column
    if(ones > 0):
        gamma_rate += '1'
    # There are more zeros than ones in column
    elif(ones < 0):
        gamma_rate += '0'

    
max_value = 2 ** ( len(gamma_rate) ) - 1
gamma_rate = int(gamma_rate, 2)
epsilon_rate = max_value - gamma_rate

print("Part one:", gamma_rate * epsilon_rate)


first_round = True
rating1 = rating2 = 0
for i in range(2):
    beginning = ''
    column = 0
    while(True):
        ones = 0
        for line in lines_second:
            if(line[column] == '1'):
                ones += 1
            else:
                ones -= 1
        column += 1

        if(ones >= 0):
            if(first_round):
                beginning += '1'
            else:
                beginning += '0'
        elif(ones < 0):
            if(first_round):
                beginning += '0'
            else:
                beginning += '1'

        i = 0
        while(i < len(lines_second)):
            if(lines_second[i].startswith(beginning) == False):
                lines_second.pop(i)
                i -= 1
            i += 1

        if(len(lines_second) == 1):
            break

    if(first_round):
        rating1 = int(lines_second[0], 2)
    else:
        rating2 = int(lines_second[0], 2)

    first_round = False
    lines_second = lines[:]

print("Part two:", rating1 * rating2)



