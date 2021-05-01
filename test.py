import re

with open('test.txt') as f:
    data = [re.sub(r'[\W_]+', '', word) for line in f for word in line.split()]

print(data[:30])
