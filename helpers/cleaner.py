import enchant
d = enchant.Dict("en_US")

l = []

with open("wiki-100k.txt", 'r') as f:
    l = f.read()

l = l.split("\n")

count = 0

with open('wiki-67k.txt', 'w') as w:
    for line in l:
        if l[0] != "#" and d.check(line):
            count += 1
            w.write(line.lower() + "\n")

print(count)
