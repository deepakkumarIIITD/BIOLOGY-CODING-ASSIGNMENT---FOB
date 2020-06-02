# code by DEEPAK KUMAR 2019418
def counter(stt , count_stt):
  counter_sum = 0
  for i in range(len(stt)-1):
    if(stt[i:i+2] == count_stt):
      counter_sum += 1
  return counter_sum

def dictionary_maker(stt):
  dictionary_of_frequencies = {"AA":counter(stt,"AA"),"AC":counter(stt,"AC"),"AG":counter(stt,"AG"),
                               "AT":counter(stt,"AT"),"CA":counter(stt,"CA"),"CC":counter(stt,"CC"),
                               "CG":counter(stt,"CG"),"CT":counter(stt,"CT"),"GA":counter(stt,"GA"),
                               "GC":counter(stt,"GC"),"GG":counter(stt,"GG"),"GT":counter(stt,"GT"),
                               "TA":counter(stt,"TA"),"TC":counter(stt,"TC"),"TG":counter(stt,"TG"),
                               "TT":counter(stt,"TT")
                              }
  return dictionary_of_frequencies

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

def list_of_chars(stt):
  return list(stt)

def final(dict_stt , list_stt):
  for i in range(len(list_stt)):
    print(list_stt[i] + " : " + str(dict_stt[list_stt[i]]))

def dictionary_getter(stt):
  return dictionary_maker(stt)

def start_to_end(stt):
  index = num_pos(stt)
  return stt[index:]

def sequence_maker(stt):
  sequence = ""
  with open(stt) as file:
    for line in file:
        sequence += line.strip()
  return sequence

def main():
  my_file = "input3.txt"
  stt = start_to_end(sequence_maker(my_file))
  final(dictionary_getter(stt) , list_of_chars(dictionary_getter(stt)))
main()
# code by DEEPAK KUMAR 2019418