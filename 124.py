def foo(a):
    reversedWord = ""
    for i in range(len(a) -1, -1, -1):
        reversedWord += a[i]
    print(reversedWord)
slovo = "либида"
foo(slovo)