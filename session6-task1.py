rows=int(input("enter the number of rows:"))
for i in range(rows):
    line=""
    for x in range(rows-i-1):
        line+=" "
    for y in range(2*i+1):
         line+="*"
    print(line)
