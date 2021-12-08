with open('8.input') as file:
  lines = file.readlines()
  lines = [line.rstrip().split(' ') for line in lines]

# 1. eba dacgefb deacb gabfde ecgadb cbdef cage gcbad afbdcg ae | gdfeba ae dfbec agce 
for i in range(len(lines)):
    lines[i].pop(10)
# First 10 items are coded digits, next 4 combinations is output value
# 2. eba dacgefb deacb gabfde ecgadb cbdef cage gcbad afbdcg ae gdfeba ae dfbec agce

counter = 0
for line in lines:
    # Count strings which have exact length
    for digit in line[10:]:
        if(len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7):
            counter += 1

print("Task one:", counter)

# ------ PART TWO ------

# Return string from arr which has len length
def find_item_by_len(arr, length):
    for item in arr:
        if(len(item) == length):
            return item

def sort_alphabetically(str):
    return ''.join(sorted(str))

# Decodes digit by code and return exact number
def return_digit(code, number):
    two = sort_alphabetically(number[0] + number[2] + number[3] + number[4] + number[6])
    three = sort_alphabetically(number[0] + number[3] + number[6] + number[2] + number[5])
    five = sort_alphabetically(number[0] + number[1] + number[3] + number[5] + number[6])

    zero = sort_alphabetically(number[0] + number[1] + number[2] + number[4] + number[5] + number[6])
    six = sort_alphabetically(number[0] + number[1] + number[3] + number[4] + number[5] + number[6])
    nine = sort_alphabetically(number[0] + number[1] + number[2] + number[3] + number[5] + number[6])
    code = sort_alphabetically(code)


    if(len(code) == 2):
        return '1'
    elif(len(code) == 3):
        return '7'
    elif(len(code) == 4):
        return '4'
    elif(len(code) == 7):
        return '8'
    elif(code == two):
        return '2'
    elif(code == three):
        return '3'
    elif(code == five):
        return '5'
    elif(code == six):
        return '6'
    elif(code == nine):
        return '9'
    elif(code == zero):
        return '0'


sum = 0
for line in lines:
    number = 7 * ['']
    """
Index of segment in arr number:
             0000 
            1    2
            1    2
             3333 
            4    5
            4    5
             6666 

             """
    # One, seven and four have exact len
    one, seven, four = find_item_by_len(line[:10], 2), find_item_by_len(line[:10], 3), find_item_by_len(line[:10], 4)
    possible_leters = "abcdefg"

    # Find letter on number[0]
    for letter in seven:
        if(letter not in one):
            number[0] = letter

    # Coded numbers to one string (first 10 codes in array)
    coded_letters = ""
    for code in line[:10]:
        coded_letters += code

    # Delete letter at number[0] from coded_letters
    coded_letters = coded_letters.replace(number[0], "")
    possible_leters = possible_leters.replace(number[0], "")

    # Every position on 7-segment display is used exact x times 
    # (for example segment 5 (number[5]) is used for all numbers without 2, it means it is used 9x)
    for letter in possible_leters:
        if(coded_letters.count(letter) == 9):
            number[5] = letter
        elif(coded_letters.count(letter) == 8):
            number[2] = letter
        elif(coded_letters.count(letter) == 6):
            number[1] = letter
        elif(coded_letters.count(letter) == 4):
            number[4] = letter
        else:
            continue
        # If letter is used, its position is known
        possible_leters = possible_leters.replace(letter, "")

    # There are always two positions left (number[3] and number[6]) and this numbers need to assign
    # Number four uses number[3], not number[6] - if letter is in code of four, it means it has to be on number[3] position
    if(possible_leters[0] in four):
        number[3], number[6] = possible_leters[0], possible_leters[1]
    else:
        number[3], number[6] = possible_leters[1], possible_leters[0]

    # Array 'Number' contains all possible letters on exact position
    # Now it is neccessary to decode all codes ans sum it together
    ans = ''
    for code in line[10:]:
        ans += return_digit(code, number)
    sum += int(ans)

print("Part two:", sum)
    
