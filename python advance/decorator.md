# DECORATOR:

its a function  and extern   its functionality and return the modifiyed function with externded  functionality

the main objective of the decorator  is for improving the  functionality of exiting function without changing the original function

**SYNTAX:**

```
def decorator function_name(arguments):     ##inputs 

          def outputfunction_name(arguments):
                    externded  function statement 
          return output function_name 
def  function_name(arguments):
          function statement block
function_name(argumrnts)
```



SYNTAX:

```
def fun_name(func):
    deff inner (*args **kwargs)
         print task
         fun(*args,*kwargs)
             print task
    return inner
  
```



* its used to add the some extra functionality  to the  exiting function withouyt modifiying  it  in the form of pre task and post task

## TYPES:

### 1.**inbuiltd decorator**:

the decorator which are predefine  by the developer   its know as the inbuiled decorator

example:        @static method , @class method  ,@abstractmethods

### 2.userdefined decorator:

this are the decorator which are the user based on the user requirement
