
#Create a Python file named lab_10-3.py
#Write a program that contains a function called double_stuff. The function should take a list as its only parameter.
#When a list is passed as an argument to the function, the function should double each value in the list, regardless of its type
#Write test cases to confirm that your function works when passed a list that:
#Contains only integers
#Contains integer and float values
#Contains a combination of integer, string, and float values
def double_stuff(list):
    for i,v in enumerate(list):
        list[i] = (v + v)  
    return list
       
       
print(double_stuff([2,6,9,4]) == [4, 12, 18, 8])
print(double_stuff([2,3.4,6.8,8.2,5.9]) == [4, 6.8, 13.6, 16.4, 11.8])
print(double_stuff([1,3.6,"string"]) == [2, 7.2, 'stringstring']) 
    
    
     
        
#_____________________________________________________________________________________________________________

#Create a Python file named lab_10-4.py

#Write a program that contains a function called indexed_names. 
#The function should take a list of names as its only parameter.
#When a list is passed as an argument to the function,
#the function should return a new list where each value is replaced by the index, 
#followed by a color, space, and the original value
#i.e. passing through ["John", "Jane", "Bob"] 
#would return ["0: John", "1: Jane", "2: Bob"]
#Write 2 test cases to confirm that your function works when passed a list that:


def indexed_names(list):
    for i,v in enumerate(list):
        
        list[i] = str(i) + ": " + v
    return list

print(indexed_names(["John", "Jane", "Bob"]) == ["0: John", "1: Jane", "2: Bob"])
print(indexed_names(["Senku", "Gen", "Chrome"]) == ["0: Senku", "1: Gen", "2: Chrome"])
print(indexed_names([]) == [])