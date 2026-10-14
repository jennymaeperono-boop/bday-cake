import tkinter as tk


WIDTH = 640
HEIGHT = 540
BACKGROUND = "#09090b"


class BirthdayCake:
    def __init__(self, root):
        self.root = root
        self.root.title("Birthday Cake")
        self.root.resizable(False, False)
        self.frame = tk.Frame(root, bg=BACKGROUND)
        self.frame.pack()

        self.canvas = tk.Canvas(
            self.frame,
            width=WIDTH,
            height=HEIGHT,
            bg=BACKGROUND,
            highlightthickness=0,
        )
        self.canvas.pack()

        self.candles_lit = True
        self.animation_frame = 0
        self.button = tk.Button(
            self.frame,
            text="Blow out the candles",
            command=self.toggle_candles,
            font=("Georgia", 11, "bold"),
            bg="#c9a45c",
            fg="#17130b",
            activebackground="#e4c783",
            relief="flat",
            padx=18,
            pady=8,
            cursor="hand2",
        )
        self.button.pack(pady=(0, 14))
        self.root.bind("<space>", self.handle_spacebar)

        self.animate()

    def toggle_candles(self):
        self.candles_lit = not self.candles_lit
        if self.candles_lit:
            self.button.config(text="Blow out the candles")
        else:
            self.button.config(text="Light the candles")

    def handle_spacebar(self, event):
        if event.keysym == "space":
            self.toggle_candles()

    def draw_background(self):
        canvas = self.canvas
        canvas.create_oval(115, 112, 525, 488, fill="#111113", outline="")
        canvas.create_line(106, 91, 238, 91, fill="#554324", width=1)
        canvas.create_line(402, 91, 534, 91, fill="#554324", width=1)
        canvas.create_text(320, 91, text="✦", fill="#c9a45c", font=("Georgia", 12))
        details = (
            (77, 145, 2), (552, 142, 2), (102, 235, 1), (538, 246, 1),
            (124, 365, 2), (516, 370, 2), (164, 119, 1), (480, 122, 1),
            (81, 416, 1), (559, 420, 1),
        )
        for index, (x, y, radius) in enumerate(details):
            color = "#c9a45c" if (index + self.animation_frame // 7) % 3 else "#76613a"
            self.canvas.create_oval(
                x - radius, y - radius, x + radius, y + radius,
                fill=color, outline="",
            )

        canvas.create_line(55, 34, 55, 505, fill="#29251e", width=1)
        canvas.create_line(585, 34, 585, 505, fill="#29251e", width=1)

    def draw_cake(self):
        canvas = self.canvas
        canvas.create_text(
            WIDTH / 2, 43,
            text="HAPPY BIRTHDAY",
            fill="#e1c27b",
            font=("Georgia", 25, "bold"),
        )
        if self.candles_lit:
            canvas.create_text(
                WIDTH / 2, 69,
                text="A night to celebrate you",
                fill="#aaa39a",
                font=("Georgia", 11, "italic"),
            )
        else:
            canvas.create_text(
                WIDTH / 2, 86,
                text="MAYANGGGG",
                fill="#f1dfb4",
                font=("Georgia", 16, "bold"),
            )

        # Layered charcoal cake with understated gold detailing.
        canvas.create_oval(143, 437, 497, 475, fill="#6a552f", outline="#c9a45c", width=2)
        canvas.create_oval(153, 435, 487, 465, fill="#171719", outline="#9d7b40", width=1)

        canvas.create_rectangle(166, 351, 474, 439, fill="#211e1d", outline="#b18d4e", width=2)
        canvas.create_oval(166, 332, 474, 370, fill="#302b26", outline="#c9a45c", width=2)
        canvas.create_line(169, 365, 471, 365, fill="#d3b46f", width=3)
        canvas.create_line(169, 374, 471, 374, fill="#6d5732", width=1)
        canvas.create_line(175, 429, 465, 429, fill="#9d7b40", width=2)
        for x in (191, 237, 283, 329, 375, 421, 455):
            canvas.create_oval(x - 2, 393, x + 2, 397, fill="#d8bd81", outline="")

        canvas.create_rectangle(211, 257, 429, 352, fill="#292625", outline="#b18d4e", width=2)
        canvas.create_oval(211, 241, 429, 275, fill="#39322a", outline="#d3b46f", width=2)
        canvas.create_line(213, 272, 427, 272, fill="#d3b46f", width=3)
        canvas.create_line(214, 281, 426, 281, fill="#6d5732", width=1)
        canvas.create_line(216, 341, 424, 341, fill="#9d7b40", width=2)
        for x in (235, 275, 315, 355, 395):
            canvas.create_oval(x - 2, 307, x + 2, 311, fill="#d8bd81", outline="")
            canvas.create_oval(x - 2, 326, x + 2, 330, fill="#8b6e3d", outline="")

        # Small rose-gold accents soften the formal look.
        for x, y in ((190, 408), (450, 408), (228, 293), (412, 293)):
            canvas.create_oval(x - 5, y - 2, x + 5, y + 2, fill="#b77b72", outline="")
            canvas.create_oval(x - 2, y - 5, x + 2, y + 5, fill="#d3a08e", outline="")
            canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="#3a2927", outline="")

        # Slim black candles with gold bands.
        candle_xs = (258, 289, 320, 351, 382)
        for x in candle_xs:
            canvas.create_rectangle(x - 5, 202, x + 5, 249, fill="#111112", outline="#c9a45c")
            canvas.create_line(x - 4, 215, x + 4, 215, fill="#d3b46f", width=2)
            canvas.create_line(x - 4, 235, x + 4, 235, fill="#d3b46f", width=2)
            canvas.create_line(x, 202, x, 195, fill="#c9a45c", width=2)
            if self.candles_lit:
                self.draw_flame(x, 192)
            elif self.animation_frame % 8 < 4:
                canvas.create_arc(
                    x - 5, 183, x + 5, 196,
                    start=35, extent=115, style=tk.ARC,
                    outline="#b8b4aa", width=2,
                )

        canvas.create_text(
            WIDTH / 2, 495,
            text="Make a wish" if self.candles_lit else "Wishing you a beautiful year ahead",
            fill="#d3b46f",
            font=("Georgia", 15, "italic"),
        )

    def draw_flame(self, x, y):
        flicker = self.animation_frame % 4
        width = 5 + flicker
        height = 13 + (flicker % 3) * 2
        self.canvas.create_oval(
            x - width, y - height, x + width, y + height,
            fill="#cf8b42", outline="",
        )
        self.canvas.create_oval(
            x - width // 2, y - height + 4,
            x + width // 2, y + height - 3,
            fill="#f4d99a", outline="",
        )

    def animate(self):
        self.canvas.delete("all")
        self.draw_background()
        self.draw_cake()
        self.animation_frame += 1
        self.root.after(180, self.animate)


def main():
    root = tk.Tk()
    BirthdayCake(root)
    root.mainloop()


if __name__ == "__main__":
    main()
