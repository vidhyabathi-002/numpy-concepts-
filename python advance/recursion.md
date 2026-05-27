# RECURSION FUN()


# NON LOCAL FUNCTIONS:

`nonlocal b`

is a key word  whichn is used to modify any local variable  inside of the nested function and it is used to refer to the variable which is defined in the nearest enclosing scope which is not global scope

 CODE:

```
def a():
    b=10
    print (b)
    b=100
    print(b)
    def a():
        nonlocal b # is a key word  whichn is used to modify any local variable  inside of the nested function and it is used to refer to the variable which is defined in the nearest enclosing scope which is not global scope
        b=1000
        print(b)
    a()
    print(b)
a()
print(b)
```

```
 OUTPUT :

10100
1000
1000
```


# WHAT IS RECURSION:

DEF:       its a process  of calling the function by itsself untill the given  condition became true

NOTE   ADV :     by using recursion user can achive high eficiency by redusing the number of instructions

NOTE DISS  : the  drawback of recursion itis  taking  more memories inside of the system 


**SYNTAX:**

```
def function_name(args):
     if < condition >:-----
                           |----------------------->>TERMINATION CONDITION
          return value-----
      return fumction_name(args)-------------------->> CALLING SAME FUNCTION
function_name(args)
```


```plantuml
@startuml
title Factorial Recursion Detailed Tracing

skinparam backgroundColor white
skinparam handwritten false
skinparam shadowing false

box "MAIN STACK AREA"

participant "main()" as Main
participant "fact(3)\nAddress : 0x83" as F3
participant "fact(2)\nAddress : 0x82" as F2
participant "fact(1)\nAddress : 0x81" as F1

end box

box "METHOD AREA"

collections "fact(n)\nMethod Definition" as Method

note right of Method
Algorithm:

1. if(n==0 || n==1)
      return 1

2. else
      return n * fact(n-1)
end note

end box

== Program Starts ==

Main -> F3 : fact(3)

activate F3

note right of F3
n = 3

Check:
n==0 ? false
n==1 ? false

Execute:
3 * fact(2)
end note

F3 -> F2 : fact(2)

activate F2

note right of F2
n = 2

Check:
n==0 ? false
n==1 ? false

Execute:
2 * fact(1)
end note

F2 -> F1 : fact(1)

activate F1

note right of F1
n = 1

Condition True

return 1
end note

F1 --> F2 : 1

deactivate F1

note right of F2
return =
2 * 1

= 2
end note

F2 --> F3 : 2

deactivate F2

note right of F3
return =
3 * 2

= 6
end note

F3 --> Main : 6

deactivate F3

note right of Main
Final Output:
Factorial of 3 = 6
end note

@enduml
```





## STEPS OF RECURSION:

1. write the termination condition opposite to  looping condition  in the  form of if statement  and  return the specific value  inside of  termination conditions
2. after the finding the logic as  itis  excluding  updation of the looping variable should be done  inside of recursive  form
