# The actual working code is tpc.py :)

def arrange_data(s, key):
	data = []
	n = len(s)
	rows = n//key + 1
	cols = key
	for i in range(rows + 1):
		row_val = []
		row_val = [c for j, c in enumerate(s) if ((j < i*key) and (j >= (i-1)*key))]
		for k, l in enumerate(row_val):
			if l == " ":
				row_val[k] = "$"

		if row_val != []:
			data.append(row_val)
	return [data, n]

def directionalise_data(data, n):
	beg_r = 0
	end_r = len(data)-1
	beg_c = 0
	end_c = len(data[0])
	flag = 0
	leng = 0

	new_data = []
	# while((beg_r != end_r) and (beg_c != end_c)):
	while leng <= n:
		print ("beg_c: ", beg_c)
		print ("end_c: ", end_c)
		print ("beg_r: ", beg_r)
		print ("end_r: ", end_r)
		for i in range(beg_r, end_r+1):
			new_data.append(data[i][beg_c])
			leng += 1
		flag = 1
		print (n, leng)
		print (new_data)

		if leng >= n:
			break

		leng += len(data[i][beg_c+1:end_c])

		if leng >= n:
			break		

		print (data[i][beg_c+1:end_c])
		new_data.extend(data[i][beg_c+1:end_c])
		print (n, leng)
		print (new_data)
		flag = 2
		beg_c += 1
		end_c -= 1

		leng += end_r - beg_r - 1

		if leng >= n:
			break

		for i in range(end_r-1, beg_r-1, -1):
			new_data.append(data[i][end_c])
		flag = 3
		print (n, leng)
		print (new_data)

		leng += len(data[beg_r][end_c-1:beg_c-1:-1])
		if leng >= n:
			break

		print (data[beg_r][end_c-1:beg_c-1:-1])
		new_data.extend(data[beg_r][end_c-1:beg_c-1:-1])
		print (n, leng)

		flag = 4
		beg_r += 1
		end_r -= 1

		print ("Inbetween")
		print ("beg_c: ", beg_c)
		print ("end_c: ", end_c)
		print ("beg_r: ", beg_r)
		print ("end_r: ", end_r)

		print(new_data, "\n")
	# if (len(data) < len(data[0])) and flag == 4:
	# 	new_data.extend(data[beg_r][beg_c:end_c])
	# elif (len(data) < len(data[0])) and flag == 2:
	# 	new_data.extend(data[beg_r][end_c:beg_c])


	encrypted_data = ""
	for c in new_data:
		encrypted_data += c
	print(encrypted_data)

	return encrypted_data


def transposition_cipher(s, key):
	[data, n] = arrange_data(s, key)
	encrypted_data = directionalise_data(data, n)

	return encrypted_data

s = input("Enter string: \n>")
key = int(input("Enter key: \n>"))
encrypted_data = transposition_cipher(s, key)
if encrypted_data == "Wlousethlew$lle$wrntabl$$llew$the":
	print ("Yayyyyy!!!!")