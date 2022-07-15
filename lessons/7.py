#wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

def wave(string):
    arr = []
    k = 0
    while k < len(string):
        arr.append(string[:k] + string[k::].title())
        k += 1
    print(arr)

wave('hello')