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
        self.num_circles = 1  # Initial number of circles
        self.mode = 1  # Start with mode 1

        self.circles = []
        self.lines = []
        self.create_elements()
        self.update_circles()
        self.create_text_instructions()

        self.master.bind("<Up>", self.increase_circles)
        self.master.bind("<Down>", self.decrease_circles)
        self.master.bind("<Right>", self.increase_speed)
        self.master.bind("<Left>", self.decrease_speed)
        self.master.bind("<Return>", self.toggle_lines)  # Enter key to toggle lines
        self.master.bind("<Escape>", self.exit_program)

        self.animate()

    def create_elements(self):
        # Create center dot
        self.center_dot = self.canvas.create_oval(self.center_x-5, self.center_y-5, 
                                                  self.center_x+5, self.center_y+5, 
                                                  fill="white", outline="white")

    def update_circles(self):
        # Clear existing circles and lines
        for circle in self.circles:
            self.canvas.delete(circle)
        for line in self.lines:
            self.canvas.delete(line)
        self.circles.clear()
        self.lines.clear()

        # Create new circles
        for i in range(self.num_circles):
            circle = self.canvas.create_oval(0, 0, 10, 10, fill="white", outline="white")
            self.circles.append(circle)

    def create_text_instructions(self):
        # Create text instructions
        self.speed_text = self.canvas.create_text(20, 20, text=f"Speed: {self.speed:.2f}", 
                                                  fill="white", anchor="nw", font=("Arial", 14))
        
        self.speed_instruction = self.canvas.create_text(20, 50, 
                                                         text="UP/DOWN: Change number of circles",
                                                        fill="white", anchor="nw", font=("Arial", 12))

        self.speed_instruction = self.canvas.create_text(20, 80, 
                                                         text="RIGHT/LEFT: Change speed", 
                                                         fill="white", anchor="nw", font=("Arial", 12))

        self.exit_instruction = self.canvas.create_text(20, 110, 
                                                        text="ESC: Exit", 
                                                        fill="white", anchor="nw", font=("Arial", 12))

    def animate(self):
        self.angle += self.speed
        for i, circle in enumerate(self.circles):
            angle_offset = (2 * math.pi / self.num_circles) * i
            x = self.center_x + self.radius * math.cos(self.angle + angle_offset)
            y = self.center_y + self.radius * math.sin(self.angle + angle_offset)
            self.canvas.coords(circle, x-5, y-5, x+5, y+5)

        # Draw lines if mode is 2
        if self.mode == 2:
            for i in range(self.num_circles):
                x1 = self.center_x + self.radius * math.cos(self.angle + (2 * math.pi / self.num_circles) * i)
                y1 = self.center_y + self.radius * math.sin(self.angle + (2 * math.pi / self.num_circles) * i)
                for j in range(i + 1, self.num_circles):
                    x2 = self.center_x + self.radius * math.cos(self.angle + (2 * math.pi / self.num_circles) * j)
                    y2 = self.center_y + self.radius * math.sin(self.angle + (2 * math.pi / self.num_circles) * j)
                    line = self.canvas.create_line(x1, y1, x2, y2, fill="white")
                    self.lines.append(line)

        self.master.after(16, self.animate)  # ~60 FPS

    def increase_circles(self, event):
        self.num_circles += 1
        self.update_circles()

    def decrease_circles(self, event):
        if self.num_circles > 1:
            self.num_circles -= 1
            self.update_circles()

    def increase_speed(self, event):
        self.speed += 0.01
        self.update_speed_display()

    def decrease_speed(self, event):
        self.speed = max(0.01, self.speed - 0.01)
        self.update_speed_display()

    def update_speed_display(self):
        self.canvas.itemconfig(self.speed_text, text=f"Speed: {self.speed:.2f}")

    def toggle_lines(self, event):
        self.mode = 3 - self.mode  # Toggle between mode 1 and 2
        self.update_circles()  # Redraw circles and lines

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
