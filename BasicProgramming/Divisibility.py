import sys
sys.set_int_max_str_digits(10000000)

def Divisibility(n, N):
    last_digits = "".join(str(num)[-1] for num in N)
    if int(last_digits) % 10 == 0:
        return "Yes"
    else:
        return "No"
n = int(input())
N = list(map(int, input().split()))
result = Divisibility(n, N)
print(result)
