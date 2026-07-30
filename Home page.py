import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chemical Elements Symbol quiz")
        self.root.geometry("1138x640")

        # Quiz Data
        self.username = ""
        self.streak = 0
        self.current_question = 0

        # All 20 Questions with options, answers and images.
        self.questions = [
            {"text": "What is the symbol of Hydrogen?", "image": "Q1.png", "options": ["H", "He", "Hy", "Hg"],
             "answer": "H"},
            {"text": "What is the symbol of Helium?", "image": "Q2.png", "options": ["H", "He", "Hy", "Hg"],
             "answer": "He"},
            {
                "text": "What is the symbol of Lithium?",
                "image": "Q3.png",
                "options": ["L", "Li", "Lt", "Lh"],
                "answer": "Li"
            },
            {
                "text": "What is the symbol of Beryllium?",
                "image": "Q4.png",
                "options": ["B", "Be", "Br", "Bg"],
                "answer": "Be"
            },
            {
                "text": "What is the symbol of Boron?",
                "image": "Q5.png",
                "options": ["B", "Be", "Br", "Bg"],
                "answer": "B"
            },
            {
                "text": "What is the symbol of Carbon?",
                "image": "Q6.png",
                "options": ["C", "Ce", "Cy", "Cg"],
                "answer": "C"
            },
            {
                "text": "What is the symbol of Nitrogen?",
                "image": "Q7.png",
                "options": ["N", "Ne", "Ny", "Ng"],
                "answer": "N"
            },
            {
                "text": "What is the symbol of Oxygen?",
                "image": "Q8.png",
                "options": ["O", "Oe", "Oy", "Og"],
                "answer": "O"
            },
            {
                "text": "What is the symbol of Fluorine?",
                "image": "Q9.png",
                "options": ["F", "Fe", "Fy", "Fg"],
                "answer": "F"
            },
            {
                "text": "What is the symbol of Neon?",
                "image": "Q10.png",
                "options": ["N", "Ne", "Na", "No"],
                "answer": "Ne"
            },
            {
                "text": "What is the symbol of Sodium?",
                "image": "Q11.png",
                "options": ["N", "Ne", "Na", "No"],
                "answer": "Na"
            },
            {
                "text": "What is the symbol of Magnesium?",
                "image": "Q12.png",
                "options": ["M", "Me", "My", "Mg"],
                "answer": "Mg"
            },
            {
                "text": "What is the symbol of Aluminium?",
                "image": "Q13.png",
                "options": ["A", "Ae", "Al", "Ag"],
                "answer": "Al"
            },
            {
                "text": "What is the symbol of Silicon?",
                "image": "Q14.png",
                "options": ["S", "Se", "Sy", "Si"],
                "answer": "Si"
            },
            {
                "text": "What is the symbol of Phosphorus?",
                "image": "Q15.png",
                "options": ["P", "Pe", "Po", "Pg"],
                "answer": "P"
            },
            {
                "text": "What is the symbol of Sulfur?",
                "image": "Q16.png",
                "options": ["S", "Se", "Sy", "Sg"],
                "answer": "S"
            },
            {
                "text": "What is the symbol of Chlorine?",
                "image": "Q17.png",
                "options": ["C", "Ce", "Cl", "Cg"],
                "answer": "Cl"
            },
            {
                "text": "What is the symbol of Argon?",
                "image": "Q18.png",
                "options": ["A", "Ao", "Ar", "Ag"],
                "answer": "Ar"
            },
            {
                "text": "What is the symbol of Potassium?",
                "image": "Q19.png",
                "options": ["K", "Pe", "Py", "Po"],
                "answer": "K"
            },
            {
                "text": "What is the symbol of Calcium?",
                "image": "Q20.png",
                "options": ["C", "Ce", "Ca", "Cg"],
                "answer": "Ca"
            }
        ]

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.show_home()

# CLear screen code to remove any widgets before loading a new command

    def clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

            #Grind layout setup for emergency exit to make the program similar to final design

    def setup_grid_layout(self):
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)
        self.container.grid_columnconfigure(2, weight=1)

        #emergency exit button with image that leads to homepage

    def add_emergency_button(self):

    # Try and except command to prevent errors if the image fail to load.
        try:
            self.emergency_img = tk.PhotoImage(file="emergency.png")
            exit_btn = tk.Button(self.container, image=self.emergency_img, command=self.restart_quiz_to_home,
                                 borderwidth=0, relief="flat", highlightthickness=0)
        except:
            exit_btn = tk.Button(self.container, text="Exit", font=("Arial", 12, "bold"),
                                 fg="white", bg="red", command=self.restart_quiz_to_home)
        exit_btn.grid(row=0, column=2, padx=20, pady=20)

        #Homepage with help icon, start button and background images.

    def show_home(self):
        self.clear_screen()
        # Try and except command to prevent errors if the image fail to load.
        try:
            self.bg_img = tk.PhotoImage(file="background.png")
            bg_label = tk.Label(self.container, image=self.bg_img)
            bg_label.place(relwidth=1, relheight=1)
        except:
            tk.Label(self.container, text="[Background Image]", bg="lightblue").place(relwidth=1, relheight=1)
