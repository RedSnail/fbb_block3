from sys import argv

with open(f"{argv[1]}_matches.blast", "r") as inp:
	matched_genes = set(map(lambda x: x.split("_")[0], inp))

print(list(matched_genes)[:10])
with open("cinadei_accession.txt", "r") as inp:
	total = set(filter(lambda x: len(x) > 0, map(lambda x: x.strip(), inp)))

print(list(total)[:10])
with open(f"cinadei_not_{argv[1]}.txt", "w") as out:
	[out.write(item + "\n") for item in (total - matched_genes)]

print(f"{len(total) - len(matched_genes)} non-homologous genes")
