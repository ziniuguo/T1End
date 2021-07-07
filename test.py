"""
Class 05 Group 06:
Eunice Kwok Xiu Yi, Guo Ziniu, Sarah Chua Yi Qi, Xavier Leung

Run this .py file in any Python IDE you like.

The interaction will be in the pop-up windows and Python console.
Use 'w', 'a', 's', 'd' to navigate, and 'g' to interact.
Please do not turn on CAPSLOCK when running it.

"""

from turtle import *
import turtle
import random
import tkinter as tk
import tkinter.messagebox
import threading
import time
import os

player1 = {"HP": 150, "Defense": 80, "Strength": 100}
playerhp = 190
monsterhp = 0
monster1 = {"HP": 650, "Defense": 60, "Strength": 120}
player = [-20, -20, 40]
xy = [[-20, -20, 40]]  # explored grids
space = [[-20, -20]]
n_position = []
m_position = []
g_position = []
f_position = []


def math():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    symbol = random.randint(1, 4)

    if symbol == 1:
        question = turtle.textinput("Time for some math", "What is " + str(num1) + "+" + str(num2) + "?")
        if type(question) is str:
            question = float(question)

        if question == num1 + num2:
            player1["HP"] = player1["HP"] + 10
            tk.messagebox.showinfo("Result",
                                   "Congratulations! You are correct! You are rewarded with 10 HP points\n" + "Player state =\t Strength:" + str(
                                       player1["Strength"]) + "\t Defense:" + str(player1["Defense"]) + "\t HP:" + str(
                                       player1["HP"]))
        elif question is None:
            player1["HP"] = player1["HP"] - 10
            tk.messagebox.showinfo("Result",
                                   "You give up. As a penalty 10 HP points will be deducted!\n" + "Player state =\t Strength:" + str(
                                       player1["Strength"]) + "\t Defense:" + str(player1["Defense"]) + "\t HP:" + str(
                                       player1["HP"]))
        else:
            tk.messagebox.showinfo("Result",
                                   "Oh No, you did not answer correctly. No rewards for you. But this is a nice try!\n" + "Player state =\t Strength:" + str(
                                       player1["Strength"]) + "\t Defense:" + str(player1["Defense"]) + "\t HP:" + str(
                                       player1["HP"]))

    elif symbol == 2:
        question = turtle.textinput("Time for some math", "What is " + str(num1) + "-" + str(num2) + "?")
        if type(question) is str:
            question = float(question)
        if question == num1 - num2:
            player1["HP"] = player1["HP"] + 10
            tk.messagebox.showinfo("Result",
                                   "Congratulations! You are correct! You are rewarded with 10 HP points\n" + "Player state =\t Strength:" + str(
                                       player1["Strength"]) + "\t Defense:" + str(player1["Defense"]) + "\t HP:" + str(
                                       player1["HP"]))
        elif question is None:
            player1["HP"] = player1["HP"] - 10
            tk.messagebox.showinfo("Result",
                                   "You give up. As a penalty 10 HP points will be deducted!\n" + "Player state =\t Strength:" + str(
                                       player1["Strength"]) + "\t Defense:" + str(player1["Defense"]) + "\t HP:" + str(
                                       player1["HP"]))
        else:
            tk.messagebox.showinfo("Result",
                                   "Oh No, you did not answer correctly. No rewards for you. But this is a nice try!\n" + "Player state =\t Strength:" + str(
                                       player1["Strength"]) + "\t Defense:" + str(player1["Defense"]) + "\t HP:" + str(
                                       player1["HP"]))

    elif symbol == 3:
        question = turtle.textinput("Time for some math", "What is " + str(num1) + "*" + str(num2) + "?")
        if type(question) is str:
            question = float(question)
        if question == num1 * num2:
            player1["HP"] = player1["HP"] + 10
            tk.messagebox.showinfo("Result",
                                   "Congratulations! You are correct! You are rewarded with 10 HP points\n" + "Player state =\t Strength:" + str(
                                       player1["Strength"]) + "\t Defense:" + str(player1["Defense"]) + "\t HP:" + str(
                                       player1["HP"]))
        elif question is None:
            player1["HP"] = player1["HP"] - 10
            tk.messagebox.showinfo("Result",
                                   "You give up. As a penalty 10 HP points will be deducted!\n" + "Player state =\t Strength:" + str(
                                       player1["Strength"]) + "\t Defense:" + str(player1["Defense"]) + "\t HP:" + str(
                                       player1["HP"]))
        else:
            tk.messagebox.showinfo("Result",
                                   "Oh No, you did not answer correctly. No rewards for you. But this is a nice try!\n" + "Player state =\t Strength:" + str(
                                       player1["Strength"]) + "\t Defense:" + str(player1["Defense"]) + "\t HP:" + str(
                                       player1["HP"]))

    elif symbol == 4:
        question = turtle.textinput("Time for some math", "What is " + str(num1) + "//" + str(num2) + "?")
        if type(question) is str:
            question = float(question)
        if question == num1 // num2:
            player1["HP"] = player1["HP"] + 10
            tk.messagebox.showinfo("Result",
                                   "Congratulations! You are correct! You are rewarded with 10 HP points\n" + "Player state =\t Strength:" + str(
                                       player1["Strength"]) + "\t Defense:" + str(player1["Defense"]) + "\t HP:" + str(
                                       player1["HP"]))
        elif question is None:
            player1["HP"] = player1["HP"] - 10
            tk.messagebox.showinfo("Result",
                                   "You give up. As a penalty 10 HP points will be deducted!\n" + "Player state =\t Strength:" + str(
                                       player1["Strength"]) + "\t Defense:" + str(player1["Defense"]) + "\t HP:" + str(
                                       player1["HP"]))
        else:
            tk.messagebox.showinfo("Result",
                                   "Oh No, you did not answer correctly. No rewards for you. But this is a nice try!\n" + "Player state =\t Strength:" + str(
                                       player1["Strength"]) + "\t Defense:" + str(player1["Defense"]) + "\t HP:" + str(
                                       player1["HP"]))
    listen()
    onkey(None, 'g')
    onkey(explore_w, 'w')
    onkey(explore_a, 'a')
    onkey(explore_s, 's')
    onkey(explore_d, 'd')
    gameloop()


