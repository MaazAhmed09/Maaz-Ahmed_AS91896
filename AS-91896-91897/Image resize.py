import tkinter as tk
from tkinter import messagebox


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudden Death Quiz")
        self.root.geometry("1138x640")

        # Quiz Data
        self.username = ""
        self.streak = 0
        self.current_question = 0


        self.questions = [
            {
                "text": "What is the capital of France?",
                "image": "paris.png",
                "options": ["London", "Berlin", "Paris", "Madrid"],
                "answer": "Paris"
            },
            {
                "text": "Which programming language is this?",
                "image": "python_logo.png",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "text": "How many legs does a spider have?",
                "image": "spider.png",
                "options": ["6", "8", "10", "12"],
                "answer": "8"
            }
        ]

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.show_home()

    def clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

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
            start_btn = tk.Button(self.container, image=self.start_btn_img, command=self.show_login, borderwidth=0)
        except:
            start_btn = tk.Button(self.container, text="START", font=("Arial", 20), command=self.show_login)
        start_btn.pack(expand=True)

    def show_login(self):
        self.clear_screen()
        tk.Label(self.container, text="Enter Your Username", font=("Arial", 18)).pack(pady=50)
        self.user_entry = tk.Entry(self.container, font=("Arial", 14))
        self.user_entry.pack(pady=10)
        tk.Button(self.container, text="Begin", command=self.save_user).pack(pady=20)

    def save_user(self):
        self.username = self.user_entry.get()
        if not self.username:
            messagebox.showwarning("Error", "Please enter a name!")
            return
        self.show_question()

    def show_question(self):
        self.clear_screen()
        q_data = self.questions[self.current_question]

        tk.Label(self.container, text=f"Current Streak: {self.streak}", font=("Arial", 12, "bold"), fg="green").pack(
            pady=5)
        tk.Label(self.container, text=q_data["text"], font=("Arial", 16, "bold"), wraplength=500).pack(pady=10)

        try:
            self.q_img = tk.PhotoImage(file=q_data["image"])
            tk.Label(self.container, image=self.q_img).pack(pady=10)
        except:
            tk.Label(self.container, text="[Question Image]", height=10).pack()

        for option in q_data["options"]:
            tk.Button(self.container, text=option, font=("Arial", 12), width=30,
                      command=lambda opt=option: self.check_answer(opt)).pack(pady=5)

    def check_answer(self, choice):
        # Sudden Death Logic
        if choice == self.questions[self.current_question]["answer"]:
            self.streak += 1
            self.current_question += 1

            # Check if there are more questions
            if self.current_question < len(self.questions):
                self.show_question()
            else:
                self.show_end_screen("Perfect Game!")
        else:
            # Wrong answer triggers immediate end
            self.show_end_screen("Game Over!")

    def show_end_screen(self, title_text):
        self.clear_screen()
        tk.Label(self.container, text=title_text, font=("Arial", 24, "bold"), fg="red").pack(pady=20)
        tk.Label(self.container, text=f"{self.username}'s Final Streak", font=("Arial", 18)).pack()

        # Streak display
        tk.Label(self.container, text=str(self.streak), font=("Arial", 60, "bold"), fg="blue").pack(pady=10)

        try:
            self.end_img = tk.PhotoImage(file="finish.png")
            tk.Label(self.container, image=self.end_img).pack(pady=10)
        except:
            tk.Label(self.container, text="🏁", font=("Arial", 80)).pack()

        tk.Button(self.container, text="Try Again", command=self.restart_quiz).pack(pady=30)

    def restart_quiz(self):
        self.streak = 0
        self.current_question = 0
        self.show_home()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
