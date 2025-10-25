### Pallendrome logic

```py
1. number = 123 (dividend)
2. result = 0
3. originalNumber = number
4. digit  = number % 10 (remainder)
5. number = number // 10 (quotient)
6. result = result * 10 + digit
7. if number > 0 then
     6.1 go to 4
8. if originalNumber = result
     8.1 say Pallendrome
9. if originamNumber != result
     9.1 say not Pallendrome
```