def non_combat():
    n = random.randrange(-25, 26, 5)
    option = random.randint(0, 2)
    if n > 0:
        message = ("Congratulations, you have found a treasure box! You have won yourself " + str(n) + " free ")
        if option == 0:
            smessage = message + "strength points!"
            tk.messagebox.showinfo("Treasure Chest", smessage)
            player1["Strength"] = player1["Strength"] + n
            tk.messagebox.showinfo("Player Info",
                                   "current state =\t Strength:" + str(player1["Strength"]) + "\t Defense:" + str(
                                       player1["Defense"]) + "\t HP:" + str(player1["HP"]))
        if option == 1:
            dmessage = message + "defense points!"
            tk.messagebox.showinfo("Treasure Chest", dmessage)
            player1["Defense"] = player1["Defense"] + n
            tk.messagebox.showinfo("Player Info",
                                   "current state =\t Strength:" + str(player1["Strength"]) + "\t Defense:" + str(
                                       player1["Defense"]) + "\t HP:" + str(player1["HP"]))
        if option == 2:
            hpmessage = message + "HP points!"
            tk.messagebox.showinfo("Treasure Chest", hpmessage)
            player1["HP"] = player1["HP"] + n
            tk.messagebox.showinfo("Player Info",
                                   "current state =\t Strength:" + str(player1["Strength"]) + "\t Defense:" + str(
                                       player1["Defense"]) + "\t HP:" + str(player1["HP"]))
    elif n < 0:
        if option == 0:
            tk.messagebox.showinfo("Treasure Chest",
                                   "How unlucky! You found an exploding bomb. You lose " + str(
                                       abs(n)) + " strength points.")
            player1["Strength"] = player1["Strength"] + n
            tk.messagebox.showinfo("Player Info",
                                   "current state =\t Strength:" + str(player1["Strength"]) + "\t Defense:" + str(
                                       player1["Defense"]) + "\t HP:" + str(player1["HP"]))
        if option == 1:
            tk.messagebox.showinfo("Treasure Chest",
                                   "You need to surrender part of your safety vest. " + str(
                                       abs(n)) + " defense points are deducted!")
            player1["Defense"] = player1["Defense"] + n
            tk.messagebox.showinfo("Player Info",
                                   "current state =\t Strength:" + str(player1["Strength"]) + "\t Defense:" + str(
                                       player1["Defense"]) + "\t HP:" + str(player1["HP"]))
        if option == 2:
            tk.messagebox.showinfo("Treasure Chest",
                                   "You found a dead body and you are now suspected as the murderer. You lose " + str(
                                       abs(n)) + " HP points.")
            player1["HP"] = player1["HP"] + n
            tk.messagebox.showinfo("Player Info",
                                   "current state =\t Strength:" + str(player1["Strength"]) + "\t Defense:" + str(
                                       player1["Defense"]) + "\t HP:" + str(player1["HP"]))
    else:
        tk.messagebox.showinfo("Treasure Chest",
                               "Oh no! You came too late. You found an empty chest. All the treasures were stolen.")
    listen()
    onkey(None, 'g')
    onkey(explore_w, 'w')
    onkey(explore_a, 'a')
    onkey(explore_s, 's')
    onkey(explore_d, 'd')
    gameloop()


