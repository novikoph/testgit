number = 23
guess = int(input("Введите целове число: "))

if guess == number:
    print("Поздравляю, вы угадали,")
    print("хотя и не выиграли никакого приза")
elif guess < number:
    print("Нет, загаданное число больше этого.")
else:
    print("Нет, загаданное число меньше этого.")

print("Завершено")