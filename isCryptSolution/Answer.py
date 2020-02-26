def isCryptSolution(crypt, solution):
    combo = []
    
    #make combo a list of the three numbers seperated by "-"
    for i in range(3):
        for j in crypt[i]:
            for k in solution:
                if k[0] == j:
                    combo.append(k[1])
                    break
        combo.append("_")
    
    newCombo = [[]]
    count = 0
    
    #break the numbers into their three individual parts and store it in 2D array newCombo
    for i in combo:
        if i == "_":
            newCombo.append([])
            count+=1
        else:
            newCombo[count].append(i)
    newCombo.remove([])
    
    #check for leading zeros
    for i in range(3):
        if ((newCombo[i][0] == '0') and len(newCombo[i]) > 1):
            return(False)
    
    #check validity using numb function
    if numb(newCombo[0]) + numb(newCombo[1]) != numb(newCombo[2]):
        return(False)
    
    return(True)

#creats the integer value for the list of nmbers (ex. it converts [1, 2, 3] into 123) 
def numb(arr):
    
    num = 0
    lenArr = len(arr)
    count = -1
    
    for i in range(lenArr-1, -1, -1):
        count += 1
        num += int(arr[count]) * (10 ** i)

    return(num)