questions = {  # (also contains the answers)
    "made divorce pea whiff ewe": "may the force be with you",
    "Coughing night ten": "covid19",  # how about covid 19 as answer too
    "sir key it bray acre": "circuit breaker",
    "Aw hunt eeth atway": "i want it that way",
    "Hatch meows hide hobo dad": "catch me outside how bout that",
    "Sauce shell dice then sink": "social distancing",
    "gnome morse ghoul": "no more school",
    "is bunch pops queer pans": "spongebob squarepants",
    "Mine case seed mud kiddo": "monkey see monkey do",
    "huat tavern it stakes": "whatever it takes",
    "Veer oof essing oat": "fear of missing out",
    "D führer iz yhals du krate": "the future is yours to create",
    "B d chank uub ish du c in dwow": "be the change you wish to see in the world",
}
learned_questions = set()


"""
The code for function below was modified from 
https://stackoverflow.com/questions/43206277/how-can-i-make-my-quiz-randomly-select-unseen-qs-in-python
"""


def gibberish():
    while len(questions) > len(learned_questions):
        unanswered_questions = set(questions) - learned_questions
        chosen_question = random.choice(list(unanswered_questions))
        correct_answer = questions[chosen_question]
        given_answer = turtle.textinput("Solve the Gibberish", chosen_question)
        if type(given_answer) is str:
            given_answer = given_answer.lower()

        if given_answer == correct_answer:
            tk.messagebox.showinfo("Result", "Congratulations! You are correct! You are rewarded with 10 HP points!")
            player1["HP"] = player1["HP"] + 10
            tk.messagebox.showinfo("Player Info",
                                   "current state =\t Strength:" + str(player1["Strength"]) + "\t Defense:" + str(
                                       player1["Defense"]) + "\t HP:" + str(player1["HP"]))
            learned_questions.add(chosen_question)
            break

        elif given_answer is None:
            tk.messagebox.showinfo("Result", "You give up. As a penalty 10 HP points will be deducted!")
            player1["HP"] = player1["HP"] - 10
            tk.messagebox.showinfo("Player Info",
                                   "current state =\t Strength:" + str(player1["Strength"]) + "\t Defense:" + str(
                                       player1["Defense"]) + "\t HP:" + str(player1["HP"]))
            break

        else:
            msg = "Oh No, you did not answer correctly. No rewards for you. Correct answer would have been: " + str(
                correct_answer)
            tk.messagebox.showinfo("Result", msg)
            tk.messagebox.showinfo("Player Info",
                                   "current state =\t Strength:" + str(player1["Strength"]) + "\t Defense:" + str(
                                       player1["Defense"]) + "\t HP:" + str(player1["HP"]))
            break
    listen()
    onkey(None, 'g')
    onkey(explore_w, 'w')
    onkey(explore_a, 'a')
    onkey(explore_s, 's')
    onkey(explore_d, 'd')
    gameloop()


