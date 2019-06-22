import re

fhand = open('regex_sum_228958.txt')

count = 0
for line in fhand:
    lst = re.findall("([0-9]+)", line)

    for i in lst:
        count = count + int(i)

    
print(count)