def wrapper( f ):
   def inner( *arg ):
       return f( *arg )
   return inner

def foo(a, b, c):
   return str(a * b) + c

closure = wrapper(foo)
print closure( -2, 3, 'hello' )
