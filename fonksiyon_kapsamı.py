#global scope

x=0

def fonk():
    #local scope
    x=1
    return x

#print(fonk()) 0 yazdı
#print(x) 1 yazdı


a=[]
print("a'nın ilk değeri:",a)


def degistir():
    def degistir2():
        a.append(1)

    degistir2()
    return a

print(degistir())
print("a'nın son değeri")