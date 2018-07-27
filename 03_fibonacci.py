# Fibonacci Sequence Generator
def fibonacci(n):
	list = []
	for x in range(1,n):
		list.append(get_next(list))
	return list

def get_next(list):
	if not list:
		return 0;
	if len(list) == 1:
		return 1
	return list[-1]+list[-2] 

n = int(input('Enter number of items: '))
print(fibonacci(n))
