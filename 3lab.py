x = str(input())

for i in range(len(x)-1):
	print(i)
	print(len(x))
	print(x[i] + " "+x[int(len(x))-i] )
	if x[i] != x[int(len(x))-i]:
		print("no")
		
		
		break


