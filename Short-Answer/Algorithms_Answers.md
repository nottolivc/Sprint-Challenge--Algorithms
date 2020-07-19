#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

given n what is the runtime of this?

The runtime it appears here is completely dependant on n, so it appears to be linear, O(n).

b)

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

given n what is the runtime of this?

This is a nested loop which appears would run in polynomial time, O(n^2) is th likely case here.

c)

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

given n what is the runtime of this?

This is a recursive function, the number of times it runs is based on the number of bunnies so it appears be O(bunnies) = O(n)

## Exercise II
