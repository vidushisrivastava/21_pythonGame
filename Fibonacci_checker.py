import math
x=int(input("Enter a number to check if it is present in the fibonacci series: "))
def perf_sq(num):
    s=int(math.sqrt(num))
    return s*s==num

def fibo_check():
    global x
    return perf_sq((5*x*x)+4) or perf_sq((5*x*x)-4)

if fibo_check()==True:
    print("Present")
else:
    print("Absent")
