
liz_len = int(input("Enter how many elements you want in List :- "))
liz =[]
for i in range(0,liz_len):
    usr_input = int(input("Enter Elements :-  "))
    liz.append(usr_input)
print(liz)

def verify(liz):
    return liz.count(19) == 2 and liz.count(5)>= 3

print(verify(liz))