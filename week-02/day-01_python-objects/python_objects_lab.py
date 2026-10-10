# 1. Identity vs equality
a = [1, 2]
b = [1, 2]

print("a == b:", a == b)
print("a is b:", a is b)

# 2. Aliasing
x = [10, 20]
y = x
y.append(30)

print("x:", x)
print("y:", y)
print("x is y:", x is y)

# 3. Rebinding
m = [1, 2]
n = m
n = n + [3]

print("m:", m)
print("n:", n)
print("m is n:", m is n)

# 4. In-place mutation
p = [1, 2]
q = p
q += [3]

print("p:", p)
print("q:", q)
print("p is q:", p is q)

# 5. Shallow copy
users = [["alice"], ["bob"]]
backup = users.copy()
backup[0].append("vip")

print("users:", users)
print("backup:", backup)
print("users is backup:", users is backup)
print("users[0] is backup[0]:", users[0] is backup[0])

# 6. Truthiness
values = [0, None, "", [], [0], "hello"]

for value in values:
    print(repr(value), "->", bool(value))
