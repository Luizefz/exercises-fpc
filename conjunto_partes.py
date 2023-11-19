def substring(n):
    for comeco in range(len(n)):
        for permutas in range(comeco, len(n) + 1):
            print(n[comeco:permutas])

substring("carlos")