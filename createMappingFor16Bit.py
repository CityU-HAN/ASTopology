import collections
from collections import OrderedDict

CAIDA_FILE = './caidarel3.txt'
OUT_FILE_1='./cbgp_16bit2AS_map.txt'
OUT_FILE_2='./cbgp_AS216bit_map.txt'
MAX_AS_NO=65535

temp_dict=dict()
mapping_dict=OrderedDict()


curr_idx=1

with open(CAIDA_FILE) as fi:
	for line in fi:
		ll=line[:len(line)-1]
		splits=ll.split(' ')
		one=splits[0]
		two=splits[1]
		one_i=int(one)
		two_i=int(two)
		if one_i<=MAX_AS_NO:
			if not one in temp_dict:
				temp_dict[one]=one
		if two_i<=MAX_AS_NO:
			if not two in temp_dict:
				temp_dict[two]=two

added_as_set=set()

with open(CAIDA_FILE) as fi:
	lnum=0
	for line in fi:
		lnum=lnum+1
		ll=line[:len(line)-1]
		splits=ll.split(' ')
		one=splits[0]
		two=splits[1]
		one_i=int(one)
		two_i=int(two)
		if one_i>MAX_AS_NO:
			for i in range(curr_idx, MAX_AS_NO+1):
				if not str(i) in temp_dict and not one in added_as_set:
					temp_dict[str(i)]=one
					added_as_set.add(one)
					curr_idx=i+1
					print lnum
					break
		if two_i>MAX_AS_NO:
			for i in range(curr_idx, MAX_AS_NO+1):
				if not str(i) in temp_dict and not two in added_as_set:
					temp_dict[str(i)]=two
					added_as_set.add(two)
					curr_idx=i+1
					print lnum
					break

mapping_dict = collections.OrderedDict(sorted(temp_dict.items()))

print OUT_FILE_1
fo=open(OUT_FILE_1, 'w')

try:
	for key in mapping_dict:
		print key+' '+mapping_dict[key]
		fo.write(key+' '+mapping_dict[key]+'\n')
finally:
	fo.close()








