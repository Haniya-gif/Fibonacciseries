# I couldn't understand the parent code but by the looks of it,
# it seems like a function for displaying Fibonacci sequence.
# I have appended the numbers to a list so they can be used for further computation. 
#Like sum of fibonacci sequience (also known as fibonacci series) till a number n specified or further more computation I have implemented sum here 
def fib(n):
	num_list = [0]
	prev = 0
	now = 1
	for x in range(n-1):
		num_list.append(now)
		temp = now
		now += prev
		prev = temp  		
	return num_list
	
def sum_of_fib(n):
	num_list = fib(n)
	num_sum = 0	
	for num in num_list:
		num_sum += num
	return num_sum
num = int(input("Enter the specific number:"))
print('Fibbonacci series till the number :')
print(fib(num))
print('sum of fibonacci sequence till the specified number is:' ,sum_of_fib(num))
