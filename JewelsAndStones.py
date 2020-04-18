def numJewelsInStones(jewls, stones):
    jewls_count = 0
    for jewel in jewls:
        for stone in stones:
            if jewel == stone:
                jewls_count += 1
    
    return jewls_count

print (numJewelsInStones ("aA", "aAAbbbb"))