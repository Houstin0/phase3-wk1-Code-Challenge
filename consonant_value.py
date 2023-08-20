def consonant_value(string):
    value=0
    max_value=0
    for char in string:
        if char not in 'aeiou':
            value+= ord(char)-ord('a')+1
            max_value=max(max_value,value)
        else:
            value=0    
    print(max_value)
    return max_value 
             
consonant_value("strength")           