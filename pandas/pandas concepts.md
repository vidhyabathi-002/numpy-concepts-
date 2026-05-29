# PANDAS:

> pandas is a   powerfull  python  library thats used for data  manipulations  and data filtering and  data analysis its provides powerfull,expresssive data structure  to work with  structured data

> The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by **Wes McKinney in 2008.**

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

# AGGREGATION FUNCTION IN PANDAS

## What is an Aggregation Function?

An **aggregation function** is a function that combines or summarizes multiple values from a Series or DataFrame into a single value or set of values. These functions are used for:

- Calculating statistics (mean, sum, count, etc.)
- Grouping and summarizing data
- Finding unique values or frequencies
- Sorting data

Aggregation functions help reduce large datasets into meaningful summaries for analysis and decision-making.

---

## 1. **value_counts()**

### Concept:

`value_counts()` counts how many times each unique value appears in a Series. It returns the results sorted by frequency in descending order. This is also known as a **frequency counter**.

### Syntax:

```python
Series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)
```

### Parameters:

- `normalize`: If True, returns relative frequencies (proportions) instead of counts
- `sort`: If True, results are sorted by frequency (default: True)
- `ascending`: If True, sorts in ascending order (default: False)
- `dropna`: If True, ignores NaN values (default: True)

### Example:

```python
s = pd.Series([2000, 5000, 78521, 5554, 2004], index=["rio", "mani", "vijay", "sachin", "dhoni"])
print(s.value_counts())  # Count occurrences of each value

# Output:
# 5554     1
# 5000     1
# 2004     1
# 2000     1
# 78521    1
# dtype: int64

# With repeated values
s2 = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(s2.value_counts())
# Output:
# 4    4
# 3    3
# 2    2
# 1    1
# dtype: int64

# With normalization (proportions)
print(s2.value_counts(normalize=True))
# Output:
# 4    0.4
# 3    0.3
# 2    0.2
# 1    0.1
# dtype: float64
```

### Use Cases:

- Finding the most common element in a dataset
- Checking data distribution
- Data quality assessment (detecting duplicates)
- Exploratory data analysis (EDA)

---

## 2. **describe()**

### Concept:

`describe()` returns a statistical summary of a Series or DataFrame. For numerical data, it provides:

- count: Number of non-null values
- mean: Average value
- std: Standard deviation (measure of spread)
- min: Minimum value
- 25%: 1st quartile (25th percentile)
- 50%: Median (2nd quartile / 50th percentile)
- 75%: 3rd quartile (75th percentile)
- max: Maximum value

### Syntax:

```python
Series.describe(percentiles=None, include=None, exclude=None)
```

### Parameters:

- `percentiles`: Custom percentiles to calculate (e.g., [0.1, 0.5, 0.9])
- `include`: Data types to include (e.g., 'all', ['number'])
- `exclude`: Data types to exclude

### Example:

```python
s = pd.Series([2000, 5000, 78521, 5554, 2004], index=["rio", "mani", "vijay", "sachin", "dhoni"])
print(s.describe())

# Output:
# count        5.000000
# mean     18615.800000
# std      33885.949894
# min       2000.000000
# 25%       2004.000000
# 50%       5000.000000
# 75%       5554.000000
# max      78521.000000
# dtype: float64
```

### Use Cases:

- Quick statistical overview of numerical data
- Understanding data distribution
- Identifying outliers and anomalies
- Data profiling and reporting

---

## 3. **sort_values()**

### Concept:

`sort_values()` sorts the Series values in ascending or descending order. The index labels move with their corresponding values.

### Syntax:

```python
Series.sort_values(ascending=True, kind='quicksort', na_position='last')
```

### Parameters:

- `ascending`: If True, sorts in ascending order (default: True); False for descending
- `kind`: Sorting algorithm ('quicksort', 'mergesort', 'heapsort', 'stable')
- `na_position`: Where to place NaN values ('first' or 'last', default: 'last')

### Example:

```python
s = pd.Series([2000, 5000, 78521, 5554, 2004], index=["rio", "mani", "vijay", "sachin", "dhoni"])

# Ascending order (default)
print(s.sort_values(ascending=True))
# Output:
# rio      2000
# dhoni    2004
# mani     5000
# sachin   5554
# vijay   78521
# dtype: int64

# Descending order
print(s.sort_values(ascending=False))
# Output:
# vijay   78521
# sachin   5554
# mani     5000
# dhoni    2004
# rio      2000
# dtype: int64
```

### Use Cases:

- Ranking data
- Finding top or bottom values
- Organizing data for visualization
- Creating leaderboards or sorted lists

---

## 4. **unique()**

### Concept:

`unique()` returns an array of distinct (unique) values in the order they first appear. It removes duplicates while preserving the order of first occurrence.

### Syntax:

```python
Series.unique()
```

### Example:

