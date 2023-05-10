#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a-b)
    print(a*b)
#The provided code stub reads two integers, a and b from STDIN.
#Add logic to print two lines. The first line should contain the result of integer division,a//b
#The second line should contain the result of float division a/b
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
#The provided code stub reads and integer,n  from STDIN. For all non-negative integers i<n print i*i:
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i*i)

#An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
#In the Gregorian calendar, three conditions are used to identify leap years:
#The year can be evenly divided by 4, is a leap year, unless:
#The year can be evenly divided by 100, it is NOT a leap year, unless:
#The year is also evenly divisible by 400. Then it is a leap year.
def is_leap(year):
    leep = False
    if (year % 4 == 0):
        leep = True
    if (year % 100 == 0):
        leep = False
    if (year % 400 == 0):
        leep = True

    # Write your logic here

    return leep
year = int(input())

#The included code stub will read an integer n,from STDIN
#Without using any string methods, try to print the following:123..n
#Note that "..." represents the consecutive values in between.

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end='')