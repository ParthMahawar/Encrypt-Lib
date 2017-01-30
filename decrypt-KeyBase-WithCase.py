tempkey = int(raw_input('Enter Key: '))
base = int(raw_input('Enter Base: '))
text = raw_input('Text to be decrypted: ')

def basechange(num, bas):
	nums = []
	fin = 0
	for i in range(1000):
		nums.append(0)
	tempoutput = []
	output = ''

	for i in range(len(nums)):
		nums[i] = 0
		while bas**(len(nums)-i) <= num:
			num -= bas**(len(nums)-i)
			nums[i] += 1
		tempoutput.append(nums[i])
	tempoutput.append(num)

	for i in tempoutput:
		output += str(i)

	return str(int(output))

key = basechange(tempkey, base)
textlist = list(text)

letternumber = {'1': 53, '0': 62, '3': 55, '2': 54, '5': 57, '4': 56, '7': 59, '6': 58, '9': 61, '8': 60, 'A': 1, 'C': 5, 'B': 3, 'E': 9, 'D': 7, 'G': 13, 'F': 11, 'I': 17, 'H': 15, 'K': 21, 'J': 19, 'M': 25, 'L': 23, 'O': 29, 'N': 27, 'Q': 33, 'P': 31, 'S': 37, 'R': 35, 'U': 41, 'T': 39, 'W': 45, 'V': 43, 'Y': 49, 'X': 47, 'Z': 51, 'a': 2, 'c': 6, 'b': 4, 'e': 10, 'd': 8, 'g': 14, 'f': 12, 'i': 18, 'h': 16, 'k': 22, 'j': 20, 'm': 26, 'l': 24, 'o': 30, 'n': 28, 'q': 34, 'p': 32, 's': 38, 'r': 36, 'u': 42, 't': 40, 'w': 46, 'v': 44, 'y': 50, 'x': 48, 'z': 52}

numlist = []
for i in textlist:
	numlist.append(letternumber.get(i, i))
def check(a, b):
	while a>=b:
		a-=b
	return a

for i in range(len(numlist)):
	x = i
	if numlist[x] in range(1, 63):
		try:
			numlist[x] = int(numlist[x]) - int(key[i])
		except:
			i = check(i, len(key))
			try:
				numlist[x] = int(numlist[x]) - int(key[i])
			except:
				pass

inverse = dict()

for keys in letternumber:
	inverse[letternumber[keys]] = keys

outputlist = list()

for i in numlist:
	try:
		if i <= 0:
			i += 62
		if i <= 0:
			i += 62
		if i <= 0:
			i += 62
		if i <= 0:
			i += 62
		if i <= 0:
			i += 62
	except:
		pass
	outputlist.append(inverse.get(i, i))

output =''

for i in outputlist:
	output += str(i)

print 'DECRYPTED TEXT:', output
