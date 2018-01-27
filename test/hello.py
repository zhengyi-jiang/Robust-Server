print("Hello, World!")
def fizzbang(n):
    for i in range(n):
        print(i)
        pass
    pass

fizzbang(3)

for i in ([123,'hello'],[1,2]):
    for j in range(1):
        print(i[j:])
        pass
    pass

j = 0
for i in [x*x for x in {x for x in range(1,356) if x % 2 is not 0} if x % 3 == 1]:
    print("Element " + str(j) + ": " + str(i))
    j=j+1
    pass

