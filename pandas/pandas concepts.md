# PANDAS:

> pandas is a   powerfull  python  library thats used for data  manipulations  and data filtering and  data analysis its provides powerfull,expresssive data structure  to work with  structured data

> The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

**WHY WE SHOULD USE PANDAS :**

1. data manipulations
2. data cleaning :
   its a process of removing the unwanted data from the exiting collection are data set

### two type of data structure:

| series:                                                                                                      | data frame                                                                                            |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| its a one dimentional data  which is looking<br />like a soingle spred sheet column<br /> having index level | its a two dimentional data which is<br /> looking like full spred sheet having<br /> rows and columns |

### CREATE THE SERIES:

```
S=pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
S
```

output:

```
a    1
b    2
c    3
d    4
e    5
dtype: int64
```

## LABEL :

If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

This label can be used to access a specified value.

```
s=pd.Series([20,3,3,3,4,4])
s[2] # it will give the value of index 2
s[2:] # it will give the value of index 2 to 4


OUTPUT:
3
2    3
3    3
4    4
5    4
dtype: int64
```

## **INDEX:**

 To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

```
s=pd.Series([1,2,3,4,5],index=["rio","mani","vijay","sachin","dhoni"])
s

OUTPUT:

rio       1
mani      2
vijay     3
sachin    4
dhoni     5
dtype: int64

```

## NAME:

used to assign the name of the series like the table information should be given as the name using name keyword

```python
s=pd.Series([1,2,3,4,5],index=["rio","mani","vijay","sachin","dhoni"],name="cricket players ")
s

OUTPUT:
rio       1
mani      2
vijay     3
sachin    4
dhoni     5
Name: cricket players, dtype: int64

```


# Pandas Series Attributes -

## What is a Series Attribute?

An **attribute** is a property or characteristic of a Series object. Attributes provide information about the Series structure, data, and metadata. You access them using dot notation: `series.attribute_name`

---

## Important Series Attributes

### 1. **Index Attribute** (.index)

**Purpose**: Returns the index labels of the Series

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s.index)
# Output: Index(['a', 'b', 'c', 'd'], dtype='object')
```

**What it tells you**: The labels/positions associated with each value
**Use case**: When you need to work with or modify index labels

---

### 2. **Values Attribute** (.values)

**Purpose**: Returns the actual data values as a NumPy array

```python
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s.values)
# Output: [10 20 30 40]

print(type(s.values))
# Output: <class 'numpy.ndarray'>
```

**What it tells you**: The raw data without index information
**Use case**: When you need to perform NumPy operations or extract raw values

---

### 3. **dtype Attribute** (.dtype)

**Purpose**: Returns the data type of elements in the Series

```python
s1 = pd.Series([1, 2, 3, 4])
print(s1.dtype)
# Output: int64

s2 = pd.Series(['apple', 'banana', 'cherry'])
print(s2.dtype)
# Output: object

s3 = pd.Series([1.5, 2.5, 3.5])
print(s3.dtype)
# Output: float64
```

**What it tells you**: Whether data is integer, float, string, boolean, etc.
**Use case**: Data validation, ensuring correct data types for operations

---

### 4. **Name Attribute** (.name)

**Purpose**: Returns or sets the name of the Series

```python
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s.name)
# Output: None (default)

s.name = "Scores"
print(s.name)
# Output: Scores
```

**What it tells you**: The identifier name given to this Series
**Use case**: Labeling columns when creating DataFrames, for better organization

---

### 5. **Shape Attribute** (.shape)

**Purpose**: Returns the dimensions of the Series as a tuple

```python
s = pd.Series([10, 20, 30, 40, 50])
print(s.shape)
# Output: (5,)

# Series is 1-dimensional, so shape shows only one number
```

**What it tells you**: The number of elements/rows in the Series
**Use case**: Quick check on how many elements are in your Series

---

### 6. **Size Attribute** (.size)

**Purpose**: Returns the total number of elements in the Series

```python
s = pd.Series([10, 20, 30, 40, 50])
print(s.size)
# Output: 5
```

**What it tells you**: The total count of elements
**Use case**: Similar to shape, but returns a single integer instead of tuple

---

### 7. **Ndim Attribute** (.ndim)

**Purpose**: Returns the number of dimensions of the Series

```python
s = pd.Series([10, 20, 30])
print(s.ndim)
# Output: 1

# Series is always 1-dimensional
```

**What it tells you**: Whether it's 1D (Series) or 2D (DataFrame)
**Use case**: Type checking - distinguishing Series from DataFrame

---

### 8. **Hasnans Attribute** (.hasnans) - DEPRECATED

**Purpose**: Checks if Series contains any NaN values

```python
import numpy as np

