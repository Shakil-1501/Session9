import pytest , os , inspect , re , random,session9
from decimal import Decimal
import math
import random


def test_log():
    #a = session9.logged(session9.summation)
    k= session9.summation(2,3)
    assert type(k) is int


def test_odd_seconds_func():
    a= session9.add(1,2)
    assert a== 3 or a==None


def test_timed():
    l= session9.fact(5)
    assert type(l) is int


def test_htmlize_integral():
    k=session9.htmlize(100)
    assert k == '100(<i>0x64</i>)'


def test_htmlize_Real():
    k=session9.htmlize(3.467)
    assert k == '3.47'


def test_authentication():
    #current_password=session9.set_password()
    #z=current_password()
    
    authen_t = session9.authenticate(session9.summation2,'secret')
    k=authen_t(1,2)
    assert k==3 


