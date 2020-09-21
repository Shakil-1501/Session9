import pytest , os , inspect , re , random,session9
from decimal import Decimal
import math
import random

README_CONTENT_CHECK_FOR = ['logged,timed,check_odd_seconds,authenticate,htmlize,html_real,html_sequence']


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


def test_privileges():
    l=session9.info1()
    m=session9.info2()
    n=session9.info3()
    o=session9.info4()
    assert type(l) is tuple and type(m) is tuple and type(n) is tuple and type(o) is str


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_funcation_had_cap_letter():
    functions = inspect.getmembers(session9, inspect.isfunction )
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_readme_words_counts():
    readme = open('README.md','r')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100 , "Kindly define README properly"


def test_readme_for_formatting():
    readme = open('README.md','r')
    content = readme.read()
    readme.close()
    assert content.count('#') >= 5 , "Kindly format the README.md"


def test_readme_proper_desscription():
    READMELOOKSGOOD = True
    readme = open('README.md','r')
    readme_words = readme.read().split()
    readme.close()
    for words in README_CONTENT_CHECK_FOR:
        if words not in readme_words:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True , "You have not defined all functions/classes in README.md"

