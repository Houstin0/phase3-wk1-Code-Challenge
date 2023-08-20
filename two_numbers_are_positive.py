def two_positive_numbers(a,b,c):
    positive_numbers=0
    if a>0:
        positive_numbers+=1
    if b>0:
        positive_numbers+=1
    if c>0:
        positive_numbers+=1
    print(positive_numbers==2)
    return positive_numbers==2 
        
two_positive_numbers(7,-2,3)    