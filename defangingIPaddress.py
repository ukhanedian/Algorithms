def defangIPaddr(address):
    defang = ""
    for ch in address:
       if ch == '.' :
            defang += "[.]"
       else:
            defang += ch
    return defang

print (defangIPaddr ("1.1.1.1"))