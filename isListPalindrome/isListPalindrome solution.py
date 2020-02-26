# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def isListPalindrome(l):
    
    #Create an empty dictionary and a counting variable
    hold = {}
    count1 = -1
    
    #Loop through linked list to create dictionary where key = value of current linked list position and value = index of linked list 
    while l is not None:
        
        count1+=1
        
        hold[count1] = l.value

        l = l.next

    #determine if values on oposite sides of list are equal and return the result (dont check middle number if odd) 
    count2 = -1
    for i in range(len(hold) - 1, (len(hold)//2) - 1, -1):
        count2 += 1
        if hold[i] != hold[count2]:
            return(False)
    return(True)
