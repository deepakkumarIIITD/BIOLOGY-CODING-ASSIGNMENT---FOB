def DNA_to_mRNA(stt):
	empty = ""
	for i in range(len(stt)):
		if(stt[i] == "T"):
			empty += "A"
		elif(stt[i] == "A"):
			empty += "U"
		elif(stt[i] == "C"):
			empty += "G"
		elif(stt[i] == "G"):
			empty += "C"
	return empty
def sequence_maker(stt):
  sequence = ""
  with open(stt) as file:
    for line in file:
        sequence += line.strip()
  return sequence
def arrow_finder(stt):
	l = []
	for i in range(len(stt)):
		if(stt[i] == ">"):
			l.append(i)
	l.append(len(stt))
	return l
def decode(stt):
	list_of_indices = arrow_finder(stt)
	list_of_samples = []
	for i in range(len(list_of_indices)-1):
			sample = stt[list_of_indices[i]:list_of_indices[i+1]]
			list_of_samples.append(sample)
	return list_of_samples
def num_pos(stt):
	for i in range(len(stt)):
		if(stt[i] == "C"):
			return i;
		elif(stt[i] == "G"):
			return i;
		elif(stt[i] == "A"):
			return i;
		elif(stt[i] == "T"):
			return i;
def getter(list_of_samples):
	for i in range(len(list_of_samples)):
		string = list_of_samples[i]
		index = num_pos(string)
		header = string[:index]
		dna = string[index:]
		print(header)
		print(DNA_to_mRNA(dna))
def main():
	my_file = "input1.txt"
	protein = sequence_maker(my_file)
	getter(decode(protein))
main()