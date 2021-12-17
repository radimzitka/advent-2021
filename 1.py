with open('inputs/1.input') as file:
  lines = [int(line.rstrip()) for line in file.readlines()]

prev_sum = lines[0]
counter = 0

for number in lines:
  if(number) > prev_sum:
    counter += 1
  prev_sum = number

print("Task one:", counter)

counter = 0
prev_sum = lines[0] + lines[1] + lines[2]
for i in range(1, len(lines) - 2):
  curr_sum = lines[i] + lines[i + 1] + lines[i + 2]
  if(curr_sum > prev_sum):
    counter += 1
  prev_sum = curr_sum

print("Task two:", counter)