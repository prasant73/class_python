# def return_runnerup_score(n, arr):
#     highest, second_highest = 0, 0
#     if arr[0] > arr[1]:
#         highest, second_highest = arr[0], arr[1]
#     else:
#         highest, second_highest = arr[1], arr[0]
#     for i in arr[2:]:
#         if i > highest and i > second_highest:
#             i = highest
#             second_highest = highest
#         elif i > second_highest and i < highest:
#             second_highest = i
#     return second_highest

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     print(return_runnerup_score(n, arr))



def return_max(a, b):
    if a > b:
        return a, b
    return b, a

def return_gcd(a,b):
    a, b = return_max(a, b)
    while b != 0:
        a, b = b, a % b
    return a

def generalizedGCD(num, arr):
    gcd = 0
    # WRITE YOUR CODE HERE
    for i in range(1, num):
        if i == 0:
            if arr[0] == 0 or arr[1] == 0:
                return 0
            gcd = return_gcd(arr[0], arr[1])
        else:
            if arr[i] == 0:
                return 0
            gcd = return_gcd(gcd, arr[i])
    return gcd

print(generalizedGCD(5, [0,2,3,4,5]))