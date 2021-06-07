
if __name__ == '__main__':

    lst = list(map(int, input("\nEnter the numbers : ").strip().split()))
    sumofnumber = 0
    for t in lst:
        sumofnumber = sumofnumber + t
    avg = sumofnumber / len(lst)
    print(round(avg, 2))