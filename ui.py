from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 10, "italic")
WHITE = "#dfe6e9"


class QuizUI:

    def __init__(self):
        # window
        self.window = Tk()
        self.window.title("Quizkaton")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # label
        self.score_label = Label(text="Score: ",
                                 font=SCORE_FONT,
                                 bg=THEME_COLOR,
                                 fg="white"
                                 )

        self.score_label.grid(column=1, row=0)
        # canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="question text",
                                                     fill=THEME_COLOR,
                                                     font=FONT,
                                                     )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # buttons
        true_answer_image = PhotoImage(file="images/true.png")
        self.answer_true_button = Button(image=true_answer_image, highlightthickness=0)
        self.answer_true_button.grid(column=0, row=2)
        false_answer_image = PhotoImage(file="images/false.png")
        self.answer_false_button = Button(image=false_answer_image, highlightthickness=0)
        self.answer_false_button.grid(column=1, row=2)

        self.window.mainloop()
