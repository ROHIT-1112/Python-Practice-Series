"""
Write a Python program that accept a list of integers and check the length and the fifth element.
 Return true if the length of the list is 8 and fifth element occurs thrice in the said list.

"""

len_liz = int(input("Enter the Total Number of elements you want in List :- "))
liz = []
for i in range(len_liz):
    usr_input = int(input("Enter Elements :- "))
    liz.append(usr_input)
print(liz)

if isinstance(liz,int):
    for i in range(len(liz)):
        if len(liz) == 8 and liz[5].count() >= 3:
            print("List is Valid")
        else:
            break