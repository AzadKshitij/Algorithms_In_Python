def bubble_short(sequence):
	indexing_length = len(sequence) - 1
	shorted = False

	while not shorted:
		shorted = True
		for i in range(indexing_length):
			if sequence[i] > sequence[i+1]:
				shorted = False
				sequence[i],sequence[i+1] = sequence[i+1],sequence[i]
	return sequence

print(bubble_short([89,399,757,257,372,553,241,216,48,355,41,34,798,470,751]))
