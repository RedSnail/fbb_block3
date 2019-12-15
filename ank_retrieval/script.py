import numpy as np
from sys import argv

AA = "ARNDCQEGHILKMFPSTWYV"

with open(argv[1], "r") as inp, \
     open(argv[2], "w") as out:
	outseq = ""
	name = ""
	prob = 1.0
	for line in inp:
		if line.startswith(">"):
			if len(outseq) > 0:
				out.write(f">{name} {prob:.4f}\n")
				out.write(outseq + "\n")

			outseq = ""
			prob = 1
			name = "".join(line.split()[:-1])
			name = name[1:]
			continue

		vals = np.array(line.split("\t")[1:], dtype=float)
		if np.max(vals) == 0:
			continue

		max_ind = np.argmax(vals)
		prob = prob*vals[max_ind]
		outseq += AA[max_ind]


	out.write(f">{name} {prob:.4f}\n")
	out.write(outseq + "\n")
