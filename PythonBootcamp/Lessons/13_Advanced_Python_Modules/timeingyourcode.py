
import timeit

print(",".join(str(n) for n in range(100)))


#generate n number

# check execution time
a = timeit.timeit(",".join(str(n) for n in range(100)),number=100000000)

print(a)

a = timeit.timeit(",".join([str(n) for n in range(100)]),number=100000000)

print(a) ## faster



#a= timeit.timeit('"-".join(map(str,range(100)))',number=100000000)
#print(a) ## faster

#%timeit ",".join([str(n) for n in range(100)])

