def decompressRLElist (nums):
	decompressList = []
	pairList = []
	for i in range (len (nums)):
		if i % 2 == 0:
			# make a pairList of [freq, val]
			pairList.append (nums [i])
			pairList.append (nums [i + 1])

			# append in decompressList with frequency
			for frequency in range (pairList [0]):
				decompressList.append (pairList [1])

			# remove elements from pairList
			pairList.remove (pairList [1])
			pairList.remove (pairList [0])

	return decompressList

print (decompressRLElist ([1, 2, 3, 4]))