i = 1
while i <= 100
	print(i,end="")
	if i % 3 == 0:
		if i % 3 == 0 and i % 5 == 0:
			print(" Fizz Buzz!")
		else:
			print(" Fizz!")
	elif i % 5 == 0:
		print(" Buzz!")
	else:
		print("")
	i += 1