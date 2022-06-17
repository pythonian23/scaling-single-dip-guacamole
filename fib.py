# Recurse for a fibonacci sequence
_fib = lambda x, y, rem: _fib(y, x+y, rem-1) if rem != 1 else x; fib = lambda lim: _fib(1,1,lim)
