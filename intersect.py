with open("cinadei_not_bilis.txt", "r") as inp1, \
     open("cinadei_not_pylori.txt", "r") as inp2, \
     open("cinadei_only.txt", "w") as out:
	set1 = set(map(lambda x: x.strip(), inp1))
	set2 = set(map(lambda x: x.strip(), inp2))
	cinadei_only = set2 & set1
	print(f"{len(cinadei_only)} cinadei-specific genes")
	[out.write(item + "\n") for item in cinadei_only]

