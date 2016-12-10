def fib(n):   # return Fibonacci series up to n
	if 𝑛 ≤ 1:
		return 𝑛
	else:
		result=[]
		result.append(0)        ## starts with 0 and 1
		result.append(1)
		[result.append(result[-1]+result[-2]) for i in range(2, n)]
		return result
