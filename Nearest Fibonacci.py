a = [15,1,3]
jumA= sum(a)
x = 0
n1 = [0]
n2 = [1]

print("Fibonacci sequence:")
while sum(n1) < jumA:
# for x in a:    
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth

print('Bilangan fibonaccci: %d' % sum(n1))
print('Selisih dengan fibonacci terdekat: %d' % (sum(n1)-jumA))