def showplayer():  # show the player at the centre of the map
    for i in n_position:  # draw all explored event spaces
        penup()
        goto(i[0] + 16.5, i[1] + 13)
        pendown()
        pencolor('black')
        write('宝', )
        penup()
    for j in f_position:  # draw all explored spaces
        penup()
        goto(j[0] + 16.5, j[1] + 13)
        pendown()
        pencolor('black')
        write('凸', )
        penup()
    for k in m_position:  # draw all explored spaces
        penup()
        goto(k[0] + 15.5, k[1] + 12.3)
        pendown()
        pencolor('black')
        write("+", font=(15))
        penup()
    for h in g_position:  # draw all explored spaces
        penup()
        goto(h[0] + 7, h[1] + 13)
        pendown()
        pencolor('black')
        write('￥%#/', )
        penup()
    goto(player[0] + 16.5, player[1] + 13)
    pendown()
    pencolor('black')
    write('人', )
    penup()
    goto(-380, 380)
    pendown()
    pencolor('white')
    write("Player Info =\t Strength:" + str(
        player1["Strength"]) + "\t Defense:" + str(
        player1["Defense"]) + "\t HP:" + str(player1["HP"]) + "\t \t Please use w, a, s, d keys to navigate.")
    penup()


"""
The code for this class that control the other thread was taken from https://www.cnblogs.com/scolia/p/6132950.html

One disadvantage of this method is that every time you pause/stop the thread, it won't stop until the beginning of 
the while loop. 
"""


