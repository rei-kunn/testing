def ans():
    ans = int(input("write any number from 1 to 10"))
    if ans < 11:
        for i in range(1,100,2):
            print(i)
    else:
        raise ValueError("the value should be less than 11")
ans()