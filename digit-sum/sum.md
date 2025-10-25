### sum

1. number = 3456 (dividend)
2. result = 0
3. digit  = number % 10 (remainder)
4. number = number / 10 (quotient)
5. result = result + digit
6. if number > 0 then
     6.1 go to 3
7. if number > 9
    7.1 number = result
    7.2 result = 0
    7.3 go to 3
8. say result
