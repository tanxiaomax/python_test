

def fib(n):


    if n < 2:
        print([1,1])
        return

    fib_array= [1,1]


    for i in range(1,n):
        temp = fib_array[i-1] + fib_array[i]
        fib_array.append(temp)



def fib_1(max):
    n,a,b =0,0,1
    while n < max:
        yield b
        a,b =b,a+b
        n = n+1
    return 'done'
a = fib_1(10)
print(fib_1(10))
print(a.__next__())
print(a.__next__())
print(a.__next__())
print("可以顺便干其他事情")
print(a.__next__())
print(a.__next__())