"""

Write a Python program find a list of integers
with exactly two occurrences of nineteen and at least
three occurrences of five ?

"""

list_len = int(input("How many elements you want in list : - "))
liz = []
for i in range(list_len):
    print("Enter Elements :- ")
    usr_input = int(input())
    liz.append(usr_input)
print("User Entered Elements in List :- {}".format(liz))

if len(liz) >0:
    for j in range(len(liz)):
        if(liz.count(19) == 2 and liz.count(5) >= 3):
            print("List is Valid.")
        else:
            break