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

> there are three types of operation we can perform an array:

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
    ======

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

> there are three types of operation we can perform an array:

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

# 2[1[i]] Variance:

    in numpy`.var `its used to calculate the variance of array elements

##### SYNTAX:

```
import numpy as np

var = np.var(health_data)
print(var)
```

VARIANCE MESURES:

the spread  of data by calculating  the average of the squred value from the mean

### 1.Find the mean:

(80+85+90+95+100+105+110+115+120+125) / 10 = 102.5

The mean is 102.5

### 2. Find the difference from the mean for each value:

80 - 102.5 = -22.5
85 - 102.5 = -17.5
90 - 102.5 = -12.5
95 - 102.5 = -7.5
100 - 102.5 = -2.5
105 - 102.5 = 2.5
110 - 102.5 = 7.5
115 - 102.5 = 12.5
120 - 102.5 = 17.5
125 - 102.5 = 22.5


### 3.Find the square value for each difference:

(-22.5)^2 = 506.25
(-17.5)^2 = 306.25
(-12.5)^2 = 156.25
(-7.5)^2 = 56.25
(-2.5)^2 = 6.25
2.5^2 = 6.25
7.5^2 = 56.25
12.5^2 = 156.25
17.5^2 = 306.25
22.5^2 = 506.25

**Note:** We must square the values to get the total spread.

### Step 4: The Variance is the Average Number of These Squared Values

4. Sum the squared values and find the average:

(506.25 + 306.25 + 156.25 + 56.25 + 6.25 + 6.25 + 56.25 + 156.25 + 306.25 + 506.25) / 10 = 206.25

The variance is 206.25.


# 2[1[ii]] STANDED DEVATION:

* IN  numpy two calculate  standed devation we have to  use std()
* squre root of variance
* avg distance from the data points  ,
* `std = squre root (variance ) `
