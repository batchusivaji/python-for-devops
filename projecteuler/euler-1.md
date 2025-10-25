### euler-1

https://projecteuler.net/problem=1

1. result = 0
2. index  = 2
3. sum    = 10
4. is_divisible = (index%3) or (index%5)
5. if is_divisible = True
    5.1 result = result + index
6. index = index + 1
7. if index < max
  7.1 go to 4
8. say result