from typing import List
import time
import sys
import weakref
import random
from math import tan, pi
from functools import singledispatch
from numbers import Real
from numbers import Integral
from collections.abc import Sequence
from html import escape
from datetime import datetime, timezone


def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f'{run_dt}: called {fn.__name__} ')
        print(f'The name of the function is {fn.__name__}')
        print(f'The docstring of the function is {fn.__doc__}')
        return result
    return inner


@logged
def summation(a,b):
  '''
  returns the summation of a and b
  '''
  return a+b


def check_odd_seconds(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now().second
        if run_dt%2!=0:

            result = fn(*args, **kwargs)
            print(f'{run_dt} th second: called {fn.__name__} ')
            return result
        else:
           return None   
    return inner


@check_odd_seconds
def add(a,b):
    '''
    returns addition of two numbers a and b
    '''
    return a+b


def timed(reps):
    def dec(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0

            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            avg_run_time = total_elapsed / reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
            return result
        return inner
    return dec


def calc_fact(n):
  return 1 if n < 2 else n * fact(n-1)


@timed(5)
def fact(n):
    #print(f'Calculating fact({n})')
    return calc_fact(n)


def set_password():
  password=''
  def inner():
      nonlocal password
      if password=='':
         password=input()
         return password
  return inner


#current_password=set_password()
#k=current_password()

def summation2(a,b):
    return a+b

def authenticate(fn,current_password,user_password):
  cnt=0
  if user_password == k:
     def inner(*args,**kwargs):
         nonlocal cnt
         cnt+=1
         #print(f'The function was called {cnt} times')
         return fn(*args,**kwargs)
     return inner
  else:
        print('You scamster!!')

@singledispatch
def htmlize(a):
    return escape(str(a))


@htmlize.register(Integral)
def htmlize_integral_numbers(a):
    return f'{a}(<i>{str(hex(a))}</i>)'

@htmlize.register(Real)
def html_real(a):
    return f'{round(a, 2)}'


def html_escape(arg):
    return escape(str(arg))



@htmlize.register(Sequence)
def html_sequence(d):
    if type(d)==str:
       return html_escape(d).replace('\n', '<br/>\n')
    if type(d)==tuple or type(d)==list:
       items = (f'<li>{html_escape(item)}</li>' for item in d)
       return '<ul>\n' + '\n'.join(items) + '\n</ul>'
    if type(d)==dict:
       items = (f'<li>{k}={v}</li>' for k, v in d.items())
       return '<ul>\n' + '\n'.join(items) + '\n</ul>'


