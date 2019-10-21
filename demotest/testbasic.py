def intgenerator():
    for i in range(20):
        yield i


res = list(intgenerator())
print(res)