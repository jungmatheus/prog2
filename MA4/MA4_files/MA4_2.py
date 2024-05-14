
#!/usr/bin/env python3
from numba import njit
from person import Person
from time import perf_counter as pc
from matplotlib import pyplot as plt

def main():


	g = Person(50)
	print(g.getDecades())
	g.setAge(51)
	print(g.getDecades())

	@njit
	def fib_numba(n):
		if n <= 1:
			return n
		else:
			return fib_numba(n-1) + fib_numba(n-2)


	def fib_py(n):
		if n <= 1:
			return n
		else:
			return fib_py(n-1) + fib_py(n-2)


	def time_fib(func, n):
		start = pc()
		func(n)
		end = pc()
		return (end - start)


	f = Person(1)
	#f.setAge(47)
	# print(f"fib(47) = {f.fib()}")
	time_numba = []
	time_fibpy = []
	time_fibc = []
	ns = [k for k in range(20, 31)]
	for n in ns:
		time_numba.append(time_fib(fib_numba, n))
		time_fibpy.append(time_fib(fib_py, n))
		f.setAge(n)
		start = pc()
		f.fib()
		end = pc()
		time_fibc.append(end - start)

	print(f"time fib numba: {time_numba}")
	print(f"time fib c++: {time_fibc}")
	print(f"time fib python: {time_fibpy}")


	fig, ax = plt.subplots()
	ax.plot(ns, time_fibc, linestyle='-', color='blue', label='fib c++')
	ax.plot(ns, time_numba, linestyle='--', color='green', label='fib numba')
	ax.plot(ns, time_fibpy, linestyle=':', color='red', label='fib py')

	plt.legend()
	ax.set(xlabel='n', ylabel='time fib')
	plt.savefig('fib.png')
	plt.close()


if __name__ == '__main__':
	main()
