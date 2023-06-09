### FIZZ BUZZ ###

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()

### ANAGRAMS ###

word1_test_a = ("Hello")
word2_test_a = ("Hello")

word1_test_b = ("Hello")
word2_test_b = ("One")

word1_test_c = ("State")
word2_test_c = ("Taste")

word1_test_d = ("word")
word2_test_d = 3

def anagrams(word1, word2):
    if type(word1) != str or type(word2) != str:
        return "That's not a word"
    elif word1.lower() == word2.lower():
        return "It's the same word, it's not an anagram"
    elif sorted(word2.lower()) == sorted(word1.lower()):
        return True
    else:
        return False

print(anagrams(word1_test_a, word2_test_a))
print(anagrams(word1_test_b, word2_test_b))
print(anagrams(word1_test_c, word2_test_c))
print(anagrams(word1_test_d, word2_test_d))

### FIBONACCI ###

def fibonacci():
    prev = 0
    next = 1

    for i in range(50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci()

### PRIME NUMBERS ###

def prime_numbers():
    for number in range (1, 101):
        if number >= 2:
            is_divisible = False
            for i in range (2, number):
                if number % i == 0:
                    is_divisible = True
            if not is_divisible:
                print(number)

prime_numbers()

### REVERSE TEXT ###

def reverse(text):
    reversed_text = ""
    for i in text[ : :-1]:
        reversed_text += i
    print(reversed_text)

reverse("Hello, World!")