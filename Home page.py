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

        # question & answers
        self.questions = [
            {
                "text": "What is the symbol of Hydrogen?",
                "image": "Q1.png",
                "options": ["H", "He", "Hy", "Hg"],
                "answer": "H"
            },
            {
                "text": "What is the symbol of Helium?",
                "image": "Q2.png",
                "options": ["H", "He", "Hy", "Hg"],
                "answer": "He"
            },
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

    def clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def setup_grid_layout(self):

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)  # Left content
        self.container.grid_columnconfigure(1, weight=1)  # Centre content
        self.container.grid_columnconfigure(2, weight=1)  # Right Emergency Button

    def add_emergency_button(self):

        try:
            self.emergency_img = tk.PhotoImage(file="emergency.png")
            exit_btn = tk.Button(self.container, image=self.emergency_img, command=self.restart_quiz,
                                 borderwidth=0, relief="flat", highlightthickness=0)
        except:
            exit_btn = tk.Button(self.container, text="⚠ Exit", font=("Arial", 12, "bold"),
                                 fg="white", bg="red", command=self.restart_quiz)

        # Always locked to Column 2 across all secondary screens
        exit_btn.grid(row=0, column=2, padx=20, pady=20)


    def show_home(self):
        self.clear_screen()
        try:
            self.bg_img = tk.PhotoImage(file="background.png")
            bg_label = tk.Label(self.container, image=self.bg_img)
            bg_label.place(relwidth=1, relheight=1)
        except:
            tk.Label(self.container, text="[Background Image]", bg="lightblue").place(relwidth=1, relheight=1)

        try:
            self.start_btn_img = tk.PhotoImage(file="start_button.png")
            start_btn = tk.Button(self.container, image=self.start_btn_img, command=self.show_login, borderwidth=0, relief= "flat", highlightthickness=0 )
        except:
            start_btn = tk.Button(self.container, command=self.show_login)
        start_btn.pack(expand=True)

    def show_login(self):
        self.clear_screen()


        try:
            self.login_bg_img = tk.PhotoImage(file="Bg.png")
            bg_label = tk.Label(self.container, image=self.login_bg_img)
            bg_label.place(relwidth=1, relheight=1)
        except:
            tk.Label(self.container, text="[Background Image]", bg="lightblue").place(relwidth=1, relheight=1)

        self.setup_grid_layout()
        login_frame = tk.Frame(self.container, bg="black")
        login_frame.grid(row=0, column=1, padx=20, pady=20)

        self.user_entry = tk.Entry(login_frame, font=("Arial", 30))
        self.user_entry.pack(pady=20)


        try:
            self.begin_btn_img = tk.PhotoImage(file="Begin_button.png")
            begin_btn = tk.Button(self.container, image=self.begin_btn_img, command=self.save_user, borderwidth=0,
                                  relief="flat", highlightthickness=0)
        except:
            begin_btn = tk.Button(self.container, text="Begin", command=self.save_user)


        begin_btn.place(relx=0.37, rely=0.70, anchor="center")

        self.add_emergency_button()

    def save_user(self):
        self.username = self.user_entry.get()
        if not self.username:
            messagebox.showwarning("Error", "Please enter a name!")
            return
        self.show_question()

    def show_question(self):
        self.clear_screen()
        try:
            self.question_bg_img = tk.PhotoImage(file="Questionbg.png")
            bg_label = tk.Label(self.container, image=self.question_bg_img)
            bg_label.place(relwidth=1, relheight=1)
        except:
            tk.Label(self.container, text="[Background Image]", bg="lightblue").place(relwidth=1, relheight=1)

        q_data = self.questions[self.current_question]

        self.setup_grid_layout()


        left_frame = tk.Frame(self.container, bg="black")
        left_frame.grid(row=0, column=0, padx=20, pady=20)


        right_frame = tk.Frame(self.container, bg="black")
        right_frame.grid(row=0, column=1, padx=20, pady=20)

        tk.Label(left_frame, text=q_data["text"], font=("Arial", 30, "bold"), fg="white", bg="black",
                 wraplength=400).pack(pady=10)

        try:
            self.q_img = tk.PhotoImage(file=q_data["image"])
            tk.Label(left_frame, image=self.q_img).pack(pady=10)
        except:
            tk.Label(left_frame, text="[Question Image]", height=10).pack()


        for option in q_data["options"]:
            tk.Button(right_frame, text=option, font=("Canva Sans", 20), width=20,
                      command=lambda opt=option: self.check_answer(opt)).pack(pady=5)

        self.add_emergency_button()

    def check_answer(self, choice):

        if choice == self.questions[self.current_question]["answer"]:
            self.streak += 1
            self.current_question += 1

            # Check if there are more questions
            if self.current_question < len(self.questions):
                self.show_question()
            else:
                self.show_end_screen("Perfect Game!")
        else:

            self.show_end_screen("Game Over!")

    def show_end_screen(self, title_text):
        self.clear_screen()
        try:
            self.finish_img = tk.PhotoImage(file="finish.png")
            bg_label = tk.Label(self.container, image=self.finish_img)
            bg_label.place(relwidth=1, relheight=1)
        except:
            tk.Label(self.container, text="[Background Image]", bg="lightblue").place(relwidth=1, relheight=1)

        self.setup_grid_layout()


        end_frame = tk.Frame(self.container, bg="black")
        end_frame.grid(row=0, column=1, padx=20, pady=20)

        tk.Label(end_frame, text=f"{self.username}'s Final Streak", font=("Arial", 18), bg="black", fg="white").pack()

        tk.Label(end_frame, text=str(self.streak), font=("Arial", 60, "bold"), fg="black", bg="yellow").pack(pady=10)

        try:
            self.end_img = tk.PhotoImage(file="END.png")
            tk.Label(self.container, image=self.end_img).pack(pady=10)
        except:
            tk.Label(self.container, font=("Arial", 80)).pack()

        tk.Button(self.container, text="Play Again", command=self.restart_quiz).pack(pady=30)

        self.add_emergency_button()

    def restart_quiz(self):
        self.streak = 0
        self.current_question = 0
        self.show_home()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


