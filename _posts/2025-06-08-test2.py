import random

n_students = int(input("enter a number of studens:"))
scores = [random.randint(0,100) for _ in range(n_students)]
scores1 = [random.randint(0,100)]
print(f"{len(scores) = }")
print(f"{scores = }")
print(f"{scores1 =}")