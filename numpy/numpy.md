<<<<<<< HEAD
# NUMPY CONCEPTS :

# indexing :

## *2D array:*

> 0     1    2   4
>
> [[5 ,  48,  43,   4]--------------> oth row
>
> [40,   2 , 34 , 27]-------------> 1st row
>
> [38,  24 ,  20 , 19]----------->2 rd row

# SLICING:

* ITS process of extraccct the group of element in an ordered sequence

SYNTAX:

` VAR=[SART:END+-: STEP/UP]`

EXAMPLE :

0, 1,2,3,4.     indexes

[1,2,3,4,5]

arr[1:5:1] --------------o\p=====>2,3,4

**2D**-========>..`arr[row slicin: column slicing]`

```
arr4= np.array([
[5,48,43,4],
[40,2,34,27],
[38,24,20,19]
])

###[2,27,24,19]
arr4[1:3,1:4:2]    ###array([[ 2, 27],[24, 19]])
```

# 3d array:

`[layer:end:update, row sart: row end: row update , column start: column end: column update`

```

arr4=np.array([
  
    [[1,2,3,4],[2,4,5,6,]],
    [[4,3,6,8],[0,4,2,9]]]
)

arr4.ndim   ### 3     layer , rows , columns 



arr4[:,:,:2]
arr4[:,1:2,1:4:2

```





# MATH OPERATIONS  IN  NUMPY:

>     there are three types of operation we can perform an array:

1. inbuild functions
2. array to array operation
3. array with constent operation





### **2[i] .inbuild  operations  of an array:**

used to perform the mathamatical operations like 

1. max():
   max  will help user to find the maximum value from the array
2. min()
   it will return the minimum value from the array
   **syntax:**    np.min(variable)
3. abs():
   it will help users  to  make all of the negative values into positive value in the arry
   **syntax:**`np.abs(variable)`
4. size():
   it will help user to find the number of elements  of array
   **syntax:**   `np.size(variable)`
5. mean()  # avg
6. median() # mid
7. mod()
8. variance()
9. std()
10. sum,()
=======
# NUMPY CONCEPTS :

# indexing :

## *2D array:*

> 0     1    2   4
>
> [[5 ,  48,  43,   4]--------------> oth row
>
> [40,   2 , 34 , 27]-------------> 1st row
>
> [38,  24 ,  20 , 19]----------->2 rd row

# SLICING:

* ITS process of extraccct the group of element in an ordered sequence

SYNTAX:

` VAR=[SART:END+-: STEP/UP]`

EXAMPLE :

0, 1,2,3,4.     indexes

[1,2,3,4,5]

arr[1:5:1] --------------o\p=====>2,3,4

**2D**-========>..`arr[row slicin: column slicing]`

```
arr4= np.array([
[5,48,43,4],
[40,2,34,27],
[38,24,20,19]
])

###[2,27,24,19]
arr4[1:3,1:4:2]    ###array([[ 2, 27],[24, 19]])
```

# 3d array:

`[layer:end:update, row sart: row end: row update , column start: column end: column update`

```

arr4=np.array([
  
    [[1,2,3,4],[2,4,5,6,]],
    [[4,3,6,8],[0,4,2,9]]]
)

arr4.ndim   ### 3     layer , rows , columns 



arr4[:,:,:2]
arr4[:,1:2,1:4:2

```





# MATH OPERATIONS  IN  NUMPY:

>     there are three types of operation we can perform an array:

1. inbuild functions
2. array to array operation
3. array with constent operation





### **2[i] .inbuild  operations  of an array:**

used to perform the mathamatical operations like 

1. max():
   max  will help user to find the maximum value from the array
2. min()
   it will return the minimum value from the array
   **syntax:**    np.min(variable)
3. abs():
   it will help users  to  make all of the negative values into positive value in the arry
   **syntax:**`np.abs(variable)`
4. size():
   it will help user to find the number of elements  of array
   **syntax:**   `np.size(variable)`
5. mean()  # avg
6. median() # mid
7. mod()
8. variance()
9. std()
10. sum,()
>>>>>>> f384663b822d5c52dcf0e9c87b8287ec8b4412f9
