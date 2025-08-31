

def doubleToStr(num):
    ans = ["0", "."]
    while num > 0:
        num *= 2
        ans.append(str(int(num)%2))
        if len(ans) > 32:
            return "ERROR"
        if num >= 1:
            num -= 1
    return ''.join(ans)


nums = [
    0.5,        # 0.1
    0.125,      # 0.001
    0.1,        # ERROR
    0.0625,     # 0.0001
    0.72,       # ERROR
    0.83984375, # 11010111
]

for n in nums:
    print(doubleToStr(n))