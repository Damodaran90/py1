import time

def main():
    list1 = [2,6,9,5,14,3,78,8,75,60]
    print(list1)
    for k in range(10):
        for j in range(0,10-k):
            if j+1>=10:
                break
            else:
                if list1[j] > list1[j+1]:
                    temp = list1[j]
                    list1[j] = list1[j+1]
                    list1[j+1] = temp 
    print(list1)

if __name__ == '__main__':
    main()