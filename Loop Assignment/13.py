# 13.python program to get the Fibonacci series between 0 to 50

a, b = 0, 1
fibonacci_series = []

while a <= 50:
    fibonacci_series.append(a)
    a, b = b, a + b

print("Fibonacci series between 0 and 50:")
print(fibonacci_series)