s1 = pd.Series([1, 2, 3, 4])
print(s1.hasnans)
# Output: False

s2 = pd.Series([1, 2, np.nan, 4])
print(s2.hasnans)
# Output: True
```

**What it tells you**: Whether missing/null values exist
**Use case**: Data quality checks (though `isna().any()` is now preferred)

**Better alternative**:

```python
s2.isna().any()  # Returns True if any NaN exists
```

---

### 9. **Empty Attribute** (.empty)

**Purpose**: Returns True if the Series is empty (0 elements)

```python
s1 = pd.Series([1, 2, 3])
print(s1.empty)
# Output: False

s2 = pd.Series([])
print(s2.empty)
# Output: True
```

**What it tells you**: Whether the Series contains any data
**Use case**: Validation checks before processing

---

### 10. **Memory Usage Attribute** (.memory_usage())

**Purpose**: Returns memory usage of Series in bytes

```python
s = pd.Series([1, 2, 3, 4, 5])
print(s.memory_usage())
# Output: 40 (bytes) - typically includes index + data

print(s.memory_usage(deep=True))
# Output: More accurate count for object dtypes
```

**What it tells you**: How much RAM the Series is consuming
**Use case**: Performance optimization, memory monitoring

---

### 11. **Array Attribute** (.array)

**Purpose**: Returns the underlying array (ExtensionArray or NumPy array)

```python
s = pd.Series([10, 20, 30])
print(s.array)
# Output: [10, 20, 30]

print(type(s.array))
# Output: <class 'numpy.ndarray'>
```

**What it tells you**: The underlying array implementation
**Use case**: Advanced operations, compatibility checks

---

### 12. **Attrs Attribute** (.attrs)

**Purpose**: Dictionary to store arbitrary metadata about the Series

```python
s = pd.Series([10, 20, 30])
s.attrs['units'] = 'meters'
s.attrs['source'] = 'sensor_01'

print(s.attrs)
# Output: {'units': 'meters', 'source': 'sensor_01'}
```

**What it tells you**: Custom metadata you attach to the Series
**Use case**: Storing additional information about data origin, units, etc.

---

### 13. **Index Name Attribute** (.index.name)

**Purpose**: Returns or sets the name of the index

```python
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s.index.name)
# Output: None

s.index.name = "Categories"
print(s.index.name)
# Output: Categories
```

**What it tells you**: The label for the index column
**Use case**: Better documentation when converting to DataFrame

---

### 14. **Iloc & Loc Attributes**

**Purpose**: Access Series by position (iloc) or by label (loc)

```python
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# iloc - integer location based
print(s.iloc[0])  # Output: 10

# loc - label based
print(s.loc['b'])  # Output: 20
```

**What it tells you**: Alternative ways to access elements
**Use case**: Flexible data access methods

---

## Quick Reference Table

| Attribute           | Returns          | Example Use          |
| ------------------- | ---------------- | -------------------- |
| `.index`          | Index labels     | `s.index`          |
| `.values`         | NumPy array      | `s.values`         |
| `.dtype`          | Data type        | `s.dtype`          |
| `.name`           | Series name      | `s.name`           |
| `.shape`          | Dimensions tuple | `s.shape`          |
| `.size`           | Element count    | `s.size`           |
| `.ndim`           | Number of dims   | `s.ndim`           |
| `.empty`          | Is it empty?     | `s.empty`          |
| `.memory_usage()` | RAM bytes        | `s.memory_usage()` |
| `.array`          | Underlying array | `s.array`          |
| `.attrs`          | Metadata dict    | `s.attrs`          |
| `.index.name`     | Index name       | `s.index.name`     |

---

## Complete Practical Example

```python
import pandas as pd
import numpy as np

# Create a Series
sales = pd.Series(
    [100, 150, 200, 120, np.nan],
    index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    name='Daily Sales'
)

# Access various attributes
print("Series:")
print(sales)
print("\n--- ATTRIBUTES ---")
print(f"Index: {sales.index}")
print(f"Values: {sales.values}")
print(f"Data Type: {sales.dtype}")
print(f"Series Name: {sales.name}")
print(f"Shape: {sales.shape}")
print(f"Size: {sales.size}")
print(f"Dimensions: {sales.ndim}")
print(f"Is Empty: {sales.empty}")
print(f"Has NaN: {sales.isna().any()}")
print(f"Memory Usage: {sales.memory_usage()} bytes")

# Add metadata
sales.attrs['currency'] = 'USD'
sales.attrs['department'] = 'Sales'
print(f"Attributes: {sales.attrs}")
```
