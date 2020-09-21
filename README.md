# Session : 9

## Objective


- Write separate decorators that:
  - allows a function to run only on odd seconds - 100pts
  - log - 100pts
  -  authenticate - 300pts
  -  timed (n times) - 100pts
  -  Provides privilege access (has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params) - 200pts
- Write our htmlize code using inbuild singledispatch - 100pts


&nbsp;
``` html 
    logged,timed,check_odd_seconds,authenticate,htmlize,html_real,html_sequence
                            
                            
                          

```
&nbsp;
- Write a test file, that tests all of the functions mentioned above + the other basic ones 
- Test file must contain at least 1 tests for each function


---
&nbsp;
## Files
 - Test File : [PyTest file](https://github.com/Shakil-1501/Session9/blob/master/test_session9.py)
 - Code: [Method Implemantation](https://github.com/Shakil-1501/Session9/blob/master/session9.py)
 - colab File: [![a](https://github.com/jagatabhay/TSAI/blob/master/openincolablogo.JPG)](https://colab.research.google.com/drive/18aU2U-RO4w09l7RJYoCtJ0XVF5-xOjqv?usp=sharing)
&nbsp;
---
&nbsp;

## Functions
| Serial No  | Name | Functionality |
| ---------- | --------- | ------ |
| 1 | logged |The function takesin function as parameters and returns the sum of  two numbers|  
| 2 | check_odd_seconds | This function returns the sum of two numbers when there is odd seconds  |
| 3 | timed |The function takes in function as parameters and returns the average runtime and result of the function  |
| 4 | authenticate | The function takes in function.user password  as parameters and returns the results only if current password matches with user password |
|5| previlege | This decorator factory takens in previlege as input based on that provide access to 1,2,3 or 4 varaiables of Employee details of a comapny |

## Test Cases Results
| Serial No  | Test Case | Result |
| ---------- | --------- | ------ |
| 1 | README File Exists | Pass |
| 2 | RREADME Words Counts | Pass |
| 3 | README proper description | Pass |
| 4 | RREADME Formatting | Pass |
| 5 |test_htmlize_integral  | Pass |
| 6 | Function name not defined with capital letters | Pass |
| 7 | test_log | Pass |
| 8 | test_odd_seconds_func | Pass |
| 9 | test_timed | Pass |
| 10 | test_authentication | Pass | 
|11| test_previleges |Pass|

---

## Authors INFO
   
   Email : md.shakiluzzaman@gmail.com
   
   -[![](https://github.com/jagatabhay/TSAI/blob/master/logo.png)](https://www.linkedin.com/in/md-shakiluzzaman-894707129/)
