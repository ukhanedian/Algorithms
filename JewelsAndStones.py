def numJewelsInStones(J, S):
    jewelsIhave = 0
    for jewel in J:
        for stone in S:
            if jewel == stone:
                jewelsIhave += 1
    
    return jewelsIhave

print (numJewelsInStones ("aA", "aAAbbbb"))