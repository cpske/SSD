"""
Function decorator (memoize) that provides a cache of previously
computed function values.

Use fibonacci as an example to see how much the function cache
speeds up the results.
Run main and try computing fibonacci(35) or fibonacci(40) in 2 cases:
  a) original fibonacci
  b) with @memoize decorator
"""


def memoize(func):
    """A function decorator that caches results for given parameter values.
    The cache is keyed on positional parameters (*args) only.
    """
    # a cache that maps parameter values -> results
    # the first time a new set of parameter values is seen,
    # it is added to the cache.
    func.cache = {}

    def memoized_func(*args):
        # if the args have already been seen, simply return the result.
        if args in func.cache:
            return func.cache[args]
        # otherwise, call the function, add the result to the cache,
        # and then return the result.

        # TODO
        result = func(*args)
        func.cache[args] = result
        return result
    return memoized_func



@memoize
def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number, where fibonacci(0) is 0,
    fibonacci(1) is 1.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    while True:
        n = input("Fibonacci index? ").strip()
        if n == '':  break
        n = int(n)
        print(f"F({n}) =", fibonacci(n))
