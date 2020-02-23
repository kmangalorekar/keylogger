

keymap = open("keymaps.txt", "r")
keymap_linelist=keymap.readlines()
keymap.close()


keylogger = open("logger.txt", "r")
keylogger_linelist=keylogger.readlines()
keylogger.close()




kmlist={}


# This loop to generate the list of keymaps
	

for i in keymap_linelist:
	i=i.split()
	l=len(i)
	if(l==4):
		kmlist[i[1]]=i[3]
	elif(l==5):
		kmlist[i[2]]=i[4]
	else:
		continue

#kmlist dict generated with keycode:key

klist=kmlist.keys()

#print klist

kllist=[]
st=0
for j in keylogger_linelist:
	j=j.split()

	l=len(j)


	if l==3:
                if j[1]=='14'and len(kllist)!=0:
                    kllist.pop()


		elif j[2]=='release':
                        if j[1]=='42' and st==1:
				kllist.append(j[1])
                                st = 0
				kllist.append('<released>')

			else:
				continue
		else:
                        if j[1]=='42' and st==1:
                            continue
			
			elif j[1]=='42'and st==0:	
			    kllist.append(j[1])
                            kllist.append('<pressed>')
                            st=1
                        
                        elif j[1]!='42':
			    kllist.append(j[1])
                        
                        else:
                            continue


#kllist is generated with codes of input from logger.txt


#print kllist



#Now to decode the keycodes using kmlist dict and writing them in log file

output=open("output.log","w")

for x in kllist:
	for y in klist:
		if x==y:
			output.write(kmlist[y])
	

	if x=='<pressed>':
		output.write('<pressed>')
	elif x=='<released>':
		output.write('<released>')

	#output.write("\n")
			

output.close()


 
#end of program



	




