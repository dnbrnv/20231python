def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
N = int(input("Enter N: "))
count, num = 0, 2
while count < N:
    if is_prime(num):
        print(num, end=" ")
        count += 1
    num += 1