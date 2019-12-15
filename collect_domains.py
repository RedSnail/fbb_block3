from sys import argv
import subprocess as sp
from toolkit import iteritems

def get_motifs(report_file):
	filtered = list(filter(lambda x: x.startswith("Motif"), report_file))
	return list(map(lambda x: x.split()[2].strip(), filtered))

with open(f"{argv[1]}.fasta", "r") as inp, open(f"{argv[1]}_motifs.txt", "w") as out:
	for item in list(iteritems(inp)):
		temp_out = open("test.fasta", "w")
		temp_out.write(f">{item[0]}\n{item[1]}\n")
		temp_out.close()

		sp.run(["patmatmotifs", "-sequence", "test.fasta", "-out", "report.patmatmotifs"])
		raw = open("report.patmatmotifs", "r")
		out.write(" ".join(get_motifs(raw)) + "\n")
		raw.close()
		sp.run(["rm", "test.fasta"])
		sp.run(["rm", "report.patmatmotifs"])


