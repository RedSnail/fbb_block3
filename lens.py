lens = []
counter = 0
with open("bilis_CDS.fasta", "r") as inp:
	for line in inp:
		if line.startswith(">") and (counter > 0):
			lens.append(counter - 1)
			if counter == 4822:
				print(line)
			counter = 0
		else:
			counter += len(line.strip())

lens.append(counter - 1)
print(f"total {len(lens)}\n")
print(f"max {max(lens)}\n")
print(f"min {min(lens)}\n")
import matplotlib.pyplot as plt

plt.hist(lens, bins=50, rwidth=0.8, label="H. bilis")
plt.show()
