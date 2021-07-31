# Go School Test Assignment

Function for finding start and end indexes of a subarray containing 
the maximum possible sum of elements in array of integers.

1. Build
```
make build
```

2. Run with a list of integers separated by commas
```
make run 1,2,-3,4,-5
```

3. Clean 
```
make clean 
```

### Or

1. Import the function from `test_assignment` python package 
```
from test_assignment.main import findSubarrayWithMaxSum
```

2. Call it with a list of integers 
```
result = findSubarrayWithMaxSum([10, -3, -12, 8, 42, 1, -7, 0, 3])
print(result)
```
