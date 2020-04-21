def balancedStringSplit (s):
	count = 0
	R = 0
	L = 0
	for i in s:
		# if it is "R"
		if i == "R":
			R += 1
		
		# if it is "L"
		elif i == "L":
			L += 1
		
		# if no. of Rs and Ls are equal so increment the count
		if L == R:
			count += 1
			# set L and R to zero
			L = 0
			R = 0
	return count

print (balancedStringSplit ("RLRRLLRLRL"))