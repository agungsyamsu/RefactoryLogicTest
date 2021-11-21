n = 10

final_list = []

for i in range(1, n+1, 1):
    if i%3==0 and i%5==0:
        a = "Fizzbuzz"
    else:
        if i%3==0:
            a = "Fizz"
        else:
            if i%5==0:
                a = "Buzz"
            else:
                a = i
    final_list.append(a)
print(final_list)