class Job(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True

    def run(self):
        global playerhp
        while self.__running.isSet():
            self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            playerhp -= monster1["Strength"] - player1["Defense"]
            print("Player HP: " + str(playerhp))
            if playerhp <= 0:
                t.pause()
                listen()
                onkey(None, 'g')
                onkey(explore_w, 'w')
                onkey(explore_a, 'a')
                onkey(explore_s, 's')
                onkey(explore_d, 'd')
                tk.messagebox.showinfo("Result", "You are defeated by the monster. You lose 30 HP!")
                player1["HP"] = player1["HP"] - 30
                gameloop()
            time.sleep(2)

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


t = Job()
t.start()
t.pause()


def showfighting():
    global monsterhp, playerhp
    monsterhp -= (player1["Strength"] - monster1["Defense"])
    print("You hit the monster! " + "Monster HP: " + str(monsterhp))
    if monsterhp < 0:
        t.pause()
        listen()
        onkey(None, 'g')
        onkey(explore_w, 'w')
        onkey(explore_a, 'a')
        onkey(explore_s, 's')
        onkey(explore_d, 'd')
        tk.messagebox.showinfo("Result", "Congratulations! You have defeated the mighty strong monster! You win 30 HP!")
        player1["HP"] = player1["HP"] + 30
        gameloop()


def fight():
    global playerhp, monsterhp
    playerhp = player1["HP"]
    monsterhp = monster1["HP"]
    a = tk.messagebox.askyesno("Fight", "You have encountered a monster\n \n" + "Monster Info =\t Strength:" + str(
        monster1["Strength"]) + "\t Defense:" + str(monster1["Defense"]) + "\t HP:" + str(
        monster1["HP"]) + "\n" + "Player Info =\t Strength:" + str(player1["Strength"]) + "\t Defense:" + str(
        player1["Defense"]) + "\t HP:" + str(player1["HP"]) + "\n" + "Do you wanna fight? If yes, press G as fast as "
                                                                     "possible before the monster knocks you down! "
                                                                     "Immediately start after choosing 'Yes'!")

    if a:
        print("Monster HP: " + str(monster1["HP"]) + " Player HP: " + str(playerhp))
        t.resume()
        listen()
        onkey(None, 'f')
        onkey(showfighting, 'g')
        onkey(None, 'w')
        onkey(None, 'a')
        onkey(None, 's')
    else:
        tk.messagebox.showinfo("Oh no!", "Even though you tried to escape, the monster knocked you down. 30 HP lost!")
        player1["HP"] = player1["HP"] - 30
        listen()
        onkey(None, 'g')
        onkey(explore_w, 'w')
        onkey(explore_a, 'a')
        onkey(explore_s, 's')
        onkey(explore_d, 'd')
        gameloop()


def square(x, y, size, color_name):  # draw a square
    up()
    goto(x, y)
    down()
    color(color_name)
    begin_fill()
    for i in range(4):
        forward(size)
        left(90)
    end_fill()


def line(x, y, a, b, line_width=1, color_name="black"):  # draw a line
    up()
    goto(x, y)
    down()
    color(color_name)
    width(line_width)
    goto(a, b)


def event_space():  # assign spaces where player triggers event
    global space
    n = 1
    while n < 50:
        x = random.randint(-9, 10) * 40 - 20
        y = random.randint(-9, 10) * 40 - 20
        n += 1
        space.append([x, y])
    temp_list = []
    for one in space:
        if one not in temp_list:
            temp_list.append(one)
    space = list(temp_list)
    if [-20, -20] in space:
        space.remove([-20, -20])


def check():
    playerposition = [player[0], player[1]]  # check position of player then interact
    for i in space:
        if i == playerposition:
            space.remove(i)
            listen()
            onkey(None, 'g')
            onkey(None, 'w')
            onkey(None, 'a')
            onkey(None, 's')
            onkey(None, 'd')
            rand = random.randint(1, 99)
            if rand <= 33:
                rand1 = random.randint(1, 2)
                if rand1 == 1:
                    math()
                    m_position.append(i)
                else:
                    gibberish()
                    g_position.append(i)
            elif 33 < rand <= 66:
                fight()
                f_position.append(i)
            else:
                non_combat()
                n_position.append(i)


def init():  # initial setups
    turtle.setup(800, 800)
    hideturtle()
    tracer(False)
    bgcolor('black')
    bgpic('pct.gif')
    penup()
    event_space()
    tk.messagebox.showinfo("Welcome!", 'Hola courageous knight, to the world of supercalifragilisticexpialidocious! '
                                       'Escape this world by obtaining 235 HP. Defend yourself from the monster by '
                                       'clicking the "G" button very fast and not letting your HP drop to zero. All '
                                       'the best for your quest!')


def explore_w():  # explore new grids
    if player[1] < 340:
        player[1] = player[1] + 40
    if player not in xy:
        xy.append(list(player))
    gameloop()


def explore_a():
    if -380 < player[0]:
        player[0] = player[0] - 40
    if player not in xy:
        xy.append(list(player))
    gameloop()


def explore_s():
    if -380 < player[1]:
        player[1] = player[1] - 40
    if player not in xy:
        xy.append(list(player))
    gameloop()


def explore_d():
    if player[0] < 340:
        player[0] = player[0] + 40
    if player not in xy:
        xy.append(list(player))
    gameloop()


def gameloop():  # game loop
    clear()
    for i in xy:  # draw all explored grids
        square(i[0], i[1], i[2], 'white')
    showplayer()
    check()
    update()
    if player1["HP"] <= 0:
        tkinter.messagebox.showerror("Game Over", "Your HP is " + str(player1["HP"]) + ". You have lost the game!")
        turtle.bye()
        os._exit(0)
    elif player1["HP"] >= 235:
        tk.messagebox.showinfo("You win this game!",
                               "Lo hicimos! Congratulation in completing the quest! Moral of the story: Don't "
                               "Give Up")
        turtle.bye()
        os._exit(0)
    elif len(xy) == 19 * 19:
        tk.messagebox.showwarning("Game Over", "You have explored the full map but you still do not reach 235 HP. "
                                               "What a pity! You have lost.")
        turtle.bye()
        os._exit(0)


init()
listen()
onkey(None, 'g')
onkey(explore_w, 'w')
onkey(explore_a, 'a')
onkey(explore_s, 's')
onkey(explore_d, 'd')
gameloop()
done()
