def is_prime(n):

	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5 
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
		return False
	i += 6 
	return True 

def count_primes_between_zero_and_n(n):
	count = sum(1 for i in range(2, n + 1) if is_prime(i))
	return count

number = int(input("Enter a number: "))
prime_count = ccount_primes_between_zero_and_n(number)
print(f"There are {prime_count} prime numbers between 0 and {number}.")
