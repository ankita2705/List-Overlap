a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
count=0
len(a)
len(b)
c=[]
for num1 in a:
    for num2 in b:
        if(num1==num2):
            c.append(num1)

'''for num3 in c:
    for num4 in c:
        if(num3==num4):
            count+=1
            if(count>1):
                c.del(num3)'''
for num3 in c:
	count=0
	for num4 in c:
		if(num3==num4):
			count+=1
			if(count>1):
				c.remove(num3)
				print(c)

				
