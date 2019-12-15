from collections import defaultdict
from itertools import repeat

with open("hepatic_power.annotations", "r") as inp, \
     open("../hepatic_power.txt", "r") as source, \
     open("hepatic_power.labels", "w") as out:
	existing_labels = defaultdict(lambda: "\n", 
                                      map(lambda x: (x.split("\t")[0], x.split("\t")[-1]), inp))
	[out.write(existing_labels[line.strip()]) for line in source]

