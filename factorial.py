#!/usr/bin/python3.4
def factorial():
        n = int(input())

        if n < 0:
                raise ValueError('Invalid input.')

        result = 1
        while n > 1:
                result *= n
                n = n - 1

        print(result)

if __name__ == "__main__":
        import sys
        factorial()