# start button with background image
        try:
            self.start_btn_img = tk.PhotoImage(file="start_button.png")
            start_btn = tk.Button(self.container, image=self.start_btn_img, command=self.show_login, borderwidth=0,
                                  relief="flat", highlightthickness=0)
        except:
            start_btn = tk.Button(self.container, text="Start Quiz", command=self.show_login)
        start_btn.pack(expand=True)
# Help button with background image
        try:
            self.help_img = tk.PhotoImage(file="help_icon.png")
            help_btn = tk.Button(self.container, image=self.help_img, command=self.show_help_page,
                                 borderwidth=0, relief="flat", highlightthickness=0, cursor="hand2")
        except:
            help_btn = tk.Button(self.container, text="Help ", font=("Arial", 12, "bold"),
                                 bg="white", fg="black", padx=10, pady=5, command=self.show_help_page)
            # Position the help button
        help_btn.place(relx=1.0, x=-20, y=20, anchor="ne")

#help page with back ground image and the exit button.
    def show_help_page(self):
        self.clear_screen()
        #grid layout for exit button
        self.setup_grid_layout()
        # Try and except command to prevent errors if the image fail to load.
        try:
            self.help_bg_img = tk.PhotoImage(file="help_background.png")
            bg_label = tk.Label(self.container, image=self.help_bg_img)
            bg_label.place(relwidth=1, relheight=1)
        except:
            tk.Label(self.container, text="[Help Background]", bg="#1a1a1a").place(relwidth=1, relheight=1)
            #exit button
        self.add_emergency_button()
# login page with user input area, back ground image and exit button
    def show_login(self):
        self.clear_screen()
        # Try and except command to prevent errors if the image fail to load.
        try:
            self.login_bg_img = tk.PhotoImage(file="Bg.png")
            bg_label = tk.Label(self.container, image=self.login_bg_img)
            bg_label.place(relwidth=1, relheight=1)
        except:
            tk.Label(self.container, text="[Background Image]", bg="lightblue").place(relwidth=1, relheight=1)
# grid layout for exit button
        self.setup_grid_layout()
        #Frame for user to input their name
        login_frame = tk.Frame(self.container, bg="black")
        login_frame.grid(row=0, column=1, padx=20, pady=20)

        self.user_entry = tk.Entry(login_frame, font=("Arial", 30))
        self.user_entry.pack(pady=20)
        # Try and except command to prevent errors if the image fail to load.
        try:
            self.begin_btn_img = tk.PhotoImage(file="Begin_button.png")
            begin_btn = tk.Button(self.container, image=self.begin_btn_img, command=self.save_user, borderwidth=0,
                                  relief="flat", highlightthickness=0)
        except:
            begin_btn = tk.Button(self.container, text="Begin", command=self.save_user)
# Position the begin button according to the design
        begin_btn.place(relx=0.37, rely=0.70, anchor="center")
        #Exit button
        self.add_emergency_button()
#save user entry and give error message if the user inputs something wrong
    def save_user(self):
        username_input = self.user_entry.get()

        # Check if the length is between 3 and 12, and contains only letters
        if not (3 <= len(username_input) <= 12 and username_input.isalpha()):
            messagebox.showwarning(
                "Invalid Username",
                "Username must be between 3 and 12 characters long and contain letters only!"
            )
            return

        self.username = username_input
        self.show_question()
#Question page with exit button, 4 options and an image
    def show_question(self):
        self.clear_screen()
        # Try and except command to prevent errors if the image fail to load.
        try:
            self.question_bg_img = tk.PhotoImage(file="Questionbg.png")
            bg_label = tk.Label(self.container, image=self.question_bg_img)
            bg_label.place(relwidth=1, relheight=1)
        except:
            tk.Label(self.container, text="[Background Image]", bg="lightblue").place(relwidth=1, relheight=1)
# Use the data from above
        q_data = self.questions[self.current_question]
        # grid layout for the exit button
        self.setup_grid_layout()
# Frame for options to be placed according to the original design
        left_frame = tk.Frame(self.container, bg="black")
        left_frame.grid(row=0, column=0, padx=20, pady=20)

        right_frame = tk.Frame(self.container, bg="black")
        right_frame.grid(row=0, column=1, padx=20, pady=20)

        tk.Label(left_frame, text=q_data["text"], font=("Arial", 30, "bold"), fg="white", bg="black",
                 wraplength=400).pack(pady=10)
        # Try and except command to prevent errors if the image fail to load.
        try:
            self.q_img = tk.PhotoImage(file=q_data["image"])
            tk.Label(left_frame, image=self.q_img).pack(pady=10)
        except:
            tk.Label(left_frame, text="[Question Image]", height=10).pack()

        for option in q_data["options"]:
            tk.Button(right_frame, text=option, font=("Canva Sans", 20), width=20,
                      command=lambda opt=option: self.check_answer(opt)).pack(pady=5)
