with open('inputs/12.input') as file:
  rules = [line.rstrip().split('-') for line in file.readlines()]

def two_lower(path, rule):
    if(path.count(rule) == 0):
        return True

    is_there_any_two_lower = False

    for item in path:
        if(item.islower() and path.count(item) > 1):
            is_there_any_two_lower = True

    if(is_there_any_two_lower and path.count(rule) >= 1):
        return False

    return True

def find_continued(path, rules, first_task):
    continued = []
    if(path[-1] == 'end'):
        return continued

    if(first_task):
        for rule in rules:
            if(path[-1] == rule[0] and (rule[1].isupper() or rule[1] not in path) and rule[1] != 'start'):
                continued.append(rule[1])

            if(path[-1] == rule[1] and (rule[0].isupper() or rule[0] not in path) and rule[0] != 'start'):
                continued.append(rule[0])

    else:
        for rule in rules:
            if(path[-1] == rule[0] and (rule[1].isupper() or two_lower(path, rule[1])) and rule[1] != 'start'):
                continued.append(rule[1])

            if(path[-1] == rule[1] and (rule[0].isupper() or two_lower(path, rule[0])) and rule[0] != 'start'):
                continued.append(rule[0])

    return continued

def make_paths(rules, first_task):
    paths = [['start']]
    paths_done = []

    while(True):
        new_path = False 
        paths_new = []

        for path in paths:
            offshots = find_continued(path, rules, first_task)

            for offshot in offshots:
                new_path = True

                if(offshot == 'end'):
                    paths_done.append(path[:] + [offshot])
                else:
                    paths_new.append(path[:] + [offshot])


        if(new_path == False):
            break

        paths = paths_new

    return len(paths_done)

print("Part one:", make_paths(rules, True))
print("Part two:", make_paths(rules, False))
