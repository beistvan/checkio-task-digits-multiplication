from functools import reduce
from random import randint


def solver(numb):
    return reduce(lambda x, y: x * y,
                  [int(d) for d in str(numb) if d != "0"],
                  1)

#print(solver([0, 1, 2, 3, 4, 5]) == 30)
#print(solver([1, 3, 5]) == 30)
#print(solver([6]) == 36)
#print(solver([]) == 0)

tests = []

for _ in range(20):
    t = randint(1, 1000000)
    ans = solver(t)
    print('{{"input": {0},\n"answer": {1}\n}},\n'.format(t, ans))



