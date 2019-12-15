from urllib.request import urlopen


inp = open("cinadei_accession.txt", "r")
out = open("cinadei_proteome.fasta", "w+")

i = 0
for line in filter(lambda x: len(x.strip()) > 0, inp):
	if i <= -1:
		i += 1
		continue

	while True:
		try:
			with urlopen(f"https://www.ebi.ac.uk/ena/data/view/{line[:-1]}&display=fasta") as fasta:
				cur_prot = fasta.read().decode()
				lines = cur_prot.splitlines()
				cur_prot = "".join([">", lines[0].split()[0].split("|")[2], "\n", *(lines[1:]), "\n"])
			
			break
		except:
			print("exception caught")


	out.write(cur_prot)
	print(i)
	i = i + 1

out.close()
inp.close()

