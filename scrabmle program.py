import random
import time
from colorama import init
from colorama import Fore, Back, Style
init()
start_time = time.time()

word = input("Please enter word")
word = (word.lower())
random_word_list = []
# initialise the random word list
for _ in word:
    random_word_list.append(chr(96 + random.randint(1, 26)))
    

print("".join(random_word_list))
# iterate over each letter of word
for index, letter in enumerate(word):
    # ...until we get the same letter in our random lis
    while random_word_list[index] != letter:
        new_random_letter = chr(96 + random.randint(1, 26))
        random_word_list[index] = new_random_letter
        if random_word_list[index] == letter:
            word_to_print = "".join(random_word_list)
            print(f"{Fore.MAGENTA + Style.BRIGHT}{word_to_print[:index+1]}{Style.RESET_ALL}{word_to_print[index+1:]}",Fore.CYAN + "          - identifed letter", random_word_list[index])
            time.sleep(0.0001)
        elif random_word_list[index] != letter:
            word_to_print = "".join(random_word_list)
            print(f"{Fore.MAGENTA + Style.BRIGHT}{word_to_print[:index]}{Fore.WHITE}{word_to_print[index:]}")
            time.sleep(0.0001)
print("word is", word)
end_time = time.time()
time_taken = (end_time - start_time)
print("It took",time_taken, "seconds to crack your word")
lol = input("press any key to exit")
