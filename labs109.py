def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust

def only_odd_digits(n):
    if n == 0:
        return False
    n_str = str(n)
    forbidden_digits = {'0', '2', '4', '6', '8'}
    for digit in n_str:
        if digit in forbidden_digits:
            return False
    return True


def is_cyclops(n):
    if n == 0:
        return True
    n = abs(n)
    if n < 10:
        return False
    
    num_digits = 0
    temp = n
    while temp > 0:
        num_digits += 1
        temp //= 10
    
    if num_digits % 2 == 0:
        return False
    
    middle_index = num_digits // 2
    temp = n
    for i in range(num_digits):
        if i == middle_index:
            if temp % 10 != 0:
                return False
        elif temp % 10 == 0:
            return False
        temp //= 10
    
    return True


def is_subsequence(small, large):
    it = iter(large)
    return all(char in it for char in small)
def words_with_letters(words, letters):
    result = [word for word in words if is_subsequence(letters, word)]
    return result
def read_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words
words = read_words('words_sorted.txt')
letters1 = 'klore'
letters2 = 'brohiic'
letters3 = 'azaz'
print(words_with_letters(words, letters1))
print(words_with_letters(words, letters2))
print(words_with_letters(words, letters3))



import math

def sum_of_two_squares(n):
    a = int(math.sqrt(n))
    b = 1
    max_pair = None
    
    while b <= a:
        sum_squares = a**2 + b**2
        if sum_squares == n:
            max_pair = (a, b)
            break
        elif sum_squares < n:
            b += 1
        else:
            a -= 1
    
    return max_pair

print(sum_of_two_squares(74))
print(sum_of_two_squares(85))
print(sum_of_two_squares(3))
print(sum_of_two_squares(25)) 




