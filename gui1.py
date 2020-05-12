import tkinter
import random

computer_guess = random.randint(0,20)  # guesses a number between 0 and 10
def check():
    # get the users value
    user_guess = int(txt_guess.get())

    # compare computer generated num with user input
    if user_guess < computer_guess:
        msg = "Higher!"
    elif user_guess > computer_guess:
        msg = "lower!"
    elif user_guess == computer_guess:
        msg = "correct!"


    # show the lbl_result
    lbl_result["text"] = msg

    #clear txt_guess
    txt_guess.delete(0,5)

def reset():
    global computer_guess

    # generates new num when reset is pressed
    computer_guess = random.randint(0,20)
    # changes the text of lbl_result
    lbl_result["text"] = "Game has been reset, Guess again "




root = tkinter.Tk()  #create root window


root.configure(bg = "white")

# change the title
root.title("Guess the Number")
# change window size
root.geometry("250x75")
# create widget
lbl_title = tkinter.Label(root, text=" This is a number guessing game ", bg ="white")
lbl_title.pack()

lbl_result = tkinter.Label(root, text=" Good luck!", bg="white")
lbl_result.pack()

btn_check = tkinter.Button(root, text="check", fg="black", bg="white", command=check)
btn_check.pack(side="left")

btn_reset = tkinter.Button(root, text="Reset", fg="black", bg="white", command=reset)
btn_reset.pack(side="right")

txt_guess = tkinter.Entry(root, width=8)
txt_guess.pack()

#start the main events
root.mainloop()
root.destroy()
