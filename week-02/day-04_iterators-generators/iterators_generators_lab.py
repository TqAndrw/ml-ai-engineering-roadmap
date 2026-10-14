# 1. Iterable -> iterator
nums = [10, 20, 30]
it = iter(nums)

print(next(it))
print(next(it))
print(next(it))

try:
    print(next(it))
except StopIteration:
    print("iterator exhausted")


# 2. Custom iterator
class Counter:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


counter = Counter(3)

for x in counter:
    print("custom iterator:", x)


# 3. Equivalent generator
def counter_generator(limit):
    current = 0

    while current < limit:
        yield current
        current += 1


for x in counter_generator(3):
    print("generator:", x)


# 4. Lazy evaluation
def squares(n):
    for i in range(n):
        print("computing", i)
        yield i * i


g = squares(3)

print("generator created")
print("first:", next(g))
print("second:", next(g))


# 5. Large lazy stream
def even_numbers(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i


total = 0

for x in even_numbers(1_000_000):
    total += x

print("sum of evens:", total)

