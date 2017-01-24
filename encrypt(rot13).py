text = list(raw_input('Text to be encrypted: '))

firsthalf = 'ABCDEFGHIJKLMabcdefghijklm'
lasthalf = 'NOPQRSTUVWXYZnopqrstuvwxyz'

output = ''

for i in text:
	if i in firsthalf:
		output += lasthalf[firsthalf.index(i)]
	elif i in lasthalf:
		output += firsthalf[lasthalf.index(i)]
	else:
		output += i

print output