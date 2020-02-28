import random
# get two input values, diplay them then swap w/o temp variable
def questionOne():
	x = input("Please enter an integer value: ")
	y = input("Please enter another integer value: ")
	print("x = " + str(x) + "\ty = " + str(y))
	x = x + y
	y = x - y
	x = x - y
	print("x = " + str(x) + "\ty = " + str(y))

# Q2 will get user input for number between 10 and 20 and print a pyramid of stars
def questionTwo():
	x = input("Enter a whole number between 10 and 20: ")
	print("You entered: " + str(x))
	while(x > 0):
		print("*" * x)
		x -= 2

def questionThree():
	x = input("Enter a whole a whole number: ")
	y = input("Enter another whole number: ")
	add = x + y
	diff = x - y
	pro = x * y
	floatQuo = round((float(x) / float(y)), 2)
	intQuo = x // y
	remain = x % y
	print("Sum = " + str(add))
	print("Difference = " + str(diff))
	print("Product  = " + str(pro))
	print("Quotient(float) = " + str(floatQuo))
	print("Quotient(int) = " + str(intQuo))
	print("Remained(int) = " + str(remain))


# matrix subtraction
def questionFour():
	A = [[-1, -2, -3], [4, 5, 6]]
	B = [[1, 2, 3], [-4, -5, -6]]
	C = [[0, 0, 0], [0, 0, 0]]
	for i in range(len(A)):
		for j in range(len(A[i])):
			C[i][j] = A[i][j] - B[i][j]
	print("------------------\nA:\n------------------")
	print(A)
	print("------------------\nB:\n------------------")
	print(B)
	print("------------------\nC: A - B\n------------------")
	print(C)
# fill 50 index array w/ rand ints then do linear search
def quesitonFive():
	# line 54 - 57 initialize random generator --> https://docs.python.org/3/library/random.html
	random.seed()
	random.setstate(random.getstate())
	random.getrandbits(32)

	# how to initialize blank list of n elements brackets whats list initialized w/
	randList = [-1] * 50
	# used to format printing, 5 per line
	count = 1
	for i in range(len(randList)):
		randList[i] = random.randrange(0, 101)
		if not count % 5: 
			print(randList[i])
		else:
			# end tell what to end the print w/ prevents prenting on each line
			print(randList[i], end = '\t')
		count += 1
	target = int(input("Enter a number to find: "))
	found = 0;
	for i in range(len(randList)):
		if randList[i] == target: 
			print(str(target) + " found at index " + str(i))
			found = 1
			break
	if not found: print(str(target) + " not found in list.")


# conduct binary search
def questionSix():
	sortList = [1, 7, 13, 20, 38, 57, 89, 116, 252, 9863]
	print(*sortList)
	index = -1
	left = 0
	# using fixed len for example
	right = 9
	target = int(input("Enter a number: "))
	while left <= right:
		# integer divide
		mid = (left + right) // 2
		if sortList[mid] == target: 
			print(str(target) + " found at index " + str(mid))
			break
		elif sortList[mid] > target: right = mid - 1
		elif sortList[mid] < target: left = mid + 1
	if left > right: print(str(target) + " not found.")

# bubble sort
def questionSeven(): 
	# len = 10
	A = [15, 99, 8, -66, 79, 35, -89, 42,  2, 28]
	print("Array: " + str(A))
	for i in range(9):
		for j in range(9 - i):
			if A[j] > A[j + 1]:
				temp = A[j]
				A[j] = A[j + 1]
				A[j + 1] = temp
	print("Bubble sorted array: " + str(A))

# determines palindrome
def questionEight():
	word = input("Enter a word: ")
	begin = 0
	end = len(word) - 1
	while(begin <= end):
		if word[begin] != word[end]: print(word + " is NOT a palindrome!")
		else:
			begin += 1
			end -= 1
	if begin > end: print(word + " is a palindrome.")

# fibonacci recursive
def questionNine(n):
	if n <= 1: return n
	else: return questionNine(n - 1) + questionNine(n - 2)

#define vowel or not 
# ------------------ PYTHON DOES NOT HAVE A SWITCH STATEMENT ------------------ 
def questionTen():
	x = input("Enter a letter: ").lower()
	# ord casts char to int value
	x = ord(x)
	if x == 97 or x == 101 or x == 105 or x == 111 or x == 117: print(chr(x) + " is a vowel")
	else: print(chr(x) + " is NOT a vowel.")


def main():
	# questionOne()
	# questionTwo()
	# questionThree()
	# questionFour()
	# quesitonFive()
	# questionSix()
	# questionSeven()
	# questionEight()
	#find the nth fib number by using n - 1
	# target = int(input("Enter a number: "))
	# print("The " + str(target) + " finonnaci number is " + str(questionNine(target - 1)))
	questionTen()

main()