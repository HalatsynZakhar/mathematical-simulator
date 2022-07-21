from tkinter import *
from random import choice, randint



win1 = Tk()
win1.title("Математика, 6 класс, тренировочная программа")
win1.geometry("610x325")

textWarning=Label(win1,text= "" ,font = "Arial 10", bg="lightyellow",fg="Black", height=20, width=80)
textWarning.place(x=0,y=0)

def func1():
    lab1 = Label(win1, text="Минимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab1.place(x=0, y=50)
    input1 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input1.place(x=150, y=50)

    lab2 = Label(win1, text="Максимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab2.place(x=0, y=75)
    input2 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input2.place(x=150, y=75)


    def start1():
        a=int(input1.get())
        b=int(input2.get())

        arr = [i for i in range(a, b + 1)]

        x = choice(arr)
        y = choice(arr)

        lab4 = Label(win1, text="{} * {} = ".format(x, y), font="Arial 10", bg="lightyellow", height=10, width=75)
        lab4.place(x=0, y=160)
        input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
        input4.place(x=150, y=160)
        def start2():
            z = int(input4.get())
            if z == int(x * y):
                lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                         bg="green", height=1, width=20)
                lab5.place(x=300, y=160)
            else:
                lab5 = Label(win1, text="Правильна ответ: " + str(x * y), font="Arial 10",
                                         bg="lightsalmon", height=1, width=20)
                lab5.place(x=300, y=160)
        but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                   activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
        but9.place(x=220, y=160)

    but8 = Button(win1, text="Генерировать задачу", bg="saddlebrown", fg="white", activebackground="white",
               activeforeground="black", width=23, height=1,  command=start1, font=("Arial", 8))
    but8.place(x=0, y=100)


def func2():
    lab1 = Label(win1, text="Минимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab1.place(x=0, y=50)
    input1 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input1.place(x=150, y=50)

    lab2 = Label(win1, text="Максимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab2.place(x=0, y=75)
    input2 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input2.place(x=150, y=75)


    def start1():
        a=int(input1.get())
        b=int(input2.get())

        arr = [i for i in range(a, b + 1)]

        x = choice(arr)
        y = choice(arr)

        lab4 = Label(win1, text="{} / {} = ".format(x*y, y), font="Arial 10", bg="lightyellow", height=10, width=75)
        lab4.place(x=0, y=160)
        input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
        input4.place(x=150, y=160)
        def start2():
            z = int(input4.get())
            if z == int(x):
                lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                         bg="green", height=1, width=20)
                lab5.place(x=300, y=160)
            else:
                lab5 = Label(win1, text="Правильна ответ: " + str(x), font="Arial 10",
                                         bg="lightsalmon", height=1, width=20)
                lab5.place(x=300, y=160)
        but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                   activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
        but9.place(x=220, y=160)

    but8 = Button(win1, text="Генерировать задачу", bg="saddlebrown", fg="white", activebackground="white",
               activeforeground="black", width=23, height=1,  command=start1, font=("Arial", 8))
    but8.place(x=0, y=100)

def func3():
    lab1 = Label(win1, text="Минимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab1.place(x=0, y=50)
    input1 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input1.place(x=150, y=50)

    lab2 = Label(win1, text="Максимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab2.place(x=0, y=75)
    input2 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input2.place(x=150, y=75)


    def start1():

        a=int(input1.get())
        b=int(input2.get())

        arr = [i for i in range(a, b + 1)]

        x = choice(arr)
        y = choice(arr)

        lab4 = Label(win1, text="НСД: {} и {} = ".format(x, y), font="Arial 10", bg="lightyellow", height=10, width=75)
        lab4.place(x=0, y=160)
        input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
        input4.place(x=150, y=160)
        def start2():
            def NSD(a, b):
                while a != 0 and b != 0:
                    if a > b:
                        a %= b
                    else:
                        b %= a
                return (a + b)
            z = int(input4.get())
            if z == int(NSD(x,y)):
                lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                         bg="green", height=1, width=20)
                lab5.place(x=300, y=160)
            else:
                lab5 = Label(win1, text="Правильна ответ: " + str(NSD(x,y)), font="Arial 10",
                                         bg="lightsalmon", height=1, width=20)
                lab5.place(x=300, y=160)
        but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                   activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
        but9.place(x=220, y=160)

    but8 = Button(win1, text="Генерировать задачу", bg="saddlebrown", fg="white", activebackground="white",
               activeforeground="black", width=23, height=1,  command=start1, font=("Arial", 8))
    but8.place(x=0, y=100)
def func4():
    lab1 = Label(win1, text="Минимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab1.place(x=0, y=50)
    input1 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input1.place(x=150, y=50)

    lab2 = Label(win1, text="Максимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab2.place(x=0, y=75)
    input2 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input2.place(x=150, y=75)


    def start1():

        a=int(input1.get())
        b=int(input2.get())

        arr = [i for i in range(a, b + 1)]

        x = choice(arr)
        y = choice(arr)

        lab4 = Label(win1, text="НСК: {} и {} = ".format(x, y), font="Arial 10", bg="lightyellow", height=10, width=75)
        lab4.place(x=0, y=160)
        input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
        input4.place(x=150, y=160)
        def start2():
            def NSD(a, b):
                while a != 0 and b != 0:
                    if a > b:
                        a %= b
                    else:
                        b %= a
                return (a + b)
            def NSK(a, b):
                return int((a * b) / NSD(a, b))
            z = int(input4.get())
            if z == int(NSK(x,y)):
                lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                         bg="green", height=1, width=20)
                lab5.place(x=300, y=160)
            else:
                lab5 = Label(win1, text="Правильна ответ: " + str(NSK(x,y)), font="Arial 10",
                                         bg="lightsalmon", height=1, width=20)
                lab5.place(x=300, y=160)
        but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                   activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
        but9.place(x=220, y=160)

    but8 = Button(win1, text="Генерировать задачу", bg="saddlebrown", fg="white", activebackground="white",
               activeforeground="black", width=23, height=1,  command=start1, font=("Arial", 8))
    but8.place(x=0, y=100)
def func5():
    lab1 = Label(win1, text="Минимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab1.place(x=0, y=50)
    input1 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input1.place(x=150, y=50)

    lab2 = Label(win1, text="Максимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab2.place(x=0, y=75)
    input2 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input2.place(x=150, y=75)


    def start1():

        a=int(input1.get())
        b=int(input2.get())

        arr = [i for i in range(a, b + 1)]

        x = choice(arr)
        y = choice(arr)
        z = choice(arr)

        if x % 4 == 0:
            lab4 = Label(win1, text="{} кг товару коштує \n{} грн. Скільки коштує {} кг?".format(x, y, z), font="Arial 10", bg="lightyellow", height=10, width=75)
            lab4.place(x=0, y=160)
            input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
            input4.place(x=150, y=160)
            def start2():
                z = float(input4.get())
                if z == round((z*y)/x,3):
                    lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                             bg="green", height=1, width=20)
                    lab5.place(x=300, y=160)
                else:
                    lab5 = Label(win1, text="Правильна ответ: {}".format(round((z*y)/x,3)), font="Arial 10",
                                             bg="lightsalmon", height=1, width=20)
                    lab5.place(x=300, y=160)
            but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                       activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
            but9.place(x=220, y=160)

        if x % 4 == 1:
            lab4 = Label(win1, text="{} кг товару коштує\n {} грн. Скільки\nможна купити товару на {} грн?".format(x, y, z), font="Arial 10", bg="lightyellow", height=10, width=75)
            lab4.place(x=0, y=160)
            input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
            input4.place(x=150, y=160)
            def start2():
                z = float(input4.get())
                if z == round((x*z)/y,3):
                    lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                             bg="green", height=1, width=20)
                    lab5.place(x=300, y=160)
                else:
                    lab5 = Label(win1, text="Правильна ответ: {}".format(round((x*z)/y,3)), font="Arial 10",
                                             bg="lightsalmon", height=1, width=20)
                    lab5.place(x=300, y=160)
            but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                       activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
            but9.place(x=220, y=160)

        if x % 4 == 2:
            lab4 = Label(win1, text="Скільки коштів\nнеобхідно для покупки\n {} кг, якщо вартість {} кг коштує {} грн?".format(x, y, z), font="Arial 10", bg="lightyellow", height=10, width=75)
            lab4.place(x=0, y=160)
            input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
            input4.place(x=150, y=160)
            def start2():
                z = float(input4.get())
                if z == round((x*z)/y,3):
                    lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                             bg="green", height=1, width=20)
                    lab5.place(x=300, y=160)
                else:
                    lab5 = Label(win1, text="Правильна ответ: {}".format(round((x*z)/y,3)), font="Arial 10",
                                             bg="lightsalmon", height=1, width=20)
                    lab5.place(x=300, y=160)
            but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                       activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
            but9.place(x=220, y=160)

        if x % 4 == 3:
            lab4 = Label(win1, text="Скільки можна купити\nкг товару на {} грн,\n якщо вартість {} кг коштує {} грн?".format(x, y, z), font="Arial 10", bg="lightyellow", height=10, width=75)
            lab4.place(x=0, y=160)
            input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
            input4.place(x=150, y=160)
            def start2():
                z = float(input4.get())
                if z == round((y*x)/z,3):
                    lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                             bg="green", height=1, width=20)
                    lab5.place(x=300, y=160)
                else:
                    lab5 = Label(win1, text="Правильна ответ: {}".format(round((y*x)/z,3)), font="Arial 10",
                                             bg="lightsalmon", height=1, width=20)
                    lab5.place(x=300, y=160)
            but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                       activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
            but9.place(x=220, y=160)

    but8 = Button(win1, text="Генерировать задачу", bg="saddlebrown", fg="white", activebackground="white",
               activeforeground="black", width=23, height=1,  command=start1, font=("Arial", 8))
    but8.place(x=0, y=100)
def func6():
    lab1 = Label(win1, text="Минимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab1.place(x=0, y=50)
    input1 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input1.place(x=150, y=50)

    lab2 = Label(win1, text="Максимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab2.place(x=0, y=75)
    input2 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input2.place(x=150, y=75)


    def start1():
        a=int(input1.get())
        b=int(input2.get())

        arr = [i for i in range(a, b + 1)]
        arr_k = [i for i in range(-10, 11)]
        arr_k.remove(0)

        x = choice(arr)
        y = choice(arr)
        z = choice(arr)
        u = choice(arr)
        v = choice(arr)
        w = choice(arr)
        k1 = choice(arr_k)
        k2 = choice(arr)
        k3 = choice(arr)

        lab4 = Label(win1, text="{}({}x{:+}){:+}({}-{}x)={}({}x+{})".format(k1, x, y, k2, z, u, k3, v, w), font="Arial 10", bg="lightyellow", height=10, width=75)
        lab4.place(x=0, y=160)
        input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
        input4.place(x=150, y=160)
        def start2():
            z = float(input4.get())
            if z == round((k3*w-k1*y-k2*z)/(k1*x-k2*u-k3*v), 3):
                lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                         bg="green", height=1, width=20)
                lab5.place(x=300, y=160)
            else:
                lab5 = Label(win1, text="Правильна ответ: {}".format(round((k3*w-k1*y-k2*z)/(k1*x-k2*u-k3*v), 3)), font="Arial 10",
                                         bg="lightsalmon", height=1, width=20)
                lab5.place(x=300, y=160)
        but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                   activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
        but9.place(x=220, y=160)

    but8 = Button(win1, text="Генерировать задачу", bg="saddlebrown", fg="white", activebackground="white",
               activeforeground="black", width=23, height=1,  command=start1, font=("Arial", 8))
    but8.place(x=0, y=100)
def func7():
    lab1 = Label(win1, text="Минимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab1.place(x=0, y=50)
    input1 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input1.place(x=150, y=50)

    lab2 = Label(win1, text="Максимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab2.place(x=0, y=75)
    input2 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input2.place(x=150, y=75)


    def start1():
        a=int(input1.get())
        b=int(input2.get())

        arr = [i for i in range(a, b + 1)]
        arr_k = [i for i in range(-10, 11)]
        arr_k.remove(0)
        char=["+", "-"]
        char1=["×", ":"]
        ch1 = choice(char)
        ch2 = choice(char)
        ch3 = choice(char1)
        r1 = choice(arr);
        r2 = choice(arr);
        r3 = choice(arr);
        r4 = choice(arr)
        k5 = int(choice(arr) / 2);
        k6 = int(choice(arr) / 2);
        k7 = int(choice(arr) / 2);
        k8 = int(choice(arr) / 2)
        k1 = r1 * choice(arr);
        k9 = r1 * choice(arr)
        k2 = r2 * choice(arr);
        k10 = r2 * choice(arr)
        k3 = r3 * choice(arr);
        k11 = r3 * choice(arr)
        k4 = r4 * choice(arr);
        k12 = r4 * choice(arr)

        lab4 = Label(win1, text="   {:>2}         {:>2}     /    {:>2}        {:>2}  \\".format(k1,k2, k3,k4) +
                                "\n{:>2} ----  {} {:>2} ---- {} | {:>2} ---- {} {:>2} ----  |".format(k5, ch1, k6, ch3, k7, ch2 ,k8) +
                                "\n   {:>2}         {:>2}     \    {:>2}        {:>2}  /".format(k9,k10, k11,k12), font="Arial 10", bg="lightyellow", height=10, width=75)
        lab4.place(x=0, y=160)
        input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
        input4.place(x=150, y=160)
        def start2():
            A=(k5*k9+k1)/k9
            B=(k6*k10+k2)/k10
            C=(k7*k11+k3)/k11
            D=(k8*k12+k4)/k12
            if ch1=="-":
                if ch2=="-":
                    if ch3==":":
                        res=A-B/(C-D)
                    else:
                        res=A-B*(C-D)
                else:
                    if ch3==":":
                        res=A-B/(C+D)
                    else:
                        res=A-B*(C+D)
            else:
                if ch2=="-":
                    if ch3==":":
                        res=A+B/(C-D)
                    else:
                        res=A+B*(C-D)
                else:
                    if ch3==":":
                        res=A+B/(C+D)
                    else:
                        res=A+B*(C+D)
            result=("{} ".format(round(res,3)))
            z = float(input4.get())
            if z == round(res,3):
                lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                         bg="green", height=1, width=20)
                lab5.place(x=330, y=160)
            else:
                lab5 = Label(win1, text="Правильна ответ: {}".format(round(res,3)), font="Arial 10",
                                         bg="lightsalmon", height=1, width=20)
                lab5.place(x=330, y=160)
        but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                   activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
        but9.place(x=220, y=160)

    but8 = Button(win1, text="Генерировать задачу", bg="saddlebrown", fg="white", activebackground="white",
               activeforeground="black", width=23, height=1,  command=start1, font=("Arial", 8))
    but8.place(x=0, y=100)
def func8():
    lab1 = Label(win1, text="Минимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab1.place(x=0, y=50)
    input1 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input1.place(x=150, y=50)

    lab2 = Label(win1, text="Максимальное число: ", font="Arial 10", bg="lightyellow", height=1, width=20)
    lab2.place(x=0, y=75)
    input2 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
    input2.place(x=150, y=75)


    def start1():
        a=int(input1.get())
        b=int(input2.get())
        arr = [i for i in range(a, b + 1)]
        r = randint(0, 100)
        x = choice(arr);
        y = choice(arr);
        t = choice(arr)
        if r % 8 == 0:
            lab4 = Label(win1, text="В першому бідоні молока в {}\n"
                                    "рази/разів більше, ніж в другому.\n Коли з першого бідона перелили\n"
                                    "в другий {} літрів, молока в \nбідонах стало порівну. Скільки літрів\n"
                                    "молока було в другому бідоні спочатку?".format(x,y), font="Arial 10", bg="lightyellow", height=10, width=75)
            lab4.place(x=0, y=160)
            input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
            input4.place(x=150, y=160)
            def start2():
                z = float(input4.get())
                if z == round((2*y)/(x-1), 3):
                    lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                             bg="green", height=1, width=20)
                    lab5.place(x=330, y=160)
                else:
                    lab5 = Label(win1, text="Правильна ответ: {}".format(round((2*y)/(x-1), 3)), font="Arial 10",
                                             bg="lightsalmon", height=1, width=20)
                    lab5.place(x=330, y=160)
            but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                       activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
            but9.place(x=220, y=160)

        if r % 8 == 1:
            lab4 = Label(win1, text="Автобус і легкова машина, швидкість якої на {} км/год\n"
                                    " більше швидкості автобуса, виїхали одночасно\n"
                      "назустріч один одному з двох міст, \n"
                                    "відстань між якими - {} км.\n"
                                    "Визнач швидкості автобуса, якщо відомо, що"
                                    "\nвони зустрілися через {} ч. Після виїзду".format(x*5,y*50,t), font="Arial 10", bg="lightyellow", height=10, width=75)
            lab4.place(x=0, y=160)
            input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
            input4.place(x=150, y=160)
            def start2():
                z = float(input4.get())
                if z == round(((y*50/t)-x*5)/2, 3):
                    lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                             bg="green", height=1, width=20)
                    lab5.place(x=330, y=160)
                else:
                    lab5 = Label(win1, text="Правильна ответ: {}".format(round(((y*50/t)-x*5)/2, 3)), font="Arial 10",
                                             bg="lightsalmon", height=1, width=20)
                    lab5.place(x=330, y=160)
            but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                       activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
            but9.place(x=220, y=160)

        if r % 8 == 2:
            lab4 = Label(win1, text="У двох братів порівну кг цукерок.\nЯкщо старший брат віддасть молодшому {} кг цукерок\n"
                                    ", то у нього стане в {} рази(ів) менше, \n"
                                    "ніж у молодшого. Скільки кг цукерок було у старшого брата спочатку?".format(x,y), font="Arial 10", bg="lightyellow", height=10, width=75)
            lab4.place(x=0, y=160)
            input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
            input4.place(x=150, y=160)
            def start2():
                z = float(input4.get())
                if z == round((x*(y+1)/(y-1)), 3):
                    lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                             bg="green", height=1, width=20)
                    lab5.place(x=330, y=160)
                else:
                    lab5 = Label(win1, text="Правильна ответ: {}".format(round((x*(y+1)/(y-1)), 3)), font="Arial 10",
                                             bg="lightsalmon", height=1, width=20)
                    lab5.place(x=330, y=160)
            but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                       activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
            but9.place(x=220, y=160)

        if r % 8 == 3:
            lab4 = Label(win1, text="У трьох посудинах з рідиною {} літрів. \nКількість літрів в першій посудині \n"
                                    "становить {}% літрів в другій посудині, \nа в третій ємкості в {} разів більше літрів, ніж у першому.\n"
                       "Скільки літрів поміщається в першій посудині?".format(x * 10, y * 10, t), font="Arial 10", bg="lightyellow", height=10, width=75)
            lab4.place(x=0, y=160)
            input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
            input4.place(x=150, y=160)
            def start2():
                z = float(input4.get())
                if z == round((x*10 / ( (y/10) + 1 + t))*(y/10), 3):
                    lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                             bg="green", height=1, width=20)
                    lab5.place(x=330, y=160)
                else:
                    lab5 = Label(win1, text="Правильна ответ: {}".format(round((x*10 / ( (y/10) + 1 + t))*(y/10), 3)), font="Arial 10",
                                             bg="lightsalmon", height=1, width=20)
                    lab5.place(x=330, y=160)
            but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                       activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
            but9.place(x=220, y=160)

        if r % 8 == 4:
            lab4 = Label(win1, text="Скільки відсотків число {} становить\nвід числа, яке є його квадратом?".format (x), font="Arial 10", bg="lightyellow", height=10, width=75)
            lab4.place(x=0, y=160)
            input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
            input4.place(x=150, y=160)
            def start2():
                z = float(input4.get())
                if z == round(1/x*100, 3):
                    lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                             bg="green", height=1, width=20)
                    lab5.place(x=330, y=160)
                else:
                    lab5 = Label(win1, text="Правильна ответ: {}".format(round(1/x*100, 3)), font="Arial 10",
                                             bg="lightsalmon", height=1, width=20)
                    lab5.place(x=330, y=160)
            but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                       activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
            but9.place(x=220, y=160)

        if r % 8 == 5:
            lab4 = Label(win1, text="Деяке число спочатку збільшили на {}%, \nа потім результат зменшили на {}%.\nУстановіть, на "
                       "скільки відсотків отримане число\nвідрізняється від початкового?".format (x, y ), font="Arial 10", bg="lightyellow", height=10, width=75)
            lab4.place(x=0, y=160)
            input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
            input4.place(x=150, y=160)
            def start2():
                z = float(input4.get())
                if z == round(abs(((1-(x/100+1)*(1-y/100)))*100), 3):
                    lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                             bg="green", height=1, width=20)
                    lab5.place(x=330, y=160)
                else:
                    lab5 = Label(win1, text="Правильна ответ: {}".format(round(abs(((1-(x/100+1)*(1-y/100)))*100), 3)), font="Arial 10",
                                             bg="lightsalmon", height=1, width=20)
                    lab5.place(x=330, y=160)
            but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                       activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
            but9.place(x=220, y=160)

        if r % 8 == 6:
            lab4 = Label(win1, text="Євген узяв {} частину цукерок,\nа Катруся - {} частину решти, після чого\nв коробці залишилось "
                       "{} г цукерок.\nСкільки г цукерок було в коробці спочатку?".format (x, y, t*10), font="Arial 10", bg="lightyellow", height=10, width=75)
            lab4.place(x=0, y=160)
            input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
            input4.place(x=150, y=160)
            def start2():
                z = float(input4.get())
                if z == round(t*10/((1-1/y)*(1-1/x)), 3):
                    lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                             bg="green", height=1, width=20)
                    lab5.place(x=330, y=160)
                else:
                    lab5 = Label(win1, text="Правильна ответ: {}".format(round(t*10/((1-1/y)*(1-1/x)), 3)), font="Arial 10",
                                             bg="lightsalmon", height=1, width=20)
                    lab5.place(x=330, y=160)
            but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                       activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
            but9.place(x=220, y=160)

        if r % 8 == 7:
            lab4 = Label(win1, text="Двоцифрове число, перва цифра якого {},\n поділили на одноцифрове й отримали остачу {}.\n"
                           "Знайти це двоцифрове число.".format (x, y), font="Arial 10", bg="lightyellow", height=10, width=50)
            lab4.place(x=0, y=160)
            input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
            input4.place(x=150, y=160)
            def start2():
                z = float(input4.get())
                if z == round(((x+1)*10-1)//y*y, 3):
                    lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                             bg="green", height=1, width=20)
                    lab5.place(x=330, y=160)
                else:
                    lab5 = Label(win1, text="Правильна ответ: {}".format(round(((x+1)*10-1)//y*y, 3)), font="Arial 10",
                                             bg="lightsalmon", height=1, width=20)
                    lab5.place(x=330, y=160)
            but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                       activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
            but9.place(x=220, y=160)

        if r % 8 == 0:
            lab4 = Label(win1, text="В першому бідоні молока в {}\n"
                                    "рази/разів більше, ніж в другому.\n Коли з першого бідона перелили\n"
                                    "в другий {} літрів, молока в \nбідонах стало порівну. Скільки літрів\n"
                                    "молока було в другому бідоні спочатку?".format(x,y), font="Arial 10", bg="lightyellow", height=10, width=75)
            lab4.place(x=0, y=160)
            input4 = Entry(win1, width=10, bd=3, font=("Arial", 8), bg="lemonchiffon")
            input4.place(x=150, y=160)
            def start2():
                z = float(input4.get())
                if z == round((2*y)/(x-1), 3):
                    lab5 = Label(win1, text="Ответ правильный!", font="Arial 10",
                                             bg="green", height=1, width=20)
                    lab5.place(x=330, y=160)
                else:
                    lab5 = Label(win1, text="Правильна ответ: {}".format(round((2*y)/(x-1), 3)), font="Arial 10",
                                             bg="lightsalmon", height=1, width=20)
                    lab5.place(x=330, y=160)
            but9 = Button(win1, text="Проверить", bg="saddlebrown", fg="white", activebackground="white",
                                       activeforeground="black", width=10, height=1, command=start2, font=("Arial", 8))
            but9.place(x=220, y=160)
    but8 = Button(win1, text="Генерировать задачу", bg="saddlebrown", fg="white", activebackground="white",
               activeforeground="black", width=23, height=1,  command=start1, font=("Arial", 8))
    but8.place(x=0, y=100)

but1 = Button(win1, bg="yellow", text="Умножение", activebackground="black", activeforeground="white",
           command=func1, font=("Arial", 10), height=1, width=15)
but1.place(x=15, y=10)

but2 = Button(win1, bg="yellow", text="Деление", activebackground="black", activeforeground="white",
           command=func2, font=("Arial", 10), height=1, width=15)
but2.place(x=165, y=10)

but3 = Button(win1, bg="yellow", text="НСД", activebackground="black", activeforeground="white",
           command=func3, font=("Arial", 10), height=1, width=15)
but3.place(x=315, y=10)

but4 = Button(win1, bg="yellow", text="НСК", activebackground="black", activeforeground="white",
           command=func4, font=("Arial", 10), height=1, width=15)
but4.place(x=465, y=10)

but5 = Button(win1, bg="yellow", text="Пропорция", activebackground="black", activeforeground="white",
           command=func5, font=("Arial", 10), height=1, width=15)
but5.place(x=465, y=90)

but6 = Button(win1, bg="yellow", text="Уравнения", activebackground="black", activeforeground="white",
           command=func6, font=("Arial", 10), height=1, width=15)
but6.place(x=315, y=50)

but7 = Button(win1, bg="yellow", text="Дроби", activebackground="black", activeforeground="white",
           command=func7, font=("Arial", 10), height=1, width=15)
but7.place(x=315, y=90)

but7 = Button(win1, bg="yellow", text="Задачи", activebackground="black", activeforeground="white",
           command=func8, font=("Arial", 10), height=1, width=15)
but7.place(x=465, y=50)


"""
text = "Hello,world"
lab1 = Label(win1, text=text, font="Arial 10", bg="lightyellow", height=1)
lab1.place(x=0,y=0)
"""
win1.mainloop()