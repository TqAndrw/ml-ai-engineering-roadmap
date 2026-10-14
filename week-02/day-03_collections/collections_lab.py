from time import perf_counter

# 1. list / tuple / set / dict
numbers_list = [1, 2, 2, 3]
numbers_tuple = (1, 2, 2, 3)
numbers_set = {1, 2, 2, 3}
prices = {"A": 10.5, "B": 20.0}

print("list:", numbers_list)
print("tuple:", numbers_tuple)
print("set:", numbers_set)
print("dict lookup:", prices["B"])


# 2. set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("union:", a | b)
print("intersection:", a & b)
print("difference:", a - b)


# 3. slicing / unpacking
nums = [10, 20, 30, 40, 50]

print("slice:", nums[1:4])

first, second, *rest = nums
print("first:", first)
print("second:", second)
print("rest:", rest)


# 4. comprehensions
evens = [x for x in range(10) if x % 2 == 0]
squares = {x: x * x for x in range(5)}

print("evens:", evens)
print("squares:", squares)


# 5. membership benchmark
N = 1_000_000

users_list = list(range(N))
users_set = set(users_list)

target = N - 1

start = perf_counter()
target in users_list
list_time = perf_counter() - start

start = perf_counter()
target in users_set
set_time = perf_counter() - start

print("list membership seconds:", list_time)
print("set membership seconds:", set_time)
