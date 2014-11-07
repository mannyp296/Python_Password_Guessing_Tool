#!/usr/bin/env python
#Manuel Perez CS 177 Homework 5, Password Cracker
import sys
import crypt
import time

def initCrack():
	total = len(sys.argv)
	if(total!=2):
		print("Error: No shadow file included: ")
		return
	dict = raw_input( "Enter dictionary to use: ")
	#print ("dictionary: " + dict)
	name = sys.argv[1]
	print("Shadow File: " + name)
	f = open( name ,'r')
	for line in f:
		line = line.rstrip('\n')
		#print("info: " + line)
		ind = line.find(':')
		usr = line[:ind]
		ind+=1
		line = line[ind:]
		print("user: " + usr)
		ind = line.find(':')
		#print("middle: " + line)
		line = line[:ind] 
		#print("hash: " +line)
		#print("other:")
		#hasht = crypt.crypt("1ht41ht4", line)#"$6$asdfghjhgfdsa")
		#print ("hascheck:" + hasht)
		#hasht = crypt.crypt("TURTLE", "asdfghjkl")
		#print ("hascheck2:" + hasht)
		#hasht = crypt.crypt("TURTLE", "$6$asdfghjhgfdsa")
		#print ("hascheck2:" + hasht)
		dictionaryFind(dict,dict,line, line,1,3,0,8)
		break
	return

def des(word, salt,hashed):
	hashed2 = crypt.crypt(word, salt)
	x=0
	#print (hashed)
	if (hashed2 == hashed):
		x=1
		print("password: " + word)
	return x
def checkReverse(line, salt, hashed):
	line2=line[::-1]
	x = des(line2,salt, hashed)
	return x

def checkUpLow(line, salt, hashed, y):
	sw=1
	pos=0
	slen = len(line)
	mylist = list(line)
	position = []
	#print("lenght: "+ str(slen))
	for i in range (slen):
		if(mylist[i]>='a' and mylist[i]<='z'):
			position.append(0)
		elif(mylist[i]>='A' and mylist[i]<='Z'):
			mylist[i] = chr(ord(mylist[i]) + 32)
			position.append(0)
		else:
			position.append(3)	
	while (sw==1):
		line2 = ''.join(mylist)
		y[0]=y[0]+1.0;
		#print("Next: " + line2)
		x= des(line2,salt,hashed)
			
		#if(y[0]>81450630.0):
		#	print(str(y[0]))
		#	break
		if(x==1):
			break
		while True:
			#Move to next position
			position[pos]=position[pos]+1
			if (position[pos]<2):
				mylist[pos]=chr(ord(mylist[pos]) - 32)
				break
			
			#if options maxed out move to another char or char is number
			else:
				if(position[pos]==4):
					position[pos]=position[pos]- 1
				pos+=1;
			if(pos==slen):
				sw=0
				break
		for i in range (pos):
			if(position[i]!=3):
				position[i]=0
				mylist[i] = chr(ord(mylist[i]) + 32)
		pos=0

	return x

def bruteForce(salt, hashed, n, y, start, end):
	char=[]
	guess=[]
	position=[]
	sw=1
	x=0
	pos=0
	total=52
	for i in range(26):
		ch = chr(ord('a') +i)
		char.append(ch)
	for i in range(26):
		ch = chr(ord('A') + i)
		char.append(ch)
	if(n>1):
		total=62
		for i in range(10):
			ch = chr(ord('0') + i)
			char.append(ch)
	if(n>2):
		total=95
		for i in range(16):
			ch = chr(ord(' ') + i)
			char.append(ch)
		for i in range(7):
			ch = chr(ord(':') + i)
			char.append(ch)
		for i in range(6):
			ch = chr(ord('[') + i)
			char.append(ch)
		for i in range(4):
			ch = chr(ord('{') + i)
			char.append(ch)
	#start brute force process
	if(start==0):
		start=1
	slen=start
	for i in range(start):
		position.append(0)
		guess.append(char[0])
	
	while (sw==1):
		line = ''.join(guess)
		y[0]=y[0]+1.0;
		x= des(line,salt, hashed)
		q=1.0
			
		if(x==1):
			break
		while True:
			#Move to next position
			position[pos]=position[pos]+1
			if (position[pos]<total):
				guess[pos]=char[(position[pos])]
				break
			#if options maxed out move to another character
			else:
				pos+=1;
			if(pos==slen):
				slen+=1
				position.append(0)
				guess.append(char[0])
				if(slen>end):
					sw=0
					break
		for i in range (pos):
			position[i]=0
			guess[i] = char[0]
		pos=0
	return x

def dictionaryFind(dictionary, dict2, salt, hashed, dicEn, mode, start, end):
	f = open(dictionary,'r')
	x=0
	y=0.0
	time1=time.time()
	words= []
	b=0;
	if(dicEn==1):
		for line in f:
			line = line.rstrip('\n')
			y=y+1.0
			#test for normal case
			#x = des(line,salt, hashed)
			#if (x==1):
			#	break
			#test for reversed strings
			y+=1.0
			x = checkReverse(line, salt, hashed)
			if (x==1):
				break
			#Test for uppercase and lowercase
			ypoint=[y]
			x = checkUpLow(line, salt, hashed, ypoint)
			y = ypoint[0]
			if (x==1):
				break
			#Test for dictionary combo
			if(dict2 != ""):
				#Only open file once
				if(b==0):
					f2 = open(dict2,'r')
					a=0;
					b=1
					for line2 in f2:
						line2 = line2.rstrip('\n')
						words.append(line2)
						a=a+1
					f2.close()
				for i in range (a):
					line2 = line + words[i]
					y=y+1.0
					#test for normal case in double
					x = des(line2,salt, hashed)
					if (x==1):
						break
				if(x==1):
					break
	if(x==0 and mode>0):
		ypoint=[y]
		x = bruteForce(salt, hashed, mode, ypoint, start, end)
		y=ypoint[0]

	timeOut = (y/(time.time()-time1))*6.0
	
	f.close()
	print("hashes: " + str(y) +", match: " + str(x))
	print("hashes/min: " + str(timeOut))
	return


#dictionaryFind("dictionary.DIC",'abE.x.71IRaTM')
#dictionaryFind("dictionary.DIC","test.txt",'abcdefghigklm',1,0,0,8)

initCrack()

#print("hash: " +hasht)

