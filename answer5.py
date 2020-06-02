def sequence_3_sorter(stt):
	l = []
	i = 0;
	j = 3;
	while(len(stt) >0):
		string = stt[i : j]
		l.append(string)
		stt = stt[j:]
	return l
def codon_table(stt):
	codon_table_dictionary  =  {"UUU" : "PHE","UUC" : "PHE","UUA" : "LEU","UUG" : "LEU",
								"CUU" : "LEU","CUC" : "LEU","CUA" : "LEU","CUG" : "LEU",
								"AUU" : "LLE","AUC" : "LLE","AUA" : "LLE","AUG" : "MET",
								"GUU" : "VAL","GUC" : "VAL","GUA" : "VAL","GUG" : "VAL",
								"UCU" : "SER","UCC" : "SER","UCA" : "SER","UCG" : "SER",
								"CCU" : "PRO","CCC" : "PRO","CCA" : "PRO","CCG" : "PRO",
								"ACU" : "THR","ACC" : "THR","ACA" : "THR","ACG" : "THR",
								"GCU" : "ALA","GCC" : "ALA","GCA" : "ALA","GCG" : "ALA",
								"UAU" : "TYR","UAC" : "TYR","UAA" : "@@@","UAG" : "@@@",
								"CAU" : "HIS","CAC" : "HIS","CAA" : "GLN","CAG" : "GLN",
								"AAU" : "ASN","AAC" : "ASN","AAA" : "LYS","AAG" : "LYS",
								"GAU" : "ASP","GAC" : "ASP","GAA" : "GLU","GAG" : "GLU",
								"UGU" : "CYS","UGC" : "CYS","UGA" : "@@@","UGG" : "TRP",
								"CGU" : "ARG","CGC" : "ARG","CGA" : "ARG","CGG" : "ARG",
								"AGU" : "SER","AGC" : "SER","AGA" : "ARG","AGG" : "ARG",
								"GGU" : "GLY","GGC" : "GLY","GGA" : "GLY","GGG" : "GLY"
								}
	return codon_table_dictionary[stt]
def dalton_table(stt):
	dalton_table_dictionary =  {"ALA" : 89,"ARG" : 174,"ASN" : 132,"ASP" : 133,
								"CYS" : 121,"GLN" : 147,"GLU" : 146,"GLY" : 75,
								"HIS" : 155,"LLE" : 131,"LEU" : 131,"LYS" : 146,
								"MET" : 149,"PHE" : 165,"PRO" : 115,"SER" : 105,
								"THR" : 119,"TRP" : 204,"TYR" : 181,"VAL" : 117,
								"@@@" : 0
								}
	return dalton_table_dictionary[stt]
def requiered_array(list_of_codons):
	index_1 = 0
	index_2 = 0
	for i in range(len(list_of_codons)):
		if(list_of_codons[i] == "MET"):
			index_1 = i
			break
	i = len(list_of_codons) - 1
	while( i > 0):
		if(list_of_codons[i] == "@@@"):
			index_2 = i
			break
		i = i - 1
	l = [index_1 , index_2 + 1]
	return list_of_codons[l[0]:l[1]]
def methy_pos_giver(requiered_array_list):
	l = []
	for i in range(len(requiered_array_list)):
		if(requiered_array_list[i] == "MET"):
			l.append(i)
	return l
def stop_pos_giver(requiered_array_list):
	l = []
	for i in range(len(requiered_array_list)):
		if(requiered_array_list[i] == "@@@"):
			l.append(i)
	return l
def maker(requiered_array_list):
	list_of_methyl_starters = methy_pos_giver(requiered_array_list)
	return list_of_methyl_starters
def calculas(list_of_threes):
	counter = []
	for i in range(len(list_of_threes)):
		counter.append(codon_table(list_of_threes[i]))
	return counter
def proper_codon_giver(requiered_array_list , list_of_methyl_starters):
	l = []
	for i in range(len(list_of_methyl_starters)):
		start = list_of_methyl_starters[i]
		working_list = requiered_array_list[start:len(requiered_array_list)]
		k = []
		for i in range(len(working_list)):
			if(working_list[i] != "@@@"):
				k.append(working_list[i])
			else:
				break
		l.append(k)
	return l
def to_sum(list_of_protein_sequences):
	for i in range(len(list_of_protein_sequences)):
		list_of_calculator = list_of_protein_sequences[i]
		protein_seq = ""
		for x in range(len(list_of_calculator)):
			protein_seq+=list_of_calculator[x]+" "
		c = final(list_of_calculator)
		print("According to 3 letter code convention the protein sequence is : " + protein_seq)
		print("mass of the above protein sequence is : " + str(c))
		print("------------------------------------------------------------------------------")
		
def sequence_maker(stt):
  sequence = ""
  with open(stt) as file:
    for line in file:
        sequence += line.strip()
  return sequence
def final(list_final):
	counter = 0
	for i in range(len(list_final)):
		counter += dalton_table(list_final[i])
	return counter
def main():
	my_file = "input4.txt"
	RNA = sequence_maker(my_file)
	to_sum(proper_codon_giver(requiered_array(calculas(sequence_3_sorter(RNA))),maker(requiered_array(calculas(sequence_3_sorter(RNA))))))
main()