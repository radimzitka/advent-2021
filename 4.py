with open('inputs/4.input') as file:
  lines = [line.rstrip().split(' ') for line in file.readlines()]

def is_row_winner(winner_numbers, board_line):
    for number in board_line:
        if(number not in winner_numbers):
            return False
    return True

def sum_no_winners_numbers(winner_numbers, board):
    numbers = []
    sum = 0
    [[numbers.append(number) for number in row] for row in board]
    for number in numbers:
        if(number not in winner_numbers):
            sum += int(number)
    
    return sum


boards_horizontal = boards_vertical = arr = []
numbers = lines[0][0].split(',')

for line in lines[2:]:
    line = [num for num in line if num != ''] # Delete redundant spaces
    if(line == []):
        boards_horizontal.append(arr)
        arr = []
        continue
    
    arr.append(line)

if(arr != []):
    boards_horizontal.append(arr)

# Transpose matrix (transform rows to column)
boards_vertical = [[[boards_horizontal[k][j][i] for j in range(len(boards_horizontal[k]))] for i in range(len(boards_horizontal[k][0]))] for k in range(len(boards_horizontal))]

first_ans = 0
second_ans = 0

# For every number in winner numbers
for i in range(len(boards_horizontal[0]), len(numbers)):
    j = 0
    while j < len(boards_horizontal):
        for k in range(len(boards_horizontal[j])):
            win = False
            if(is_row_winner(numbers[:i], boards_horizontal[j][k])):
                if(first_ans == 0):
                    first_ans = int(numbers[:i][-1]) * sum_no_winners_numbers(numbers[:i], boards_horizontal[j])
                second_ans = int(numbers[:i][-1]) * sum_no_winners_numbers(numbers[:i], boards_horizontal[j])
                win = True
                break
            elif(is_row_winner(numbers[:i], boards_vertical[j][k])):
                if(first_ans == 0):
                    first_ans = int(numbers[:i][-1]) * sum_no_winners_numbers(numbers[:i], boards_vertical[j])
                second_ans = int(numbers[:i][-1]) * sum_no_winners_numbers(numbers[:i], boards_vertical[j])
                win = True
                break

        # Remove matrix from boards in case the board won    
        if(win):
            boards_horizontal.pop(j)    
            boards_vertical.pop(j)
        j += 1
    
print("Task one:", first_ans)
print("Task two:", second_ans)