with open('inputs/13.input') as file:
  lines = [line.rstrip() for line in file.readlines()]

hashtags = []
folds = []

# Load entry data
for line in lines:
    if('fold' not in line and line != ''):
        hashtags.append([int(line.split(',')[0]), int(line.split(',')[1])])

    elif(line != ''):
        fold_coor = line.split(' ')[2].split('=')
        folds.append([fold_coor[0], int(fold_coor[1])])

# Load size of array (max y and max x) on the beginning
size_x, size_y = 0, 0
for hashtag in hashtags:
    if(hashtag[0] > size_x):
        size_x = hashtag[0]
    if(hashtag[1] > size_y):
        size_y = hashtag[1]

# Fold array in ways from assignment
for i in range(len(folds)):
    # Horizontal fold
    way = 1
    size_y = folds[i][1]

    # Vertical fold
    if(folds[i][0] == 'x'):
        way = 0
        size_x = folds[i][1]

    # Change coordinates of hashtags by the fold
    for j in range(len(hashtags)):
        if(hashtags[j][way] > folds[i][1]):
            hashtags[j][way] = abs(hashtags[j][way] - folds[i][1] * 2)

    # Remove duplicate hashtags from array
    res = []
    [res.append(x) for x in hashtags if x not in res]
    hashtags = res[:]

    if(i == 0):
        print("Part one:", len(hashtags))

# Make text area
text_area = [ [' '] * size_x for i in range(size_y)]

# Set hashtags for relevant points in the text area
for hashtag in hashtags:
    text_area[hashtag[1]][hashtag[0]] = '#'

# Draw all the letters
i = 0
print("Part two:")
for line in text_area:
    for letter in line:
        print(letter, end='')
        
        i += 1
        if(i == 5):
            print('    ', end='')
            i = 0

    print('')

    