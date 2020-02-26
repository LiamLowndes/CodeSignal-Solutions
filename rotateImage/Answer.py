def rotateImage(a):
    
    rot = []
    row = len(a[0])
    
    #create a new list thats blank (populated with just zeros)
    for i in range(row):
        rot.append([])
        for j in range(row):
            rot[i].append(0)
    
    #fill the blank list with the newly rotated image
    for i in range(row):
        for j in range(row):
            rot[i][j] = a[(row-1) - j][i]
        print()
    return(rot)
