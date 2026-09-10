def abc():
    for i in range(5):
        yield(i)

gen_obj = abc()

for i in range(5):
    print(next(gen_obj))