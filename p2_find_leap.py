'''
4, 8, 12
2000
2400
3200
400
800

100
200
300
500
2100
2200

divisible by 4 can be leap
if year is divisible by 4 and not by 100 (4, 8, 12) - leap
if year is divisible by 4 and also by 100 (100, 200, 300, 500, 2100) - not leap
if year is divisible by 4 and also by 400 (2000, 2400, 2800)
'''

def check_leap(year):
    if year % 4 != 0:
        return False
    else:
        if year % 400 == 0: # 2100
            return True
        elif year % 100 == 0:
            return False
        else:
            return True

# list_of_years = [4, 8, 12, 100, 200, 300, 500, 2100, 2000, 2400, 2800]
# for year in list_of_years:
    # if check_leap(year):
    #     print(year, "leap")
    # else:
    #     print(year, "not leap")

start = int(input("Enter starting range - "))
end = int(input("Enter ending range - "))

for year in range(start, end + 1):
    if check_leap(year):
        print(year, "leap")
    else:
        print(year, "not leap")


