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


# Even the odds
def only_odd_digits(n):
    if n == 0:
        return False
    n_str = str(n)
    forbidden_digits = {'0', '2', '4', '6', '8'}
    for digit in n_str:
        if digit in forbidden_digits:
            return False
    return True


# Cyclops numbers
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


# Subsequent words
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


# Sum of two squares
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


# Expand Positive Integer Intervals
def expand_intervals(intervals):
    if not intervals:
        return []
    
    result = []
    parts = intervals.split(',')
    
    for part in parts:
        if '-' in part:
            start, end = map(int, part.split('-'))
            result.extend(range(start, end + 1))
        else:
            result.append(int(part))
    
    return result

# Test cases
print(expand_intervals('')) 
print(expand_intervals('42'))
print(expand_intervals('4-5'))  
print(expand_intervals('4-6,10-12,16')) 
print(expand_intervals('1,3-9,12-14,9999'))





# What do you hear, what do you say?
def count_and_say(digits):
    if not digits:
        return ''
    result = []
    count = 1
    current_digit = digits[0]
    for digit in digits[1:]:
        if digit == current_digit:
            count += 1
        else:
            result.append(f'{count}{current_digit}')
            current_digit = digit
            count = 1
    result.append(f'{count}{current_digit}')
    return ''.join(result)
print(count_and_say('333388822211177'))  
print(count_and_say('11221122'))         
print(count_and_say('123456789'))        
print(count_and_say('777777777777777'))  
print(count_and_say(''))                 
print(count_and_say('1'))


# Revorse the vewels
def reverse_vowels(text):
    vowels = 'aeiouAEIOU'
    vowels_in_text = [char for char in text if char in vowels]
    result = []
    for char in text:
        if char in vowels:
            reversed_vowel = vowels_in_text.pop()
            if char.isupper():
                result.append(reversed_vowel.upper())
            else:
                result.append(reversed_vowel.lower())
        else:
            result.append(char)
    return ''.join(result)
print(reverse_vowels('Bengt Hilgursson'))
print(reverse_vowels('Why do you laugh? I chose death.'))
print(reverse_vowels('These are the people you protect with your pain!')) 
print(reverse_vowels('We had to sacrifice a couple of miners to free Bolivia.')) 
print(reverse_vowels("Who's the leader of the club that's made for you and me? T-R-I-C-K-Y M-O-U-S-E! Tricky Mouse! TRICKY MOUSE! Tricky Mouse! TRICKY MOUSE! Forever let us hold our Hammers high! High! High! High!"))  
