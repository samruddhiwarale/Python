first = "listen"
second ="silent"
if len (first)  !=len(second) :
    print (False)
else :
    count={}

    for char in first :
        if char in count:
            count[char] += 1
        else:
            count[char]= 1

    for char in second:
        if char in count:
            count[char]-= 1
        else:
            count[char]= -1
    result = True
    for value in count.values ():
        if value != 0 :
            result = False
            break
    print(result)