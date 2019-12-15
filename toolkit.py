def iteritems(inp):
	out = ""
	for line in inp:
		if (line.startswith(">")) and (len(out) > 0):
			lines = out.split("\n")
			yield (lines[0][1:].strip(), "".join(lines[1:]))
			out = ""

		out = out + line

	yield out


