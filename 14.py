with open('inputs/14.input') as file:
  lines = [line.rstrip() for line in file.readlines()]

# Get template
template = lines[0]

# Hash table due to speed
rules = {}
occurrencies = {}
alphabet = []

# Get rules from asignment
for line in lines[2:]:
    rules[line.split(' -> ')[0]] = line.split(' -> ')[1]

# Make hash table - for every couple of letters in template is made an record with number of repeatings
# For example, couple 'NH' is in string two times, so occurencies['NH'] = 2  
for i in range(len(template) - 1):
    occurrencies[template[i:i+2]] = occurrencies.get(template[i:i+2], 0) + 1

for i in range(40):
    new_occurrencies = {}

    # For every record in occurrencies are two record made:
    # For example, for record 'NH' is made records 'NC' and 'CN'
    # Both record are saved in new_occurencies with value of repeatings (>1 if the record is found, 1 if record was created)
    for occurrence in occurrencies:
        # new_occurrencies['NC'] = new_occurrencies['NC'] + 1
        new_occurrencies[occurrence[0] + rules[occurrence]] = new_occurrencies.get(occurrence[0] + rules[occurrence], 0) + occurrencies[occurrence]
        
        # new_occurrencies['CN'] = new_occurrencies['CN'] + 1
        new_occurrencies[rules[occurrence] + occurrence[1]] = new_occurrencies.get(rules[occurrence] + occurrence[1], 0) + occurrencies[occurrence]

    occurrencies = new_occurrencies
    
    if(i == 9):
        print("Part one: ", end='')
    elif(i == 39):
        print("Part two: ", end='')
    else:
        continue

    # In occurencies are couples, care just about first letter
    alphabet = {}
    for occurency in occurrencies:
        # Increse value of first letter in occurency about its occurrence
        alphabet[occurency[0]] = alphabet.get(occurency[0], 0) + occurrencies[occurency]

    print(max(alphabet.values()) - min(alphabet.values()) + 1)