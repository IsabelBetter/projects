import random
import time

word = input("Please enter the word you would like to crack:   ")
word = (word.lower())
random_word_list = []
# initialise the random word list
for _ in word:
    random_word_list.append(chr(96 + random.randint(1, 26)))

print("".join(random_word_list))
# iterate over each letter of word
for index, letter in enumerate(word):
    # ...until we get the same letter in our random list
    while random_word_list[index] != letter:
        new_random_letter = chr(96 + random.randint(1, 26))
        random_word_list[index] = new_random_letter
        print("".join(random_word_list))
        time.sleep(0.0001)
if random_word_list[index] == letter:
    print("cracked word is", word)
    endProgram = input("Please press any key to close this program")
