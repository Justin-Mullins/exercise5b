'''

Exercise 5b

In addition to the functions of your solution from exercies 5a,
Handle punctuation—If a word ends with punctuation, then that punctuation
should be shifted to the end of the translated word.

'''

def pig_latin(word):
    first_letter = word[0]
    last = word[-1]
    if first_letter in 'aeiou':
        word += 'way'
    else:
        word = word[1:] + first_letter + 'ay'
    if first_letter.isupper():
        word = f'{word[0].upper()}{word[1:].lower()}'
    if last in '.!?,;':
        word = word.replace(last, '') + last
    return word
 
print(pig_latin('Computer'))
print(pig_latin('Python'))
print(pig_latin('arrow'))
print(pig_latin('Hello!'))