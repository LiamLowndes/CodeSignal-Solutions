def firstNotRepeatingCharacter(s):
  
    #create a set for the repeating and uniq characters
    reps = set()
    uniq = set()
     
    #sort the characters into the appropriate sets
    for i in range(len(s)):
        if s[i] in uniq:
            uniq.remove(s[i])
            reps.add(s[i])
        elif s[i] in reps:
            continue
        else:
            uniq.add(s[i])
    
    #return the proper output
    if len(uniq) == 0:
        return("_")
    else:
        #find the repeating character that is earliest in the list
        hold = len(s) + 1
        for j in uniq:
            temp = s.find(j)
            if temp < hold:
                hold = temp
        return(s[hold])
