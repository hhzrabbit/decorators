import time

def name_arg( f ):
   def inner( *arg ):
      print "%s: %s" % (f.func_name, str(arg))
      return f( *arg )
   return inner

def timer( f ):
   def inner( *arg ):
      start = time.time()
      f( *arg )
      end = time.time()
      return "execution time: %s" % (end - start)
   return inner
   
@name_arg
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

@timer
def fib_timed(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
 
print "Fibonacci"
print "--"
print fib(4)
print fib_timed(4)
print "--"
print fib(5)
print fib_timed(5)
print "--"
print fib(6)
print fib_timed(6)
print "--"
print

@name_arg
def fact(n):
   if n == 1:
      return n
   return n * fact(n-1)

@timer
def fact_timed(n):
   if n == 1:
      return n
   return n * fact(n-1)

print "Factorial"
print "--"
print fact(3)
print fact_timed(3)
print "--"
print fact(4)
print fact_timed(4)
print "--"
print fact(5)
print fact_timed(5)
print "--"
print


