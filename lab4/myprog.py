import tkinter as tk
import random

words = ["We cannot solve problems\n with the kind of thinking\n we employed when we\n came up with them.",
"Learn as if you will live forever, \nlive like you will die tomorrow.",
"Stay away from those\n people who try to disparage\n your ambitions. Small minds\n will always do that, "
"but\n great minds will give you a feeling\n that you can become great too.",
"When you give joy to other people,\n you get more joy in return.\n You should give a good thought to\n happiness that "
"you can give out.",
"When you change your thoughts,\n remember to also change your world.",
"It is only when we take chances,\n when our lives improve. The initial\n and the most difficult risk that we\n need to "
"take is to become honest.",
"Nature has given us all the pieces\n required to achieve exceptional\n wellness and health, but has left it\n to us to put "
"these pieces together."]

name = ""
numbers = []


def guess_num():
    global game_ans
    numb = int(guess.get())
    guess.delete(0, tk.END)
    ran_ind = random.randint(0, 2)
    print(numb)
    print(numbers[ran_ind])
    if numb == numbers[ran_ind]:
        game_ans.configure(text="Nice! \nYou guessed the number!")
    else:
        game_ans.configure(text="Sorry! \nYou are wrong...")


def go_exit():
    root.destroy()


def start():
    global img
    global heart
    global txt
    canvas1.delete('all')
    canvas1.create_image(0, 0, image=img, anchor="nw")

    canvas1.create_text(260, 200, font=("Times New Roman Bold", 40), text="Welcome!")
    canvas1.create_text(260, 300, font=("Times New Roman Bold", 25), text="Input your name")
    txt.delete(0, tk.END)
    txt.focus()
    canvas1.create_window(260, 350, anchor="center", window=txt)
    btn = tk.Button(root, text="Submit name!", font=("Times New Roman Bold", 20), cursor="hand2", bg="pink", fg="black", command=sub_name)
    canvas1.create_window(260, 400, anchor="center", window=btn)
    btn5 = tk.Button(root, text="Exit", font=("Times New Roman Bold", 15), cursor="hand2", bg="pink",
                     fg="black",
                     command=go_exit)
    canvas1.create_window(260, 700, anchor="center", window=btn5)


def tell_words():
    global img
    global heart
    canvas1.delete('all')
    canvas1.create_image(0, 0, image=img, anchor="nw")
    canvas1.create_text(260, 100, font=("Times New Roman Bold", 40), text="Words!")
    index = random.randint(0, 6)
    canvas1.create_text(260, 350, font=("Times New Roman Bold", 20), fill="white", text=words[index])
    btn11 = tk.Button(root, text="One more!", font=("Times New Roman Bold", 15), cursor="hand2", bg="pink",
                     fg="black",
                     command=tell_words)
    canvas1.create_window(200, 700, anchor="center", window=btn11)
    btn12 = tk.Button(root, text="Go back!", font=("Times New Roman Bold", 15), cursor="hand2", bg="pink",
                      fg="black",
                      command=sub_name)
    canvas1.create_window(320, 700, anchor="center", window=btn12)


def show_pic():
    global img
    global heart
    global pictures
    canvas1.delete('all')
    canvas1.create_image(0, 0, image=img, anchor="nw")
    canvas1.create_text(260, 100, font=("Times New Roman Bold", 40), text="Picture!")
    index = random.randint(0, 6)
    canvas1.create_image(260, 350, image=pictures[index], anchor="center")
    btn21 = tk.Button(root, text="One more!", font=("Times New Roman Bold", 15), cursor="hand2", bg="pink",
                      fg="black",
                      command=show_pic)
    canvas1.create_window(200, 700, anchor="center", window=btn21)
    btn22 = tk.Button(root, text="Go back!", font=("Times New Roman Bold", 15), cursor="hand2", bg="pink",
                      fg="black",
                      command=sub_name)
    canvas1.create_window(320, 700, anchor="center", window=btn22)


