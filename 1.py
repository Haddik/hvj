from datetime import datetime
import random
import os
os.startfile("stat.txt")

number = random.randint(1, 100)
attempts = 0
start = datetime.now()

print("Угадай число от 1 до 100!")


while True:
    guess = int(input(" "))
    attempts += 1
    if number > guess:
        print("больше")
    else:
        print('меньше')

    if guess == number:
        time_spent = (datetime.now() - start).seconds
        print(f"Верно! Попыток: {attempts}, время: {time_spent} сек")
        
        with open("stat.txt", "a") as f:
            f.write(f"{datetime.now()} | Попыток: {attempts} | Время: {time_spent} сек\n")
        break
    
    print("Неверно!")

