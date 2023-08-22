##I basically used this to know the number of items on a text editor cause after creating a
#list(normal, vertical...like a shopping list) over time. 
#Works best if you tend to skip a line before creating another item

 
a=int(input("How many lines you at?"))
counts = 0
# for i in range(0, a, 2):			# THIS CODE WORKS TOO.
# 	counts += 1						
# print(counts)		


for i in range(0, a):
	if i%2==1 :					#完璧👌
		counts += 1
	else: 
		print("counting...")
	print(counts)
