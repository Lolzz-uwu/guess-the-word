import random
import os
import platform
import time
def clearing():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
try:
    s = open('words.txt')
    s.close()
except Exception:
    print('please download the worlist')
def sex():
    global sex2
    global random_word
    global j
    with open('wordlist.txt') as file:
        o = []
        words = file.readlines()
        random_index = random.randrange(0,500)
        random_word = words[random_index]
        ss = list(random_word)
    word_length = len(random_word) -1
    first_pop = random.randrange(0,word_length)
    ss.pop(word_length)
    j = ''.join(ss)
    ss.pop(first_pop)
    ss.insert(first_pop,'_')
    sex2 = "".join(ss)
    print(f'[word]- "{sex2}"')    
clearing()
while True:
    clearing()
    
    print('''                             _   _                                  _ 
                            | | | |                                | |
  __ _ _   _  ___  ___ ___  | |_| |__   ___  __      _____  _ __ __| |
 / _` | | | |/ _ \/ __/ __| | __| '_ \ / _ \ \ \ /\ / / _ \| '__/ _` |
| (_| | |_| |  __/\__ \__ \ | |_| | | |  __/  \ V  V / (_) | | | (_| |
 \__, |\__,_|\___||___/___/  \__|_| |_|\___|   \_/\_/ \___/|_|  \__,_|
  __/ |                                                               
 |___/   ''')
    sex()
    us = input('[answer]-:')
    if us == j:
        print('you won!!')
        time.sleep(2)
        play_again = input('do u want to play again? y/n:')
        if play_again == 'n':
            print('thank you for playing')
            time.sleep(2)
            break
    else:
        p = input('try again:')
        if p == j:
            print('you won!!')
            time.sleep(2)
            play_again = input('do u want to play again? y/n:')
            if play_again == 'n':
                clearing()
                print('thank you for playing')
                time.sleep(2)
                break
        else:
            sex44 = input('try again:')
            if sex44 == j:
                print('you won!!')
                time.sleep(2)
                play_again = input('do u want to play again? y/n:')
                if play_again == 'n':
                    clearing()
                    print('thank you for playing')
                    time.sleep(2)
                    break
            else:
                print(f'you lost the word was {j}')
            play_again = input('do u want to play again? y/n:')
            if play_again == 'n':
                clearing()
                print('thank you for playing')
                time.sleep(2)
                break
