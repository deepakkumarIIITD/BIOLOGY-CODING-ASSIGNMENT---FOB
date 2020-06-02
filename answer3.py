def dH_counter(s,t):
	counter = 0
	for i in range(len(s)):
		if(s[i] != t[i]):
			counter = counter + 1
	return  "Hamming distance for the two sequence is : "+ str(counter)
def decoder(stt):
	l = []
	for i in range(len(stt)):
		if(stt[i] == ">"):
			l.append(i)
	l.append(len(stt))
	return l
def string_getter(list_indexes , stt):
	l = []
	for i in range(len(list_indexes) - 1):
		start = list_indexes[i]
		end = list_indexes[i+1]
		l.append(stt[start:end])
	return l
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
def sequence_maker(stt):
  sequence = ""
  for line in stt:
    sequence += line.strip()
  return sequence
def final(list_codes):
	l = []
	for i in range(len(list_codes)):
		string_one = sequence_maker(list_codes[i])
		string_one = string_one[num_pos(string_one):]
		l.append(string_one)
	print(dH_counter(l[0],l[1]))
def main():
	my_file = (open("input2.txt")).read()
	final(string_getter(decoder(my_file),my_file))
main()