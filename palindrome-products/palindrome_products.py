def largest_palindrome(max_factor, min_factor=1):
    max_palindrome = 1
    factors = {}
    for i in range(min_factor, max_factor+1):
        for j in range(i, max_factor+1):
            product = i*j
            if is_palindrome(product):
                if product > max_palindrome:
                    max_palindrome = product
                    factors = {i,j}
    return max_palindrome,factors


def smallest_palindrome(max_factor, min_factor=1):
    min_palindrome = ""
    factors = {}
    for i in range(min_factor, max_factor+1):
        for j in range(i, max_factor+1):
            product = i*j
            if is_palindrome(product):
                if product < min_palindrome:
                    min_palindrome = product
                    factors = {i,j}
    return min_palindrome, factors


def is_palindrome(number):
    strnum = str(number)
    return "".join(list(reversed(strnum))) == strnum

if __name__ == "__main__":
    print is_palindrome(121)
    print is_palindrome(123)
