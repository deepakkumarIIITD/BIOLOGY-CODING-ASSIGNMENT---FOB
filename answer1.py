def gc_summer(stt):
	return(stt.count("G") + stt.count("C"))
def percentage(stt):
	return((gc_summer(stt)/len(stt))*100)
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
	my_dictionary = dict()
	l = []
	for i in range(len(list_of_samples)):
		string = list_of_samples[i]
		index = num_pos(string)
		header = string[:index]
		dna = string[index:]
		my_dictionary.__setitem__(percentage(dna),header)
		l.append(percentage(dna))
	while(len(l) > 0):
		maximum_gc = max(l)
		print(my_dictionary[maximum_gc] + " : " + str(maximum_gc) + " %")
		l.remove(maximum_gc)
def main():
	my_file = "input1.txt"
	protein = sequence_maker(my_file)
	getter(decode(protein))
main()