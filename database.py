import random
from datetime import datetime

today = datetime.now()
ran = random.randint(1, 1000)
def main():
    cho = input("(Регистрация: 1, Авторизация: 2, Посмотреть список входов в уч.запись: 3): ")
    if cho == "1":
        whatname = str(input("Введите своё имя: "))
        password = input("Придумайте свой пароль: ")
        result = whatname.split()
        FILENAME = result[0] + str(ran) + ".txt"
        with open(FILENAME, "w") as file:
            file.write("Name:\n" + whatname + "\n" + "Password:\n" + password)
            print("Запомните эти цифры: " + str(ran) + ", они пригодятся вам в дальнейшем для востановления пароля")
    elif cho == "2":
        login = input("Введите своё имя: ")
        print("Если забыли пароль то введите цифру 1.")
        password1 = input("Введите свой пароль: ")
        if password1 == "1":
            lognum = int(input("Введите цифры которые вам выдавали при регистрации: "))

            FILENAME1 = (login + str(lognum) + ".txt")
            with open(FILENAME1, "r") as file:
                userinfo = file.readlines()
                userpass = userinfo[3]
                print("Ваш пароль: " + userpass)

        else:
            lognum1 = int(input("Введите цифры которые вам выдавали при регистрации: "))
            lognum1 = str(lognum1).strip()
            login = login.strip()
            FILENAME2 = (login + lognum1 + ".txt")
            with open(FILENAME2, "r") as file:
                userinfo1 = file.readlines()
                userpass1 = userinfo1[3]

                if password1 == userpass1:
                    print("Вход выполнен")

                    with open(FILENAME2, "a") as file:
                        file.write("\nВход в уч.запись: " + str(today) + "\n")
                else:
                    print("Неверно введённые данные")

    elif cho == "3":
        logname = input("Введите своё имя: ")
        lognum2 = int(input("Введите цифры которые вам выдавали при регистрации: "))
        lognum2 = str(lognum2).strip()
        FILENAME3 = (logname + lognum2 + ".txt")
        with open(FILENAME3, "r") as file:
            userlog = file.readlines()
            userauth = userlog[-1]
            print(userauth)

main()                                                                              
