with open('10.input') as file:
  lines = [line.rstrip() for line in file.readlines()]

def bracket_complement(bracket):
    if(bracket == '('):
        return ')'
    elif(bracket == '{'):
        return '}'
    elif(bracket == '['):
        return ']'
    elif(bracket == '<'):
        return '>'
    if(bracket == ')'):
        return '('
    elif(bracket == '}'):
        return '{'
    elif(bracket == ']'):
        return '['
    elif(bracket == '>'):
        return '<'

score = 0
lines_bkp = lines[:]
for line in lines:
    stack = []
    for bracket in line:

        if(len(stack) == 0):
            stack.append(bracket)
            continue

        if(bracket_complement(bracket) == stack[-1]):
            stack.pop()

        elif(bracket == '(' or bracket == '[' or bracket == '{' or bracket == '<'):
            stack.append(bracket)

        else:
            if(bracket == ')'):
                score += 3
            elif(bracket == ']'):
                score += 57
            elif(bracket == '}'):
                score += 1197
            elif(bracket == '>'):
                score += 25137

            lines_bkp.remove(line)
            break

print("Part one:", score)


lines = lines_bkp[:]
complements = []
for line in lines:
    stack = []

    for bracket in line:
        if(bracket == '(' or bracket == '{' or bracket == '[' or bracket == '<'):
            stack.append(bracket)

        elif(bracket_complement(stack[-1]) == bracket):
            stack.pop()

    for i in range(len(stack)):
        stack[i] = bracket_complement(stack[i])
    
    complements.append(reversed(stack))

scores = []
for brackets in complements:
    score = 0
    for bracket in brackets:
        if(bracket == ')'):
            score = score * 5 + 1
        elif(bracket == ']'):
            score = score * 5 + 2
        elif(bracket == '}'):
            score = score * 5 + 3
        elif(bracket == '>'):
            score = score * 5 + 4

    scores.append(score)

scores.sort()
winner_score = scores[int(len(scores) / 2)]
print("Part two:", winner_score)

