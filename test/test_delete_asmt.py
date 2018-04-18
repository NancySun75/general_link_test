to_delete_asmt=[]
f = open('to_delete_samt.txt', 'r')
for line in f:
	to_delete_asmt.append(map(string,line.split('\n')))
print (to_delete_asmt)
