#Prime number sequence generator
prime_list = []
current_integer = 2
looper = True
print("press enter to generate next prime, enter any other string to exit")
while(looper):
	found_prime = False
	while not found_prime:
		is_prime = True
		for x in prime_list:
			if(current_integer%x == 0):
				is_prime = False
		if(is_prime):
			prime_list.append(current_integer)
			found_prime = True
			print(current_integer)
		current_integer += 1
	looper = input("") == ""