```python
s = pd.Series([1, 2, 3, 3, 5], index=["rio", "mani", "vijay", "sachin", "dhoni"])

print(s.unique())
# Output: [1 2 3 5]

# Count unique values
print(s.nunique())
# Output: 4

# With string data
s2 = pd.Series(['apple', 'banana', 'apple', 'cherry', 'banana'])
print(s2.unique())
# Output: ['apple' 'banana' 'cherry']
```

### Related Method - **nunique()**:

Returns the count of unique values (excludes NaN by default)

### Use Cases:

- Finding distinct categories or values
- Data deduplication
- Understanding data variety
- Data quality checks

---

## 5. **sum()**

### Concept:

Returns the sum of all values in the Series. Skips NaN values by default.

### Syntax:

```python
Series.sum(skipna=True, level=None, numeric_only=None, min_count=0)
```

### Example:

```python
s = pd.Series([10, 20, 30, 40, 50])
print(s.sum())
# Output: 150

# With NaN values
s2 = pd.Series([10, 20, np.nan, 40])
print(s2.sum())  # Skips NaN
# Output: 70
```

---

## 6. **mean()**

### Concept:

Returns the average (arithmetic mean) of all values in the Series.

### Syntax:

```python
Series.mean(skipna=True, level=None, numeric_only=None)
```

### Example:

```python
s = pd.Series([10, 20, 30, 40, 50])
print(s.mean())
# Output: 30.0
```

---

## 7. **median()**

### Concept:

Returns the middle value when data is sorted. Less affected by outliers than mean.

### Example:

```python
s = pd.Series([10, 20, 30, 40, 50])
print(s.median())
# Output: 30.0

# With outlier
s2 = pd.Series([10, 20, 30, 40, 1000])
print(s2.median())
# Output: 30.0 (not affected by 1000)
```

---

## 8. **min() and max()**

### Concept:

`min()` returns the smallest value; `max()` returns the largest value.

### Example:

```python
s = pd.Series([10, 20, 30, 40, 50])
print(s.min())   # Output: 10
print(s.max())   # Output: 50
```

---

## 9. **count()**

### Concept:

Returns the number of non-null values in the Series.

### Example:

```python
s = pd.Series([10, 20, np.nan, 40, 50])
print(s.count())
# Output: 4 (excludes NaN)
```

---

## 10. **std() and var()**

### Concept:

- `std()`: Standard deviation (measure of data spread)
- `var()`: Variance (square of standard deviation)

### Example:

```python
s = pd.Series([10, 20, 30, 40, 50])
print(s.std())  # Output: 15.81... (standard deviation)
print(s.var())  # Output: 250.0 (variance)
```

---

## Comparison Table of Common Aggregation Functions

| Function           | Purpose                  | Returns    | Example       |
| ------------------ | ------------------------ | ---------- | ------------- |
| `sum()`          | Total of all values      | Single num | `150`       |
| `mean()`         | Average value            | Single num | `30.0`      |
| `median()`       | Middle value             | Single num | `30.0`      |
| `min()`          | Smallest value           | Single num | `10`        |
| `max()`          | Largest value            | Single num | `50`        |
| `count()`        | Count of non-null values | Single int | `4`         |
| `std()`          | Standard deviation       | Single num | `15.81...`  |
| `var()`          | Variance                 | Single num | `250.0`     |
| `value_counts()` | Frequency of each value  | Series     | Counts        |
| `describe()`     | Statistical summary      | Series     | Stats summary |
| `sort_values()`  | Sorted values            | Series     | Sorted series |
| `unique()`       | Distinct values only     | Array      | Unique values |
| `nunique()`      | Count of unique values   | Single int | `5`         |

---

## Complete Practical Example

```python
import pandas as pd
import numpy as np

# Sample data
sales = pd.Series(
    [100, 150, 200, 150, np.nan, 180, 150],
    index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    name='Daily Sales'
)

print("Series:")
print(sales)

print("\n--- AGGREGATION FUNCTIONS ---")
print(f"Sum: {sales.sum()}")
print(f"Mean: {sales.mean():.2f}")
print(f"Median: {sales.median()}")
print(f"Min: {sales.min()}")
print(f"Max: {sales.max()}")
print(f"Count: {sales.count()}")
print(f"Std Dev: {sales.std():.2f}")

print(f"\nValue Counts:\n{sales.value_counts()}")
print(f"\nDescribe:\n{sales.describe()}")
print(f"\nUnique Values: {sales.unique()}")
print(f"Number of Unique Values: {sales.nunique()}")
print(f"\nSorted (Descending):\n{sales.sort_values(ascending=False)}")
```

---

## Key Concepts to Remember

1. **Aggregation** = Combining multiple values into fewer values or statistics
2. **NaN Handling** = Most functions skip NaN values by default (skipna=True)
3. **Return Type** = Some return a single value, others return Series or arrays
4. **Performance** = Aggregation functions are optimized for speed on large datasets
5. **Use Cases** = Data exploration, reporting, and summary statistics





# MODIFICATION OF SERIES DATA:

to modified the data inside of the list we need to follow same notations  like list

**SYNTAX:**

**`VAR["INDEX"]="NEW VALUES STR  " OR INTEGER `**
