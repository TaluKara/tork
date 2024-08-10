import tkinter as tk
import math
import sys

class CircularAnimation:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, bg="black", width=1920, height=1080)
        self.canvas.pack()

        self.center_x, self.center_y = 960, 540
        self.radius = 300
        self.angle = 0
        self.speed = 0.05
        self.mode = 1  # Start with mode 1
        self.theme = "dark"  # Start with dark theme

        self.create_elements()
        self.create_text_instructions()

        self.master.bind("<Up>", self.increase_speed)
        self.master.bind("<Down>", self.decrease_speed)
        self.master.bind("<Left>", self.switch_theme)
        self.master.bind("<Right>", self.switch_mode)
        self.master.bind("<Escape>", self.exit_program)

        self.animate()

    def create_elements(self):
        # Center dot
        self.center_dot = self.canvas.create_oval(self.center_x-5, self.center_y-5, 
                                                  self.center_x+5, self.center_y+5, 
                                                  fill="white", outline="white")

        self.moving_dot = self.canvas.create_oval(0, 0, 10, 10, fill="white", outline="white")
        self.rotating_line = self.canvas.create_line(self.center_x, self.center_y, 
                                                     self.center_x + self.radius, self.center_y, 
                                                     fill="white")

    def create_text_instructions(self):
        self.speed_text = self.canvas.create_text(960, 50, text=f"Speed: {self.speed:.2f}", 
                                                  fill="white", anchor="center", font=("Arial", 20))
        
        self.speed_instruction = self.canvas.create_text(960, 100, 
                                                         text="Use UP and DOWN arrow keys to change speed", 
                                                         fill="white", anchor="center", font=("Arial", 16))

        self.mode_instruction = self.canvas.create_text(960, 980, 
                                                        text="Press RIGHT arrow key to switch mode", 
                                                        fill="white", anchor="center", font=("Arial", 24))

        self.theme_instruction = self.canvas.create_text(960, 1020, 
                                                         text="Press LEFT arrow key to switch color theme", 
                                                         fill="white", anchor="center", font=("Arial", 24))

        self.exit_instruction = self.canvas.create_text(960, 1060, 
                                                        text="Press ESC to exit", 
                                                        fill="white", anchor="center", font=("Arial", 24))

    def animate(self):
        self.angle += self.speed
        x = self.center_x + self.radius * math.cos(self.angle)
        y = self.center_y + self.radius * math.sin(self.angle)

        if self.mode == 1:
            self.canvas.coords(self.moving_dot, x-5, y-5, x+5, y+5)
            self.canvas.itemconfig(self.moving_dot, state="normal")
            self.canvas.itemconfig(self.rotating_line, state="hidden")
        else:
            self.canvas.coords(self.rotating_line, self.center_x, self.center_y, x, y)
            self.canvas.itemconfig(self.moving_dot, state="hidden")
            self.canvas.itemconfig(self.rotating_line, state="normal")

        self.master.after(16, self.animate)  # ~60 FPS

    def increase_speed(self, event):
        self.speed += 0.01
        self.update_speed_display()

    def decrease_speed(self, event):
        self.speed = max(0.01, self.speed - 0.01)
        self.update_speed_display()

    def update_speed_display(self):
        self.canvas.itemconfig(self.speed_text, text=f"Speed: {self.speed:.2f}")

    def switch_mode(self, event):
        self.mode = 3 - self.mode  # Switch between 1 and 2

    def switch_theme(self, event):
        if self.theme == "dark":
            self.theme = "light"
            bg_color, fg_color = "white", "black"
        else:
            self.theme = "dark"
            bg_color, fg_color = "black", "white"
        
        self.canvas.config(bg=bg_color)
        
        # Update shapes
        for item in [self.center_dot, self.moving_dot]:
            self.canvas.itemconfig(item, fill=fg_color, outline=fg_color)
        self.canvas.itemconfig(self.rotating_line, fill=fg_color)
        
        # Update text
        for item in [self.speed_text, self.speed_instruction, 
                     self.mode_instruction, self.theme_instruction, 
                     self.exit_instruction]:
            self.canvas.itemconfig(item, fill=fg_color)

    def exit_program(self, event):
        self.master.destroy()
        sys.exit()

def main():
    root = tk.Tk()
    root.title("Circular Animation")
    root.attributes('-fullscreen', True)

    app = CircularAnimation(root)
    root.mainloop()

if __name__ == "__main__":
    main()
