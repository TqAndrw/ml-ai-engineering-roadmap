# 1. Mutation through shared object
def add_item(items):
    items.append("x")

a = []
add_item(a)
print("mutation:", a)


# 2. Rebinding local name
def add_one(x):
    x = x + 1
    return x

a = 10
result = add_one(a)

print("original:", a)
print("returned:", result)


# 3. LEGB
x = "global"

def outer():
    x = "outer"

    def inner():
        print("LEGB:", x)

    inner()

outer()


# 4. nonlocal
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1

    increment()
    increment()

    return count

print("counter:", counter())


# 5. *args
def total(*numbers):
    return sum(numbers)

print("total:", total(1, 2, 3, 4))


# 6. **kwargs
def show_user(**info):
    print("user:", info)

show_user(name="Tristan", age=23)


# 7. Mutable default pitfall
def bad_add_user(name, users=[]):
    users.append(name)
    return users

print("bad 1:", bad_add_user("Alice"))
print("bad 2:", bad_add_user("Bob"))


# 8. Correct default pattern
def add_user(name, users=None):
    if users is None:
        users = []

    users.append(name)
    return users

print("good 1:", add_user("Alice"))
print("good 2:", add_user("Bob"))
