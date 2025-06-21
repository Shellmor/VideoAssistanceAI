import tkinter as tk

class NotificationWindow(tk.Toplevel):
    def __init__(self, master, text='', timeout=50000):
        super().__init__(master)
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.configure(bg='#1e1e1e')
        self.attributes('-alpha', 0.95)

        self.label = tk.Label(
            self,
            text=text,
            bg='#1e1e1e',
            fg='white',
            font=('Segoe UI', 14, 'bold'),
            padx=20,
            pady=15,
            justify='left',
            wraplength=600
        )
        self.label.pack()

        close_btn = tk.Button(
            self,
            text='✕',
            command=self.destroy,
            bg='#2e2e2e',
            fg='white',
            bd=0,
            activebackground='#3e3e3e',
            activeforeground='white',
            font=('Segoe UI', 8)
        )
        close_btn.place(relx=1.0, rely=0.0, anchor='ne')

        self.update_idletasks()
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()

        screen_width = self.winfo_screenwidth()
        x = (screen_width // 2) - (width // 2)
        y = 50

        self.geometry(f"{width}x{height}+{x}+{y}")

        self.label.bind("<ButtonPress-1>", self.start_move)
        self.label.bind("<B1-Motion>", self.do_move)

        self.after(timeout, self.destroy)

    def start_move(self, event):
        self._x = event.x
        self._y = event.y

    def do_move(self, event):
        x = self.winfo_pointerx() - self._x
        y = self.winfo_pointery() - self._y
        self.geometry(f"+{x}+{y}")

class WindowManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.current_window = None

    def show_window(self, message):
        self.close_window()
        self.current_window = NotificationWindow(self.root, text=message)

    def close_window(self):
        if self.current_window is not None:
            try:
                self.current_window.destroy()
            except Exception:
                pass
            self.current_window = None

    def mainloop(self):
        self.root.mainloop()