import timeit

def teste1():
	l = []
	for i in range(1000):
		l = l + [i]

def teste2():
	l = []
	for i in range(1000):
		l.append(i)
		
def teste3():
	l = [i for i in range(1000)]

def teste4():
	l = list(range(1000))

t1 = timeit.Timer("teste1()", "from __main__ import teste1")
print("concatenacao ", t1.timeit(number=1000), "milissegundos")
t2 = timeit.Timer("teste2()", "from __main__ import teste2")
print("append", t2.timeit(number=1000), "milissegundos")
t3 = timeit.Timer("teste3()", "from __main__ import teste3")
print("comprehension ", t3.timeit(number=1000), "milissegundos")
t4 = timeit.Timer("teste4()", "from __main__ import teste4")
print("range ", t4.timeit(number=1000), "milissegundos")