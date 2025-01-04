import math

"""
n//10 + n//100*10 + n//1000*100 + ...

300

32 + 30

+ (n % 10 > 1)
+ min(max(0,n%100)-(2*10-1)), 10)

"""

n = 25
numTwos = 0
for i in range(math.floor(math.log(n, 10))):
    numTwos += n//pow(10, i+1) * pow(10, i)

for i in range(math.floor(math.log(n, 10)) + 1):
    currPow = pow(10, i)
    # pow(10, 2) = 100
    numGreater = (n%pow(10,i+1)) - (2*currPow-1)
    # print(numGreater)
    numTwos += min(max(0, numGreater), currPow)
"""
0 - (2*10-1) = -19
"""
print(numTwos)
