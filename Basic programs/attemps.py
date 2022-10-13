def attempts(n):
    x = 1
    while x <= n:
        print("Attempt" + str(x))
        x += 50
    print("Done")


attempts(500)

