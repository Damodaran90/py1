import time

def main():
    iArray = [2,6,9,5,14,3,78,8,75,60]
    test = "hello ffff ?_12685i?oui?_o22dioajfiafiewiriujfdiosapj"
    print(iArray)
    for k in range(10):
        min = iArray[k]
        for j in range(k+1,10):
            if min > iArray[j]:
                temp = min
                min = iArray[j]
                iArray[j] = temp 
        iArray[k] = min
    print(iArray)

if __name__ == '__main__':
    main()
