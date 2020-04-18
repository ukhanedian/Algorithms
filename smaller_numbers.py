def smallerNumbersThanCurrent (nums):
    OutputList = []
    for num in nums:
        smaller = 0
        for i in nums:
            if i != num:
                if i < num:
                    smaller += 1
        OutputList.append (smaller)
    return OutputList

print (smallerNumbersThanCurrent ([8,1,2,2,3]))