def play():
    global img
    global heart
    global guess
    global numbers
    canvas1.delete('all')
    canvas1.create_image(0, 0, image=img, anchor="nw")
    canvas1.create_text(260, 100, font=("Times New Roman Bold", 40), text="Game!")
    numbers = []
    for i in range(3):
        numbers.append(random.randint(1, 100))
    canvas1.create_text(260, 250, font=("Times New Roman Bold", 40),
                        text=str(numbers[0])+"\n"+str(numbers[1])+"\n"+str(numbers[2]))
    canvas1.create_window(260, 370, anchor="center", window=guess)
    guess.focus()
    game_ans.configure(text="")
    canvas1.create_window(260, 550, anchor="center", window=game_ans)
    btn30 = tk.Button(root, text="Guess number!", font=("Times New Roman Bold", 15), cursor="hand2", bg="pink",
                      fg="black",
                      command=guess_num)
    canvas1.create_window(260, 450, anchor="center", window=btn30)
    btn31 = tk.Button(root, text="One more!", font=("Times New Roman Bold", 15), cursor="hand2", bg="pink",
                      fg="black",
                      command=play)
    canvas1.create_window(200, 700, anchor="center", window=btn31)
    btn32 = tk.Button(root, text="Go back!", font=("Times New Roman Bold", 15), cursor="hand2", bg="pink",
                      fg="black",
                      command=sub_name)
    canvas1.create_window(320, 700, anchor="center", window=btn32)


def sub_name():
    global img
    global heart
    global txt
    global name

    name = str(txt.get())
    canvas1.delete('all')
    canvas1.create_image(0, 0, image=img, anchor="nw")
    canvas1.create_text(260, 100, font=("Times New Roman Bold", 40), text=("Welcome "+str(name)+"!"))
    canvas1.create_text(260, 200, font=("Times New Roman Bold", 25), text="What do you want to do today?")

    canvas1.create_image(260, 600, image=heart, anchor="center")

    btn1 = tk.Button(root, text="Tell pleasant words!", font=("Times New Roman Bold", 15), cursor="hand2", bg="pink", fg="black",
                    command=tell_words)
    canvas1.create_window(140, 300, anchor="center", window=btn1)
    btn2 = tk.Button(root, text="Show beautiful picture!", font=("Times New Roman Bold", 15), cursor="hand2", bg="pink",
                     fg="black",
                     command=show_pic)
    canvas1.create_window(260, 400, anchor="center", window=btn2)
    btn3 = tk.Button(root, text="Play with me!", font=("Times New Roman Bold", 15), cursor="hand2", bg="pink",
                     fg="black",
                     command=play)
    canvas1.create_window(380, 300, anchor="center", window=btn3)
    btn4 = tk.Button(root, text="Start again", font=("Times New Roman Bold", 15), cursor="hand2", bg="pink",
                     fg="black",
                     command=start)
    canvas1.create_window(100, 700, anchor="center", window=btn4)
    btn5 = tk.Button(root, text="Exit", font=("Times New Roman Bold", 15), cursor="hand2", bg="pink",
                     fg="black",
                     command=go_exit)
    canvas1.create_window(420, 700, anchor="center", window=btn5)


root = tk.Tk()
root.title("Relax")
root.geometry("520x780")
root.resizable(False, False)
canvas1 = tk.Canvas(root, width=520, height=780)
canvas1.pack()
img = tk.PhotoImage(file="mainpicr.png")
heart = tk.PhotoImage(file="heart.png")
pic_1 = tk.PhotoImage(file="1.png")
pic_2 = tk.PhotoImage(file="2.png")
pic_3 = tk.PhotoImage(file="3.png")
pic_4 = tk.PhotoImage(file="4.png")
pic_5 = tk.PhotoImage(file="5.png")
pic_6 = tk.PhotoImage(file="6.png")
pic_7 = tk.PhotoImage(file="7.png")
pictures = [pic_1, pic_2, pic_3, pic_4, pic_5, pic_6, pic_7]

t_name = tk.StringVar()
txt = tk.Entry(root, font=("Times New Roman Bold", 20), width=15, textvariable=t_name, justify="center", state='normal')
guess = tk.Entry(root, font=("Times New Roman Bold", 20), width=15, justify="center", state='normal')
game_ans = tk.Label(root, font=("Times New Roman Bold", 30), text="", justify="center")
start()


root.mainloop()