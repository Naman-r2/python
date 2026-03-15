def cs(l1):
    if len(l1)==0 or len(l1)==1:
        return True
    if(l1[0]>=l1[1]):
      return False
    
    return cs(l1[1:])




print(cs([2,5,7,9,10]))