# exit button
        self.add_emergency_button()
#checks if answer is correct or incorrect
    def check_answer(self, choice):
        #  Check if the answer is correct
        if choice == self.questions[self.current_question]["answer"]:
            self.streak += 1
            self.current_question += 1

            # Check if there are more questions left
            if self.current_question < len(self.questions):
                self.show_question()
            else:
                # If they passed all 20 questions, show the perfect screen
                self.show_perfect_score_screen()
        else:
            # Immediate game over if incorrect!
            self.show_incorrect_score_screen()
# If user gets all 20 questions right
    def show_perfect_score_screen(self):
        self.clear_screen()
        # Try and except command to prevent errors if the image fail to load.
        try:
            self.perfect_bg_img = tk.PhotoImage(file="perfect_bg.png")
            bg_label = tk.Label(self.container, image=self.perfect_bg_img)
            bg_label.place(relwidth=1, relheight=1)
        except:
            tk.Label(self.container, text="[Perfect Score Background]", bg="lightgreen").place(relwidth=1, relheight=1)

#Displays user name along with a message for the user
        title_label = tk.Label(self.container, text=f"Flawless Victory, {self.username}!",
                               font=("Arial", 28, "bold"), bg="black", fg="gold")
        title_label.pack(pady=(120, 10))

# create empty space to match the final design
        spacer = tk.Frame(self.container, height=220, bg="black")
        spacer.pack()

# Play again and Menu buttons
        self.create_navigation_buttons(self.container)

#If user dosent get all 20 questions right
    def show_incorrect_score_screen(self):
        self.clear_screen()
        # Try and except command to prevent errors if the image fail to load.
        try:
            self.incorrect_bg_img = tk.PhotoImage(file="Incorrect_bg.png")
            bg_label = tk.Label(self.container, image=self.incorrect_bg_img)
            bg_label.place(relwidth=1, relheight=1)
        except:
            tk.Label(self.container, text="[Incorrect Score Background]", bg="coral").place(relwidth=1, relheight=1)

        # Text header positioned at the top
        title_label = tk.Label(self.container, text=f"Nice Try! Keep practicing, {self.username}!",
                               font=("Arial", 24, "bold"), bg="black", fg="white")
        title_label.pack(pady=(50, 5))
# shows how many questions the user got right
        score_label = tk.Label(self.container, text=f"Score: {self.streak} / {len(self.questions)}",
                               font=("Arial", 32, "bold"), fg="red", bg="black")
        score_label.pack(pady=(50, 10))

        # Empty pace to match the final design
        spacer = tk.Frame(self.container, height=180, bg="black")
        spacer.pack()

        # Navigation buttons positioned at the bottom
        self.create_navigation_buttons(self.container)
#includes the play again and menu button from the final page
    def create_navigation_buttons(self, parent_frame):
        # Sub-frame to keep buttons perfectly aligned side-by-side
        btn_frame = tk.Frame(parent_frame, bg="black")


        btn_frame.pack(pady=(90, 20))

        # Play Again Button
        # Try and except command to prevent errors if the image fail to load.
        try:
            self.play_again_img = tk.PhotoImage(file="play_again_btn.png")
            play_btn = tk.Button(btn_frame, image=self.play_again_img,
                                 command=self.restart_quiz_to_login,
                                 borderwidth=0, relief="flat", highlightthickness=0)
        except:
            play_btn = tk.Button(btn_frame, text="Play Again",
                                 font=("Arial", 16, "bold"), bg="blue", fg="white",
                                 command=self.restart_quiz_to_login)
        play_btn.pack(side="left", padx=20)

        # Main Menu Button
        # Try and except command to prevent errors if the image fail to load.
        try:
            self.menu_img = tk.PhotoImage(file="menu_btn.png")
            menu_btn = tk.Button(btn_frame, image=self.menu_img,
                                 command=self.restart_quiz_to_home,
                                 borderwidth=0, relief="flat", highlightthickness=0)
        except:
            menu_btn = tk.Button(btn_frame, text="Main Menu",
                                 font=("Arial", 16, "bold"), bg="grey", fg="white",
                                 command=self.restart_quiz_to_home)
        menu_btn.pack(side="left", padx=20)

#For play again button to lead user to login page
    def restart_quiz_to_login(self):
        self.streak = 0
        self.current_question = 0
        self.show_login()
# For exit button and menu button to lead user back to the homepage
    def restart_quiz_to_home(self):
        self.streak = 0
        self.current_question = 0
        self.show_home()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

