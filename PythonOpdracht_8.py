import click
import random
import string
import datetime
import os
import operator


alfabet = list("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")


print(f"De {len(alfabet)} letters van het alfabet zitten in mijn geheugen!")
print("Ik zal je telkens een letter geven en jij moet zo snel mogelijk de letter die ervoor en erna komt typen.")
print("Enter drukken is niet nodig.")
print("Druk op <SPATIE> om te beginnen. Een andere toets om te stoppen.")
print("Het spel eindigen kan op elk moment met het uitroepteken!")


if click.getchar() != ' ':
    exit()

print("Let's begin!")

user_c = '%'

while user_c != '!':
    guess_c_index = random.randint(1, len(alfabet)-2)
    time_start = datetime.datetime.now()
    print(f"Wat komt er voor {alfabet[guess_c_index]}")
    user_c_before = click.getchar()
    print(f"Wat komt er na {alfabet[guess_c_index]}")
    user_c_after = click.getchar()
    time_user = datetime.datetime.now() - time_start
    before_c = alfabet[guess_c_index-1]
    after_c = alfabet[guess_c_index+1]
    if not(before_c == user_c_before and after_c == user_c_after):
        print(
            f"Fout! Het juiste antwoord was {before_c} en {after_c}. Je tijd was {time_user}.")
    else:
        print(f"Corract. Je tijd was {time_user}.")