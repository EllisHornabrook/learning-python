list = ['Lets', 'make', 'a', 'list', 2]
    # lists can hold both strings and integers
listTwo = ['add', 'to', 'list']
list + listTwo
    # returns joint lists
newList = list + listTwo
    # creates new list
list.append(15) 
    # adds to the end
list.pop() 
    # removes from the end
list.remove(2) 
    # removes first instance of value given
listOfLists = [list, listTwo, [1, 2, 3]]
    # create new list with lists
del(listOfLists[1][2])
    # deletes the third value in the second list (s)