from random import randint
with open('for_homework_5.txt', mode='w+') as f:
    f.write(" ".join([str(randint(1, 500)) for _ in range(50)]))
    f.seek(0)
    print(sum(map(int, f.readline().split())))