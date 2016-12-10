#!  python3
## Uses python3
## find the product of the maximum pairs of n numbers
# Enter n intergers separated by space
#constraint:'n' must be between 2 and 2x10**5 and 'a' between 0 and 10**5
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

a.sort(reverse=True)
result = 0
if 2<=n<=2*(10**5) and (a[-1]>0 and (a[0]<10**5)):
    result = a[0]*a[1]
else:
     raise ValueError('invalid user input')
  
print(result)


