bracktes=input("enter bracktes")
stack=[]
for i in bracktes:
    if i in "([{":
        stack.append(i)
    elif i==")"and stack[-1:]==["("]:
        stack.pop()
    elif i=="]"and stack[-1:]==["["]:
        stack.pop()
    elif i=="}"and stack[-1:]==["{"]:
        stack.pop() 
    else:
        print("not balanced") 
        break   
else:
    if not stack:
        print("balanced")
    else:
        print("not balanced")



