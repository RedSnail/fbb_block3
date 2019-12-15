from sys import argv
from toolkit import iteritems

with open(argv[1], "r") as full, \
     open(argv[2], "r") as slice, \
     open(argv[3], "w") as out:
	names = set(map(lambda x: x.strip(), slice))
	print(len(names))
	source = list(iteritems(full))
	print(source[0])
	items = filter(lambda x: x[0] in names, source)
	[out.write(f">{name}\n{seq}\n") for name, seq in items]

