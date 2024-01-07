import time
import random
from tkinter import *


WIDTH = 600
HEIGHT = 600
SCALE = 20
FRAME_RATE = 0.15

def main():
    root = Tk()
    board = Canvas(root, width=WIDTH, height=HEIGHT, bg="grey")
    board.pack()

    snake = Snake(board)
    snake.update()

    root.mainloop()
    

class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        self.pos = (random.randint(0, WIDTH-SCALE) * SCALE, random.randint(0, HEIGHT-SCALE) * SCALE)

    def show(self):
        self.canvas.create_rectangle(self.pos[0] * SCALE, self.pos[1] * SCALE, (self.pos[0] + SCALE) * SCALE, (self.pos[1] + SCALE) * SCALE, fill="red")
    
    def get_new_position(self):
        return (random.randint(0, WIDTH-SCALE) * SCALE, random.randint(0, HEIGHT-SCALE) * SCALE)


class Snake():
    def __init__(self, canvas):
        self.canvas = canvas
        canvas.bind("<Left>", self.move_left)
        canvas.bind("<Right>", self.move_right)
        canvas.bind("<Up>", self.move_up)
        canvas.bind("<Down>", self.move_down)

        self.head = (WIDTH/2 - SCALE, HEIGHT/2 - SCALE)
        self.speed = (0, 0)
        self.body = []


    def set_direction(self, x, y): self.speed = (x, y)

    def move_left(self): self.set_direction(-1, 0)

    def move_right(self): self.set_direction(1, 0)

    def move_up(self): self.set_direction(0, -1)

    def move_down(self): self.set_direction(0, 1)

    def eat(self, food): self.body.append(food)


    def is_collision(self):
        # wall collision
        if not 0 <= self.head[0] <= WIDTH - SCALE and 0 <= self.head[1] <= HEIGHT - SCALE:
            return True
        
        # body collision
        if self.head in self.body:
            return True
        
        return False


    def show(self):
        self.canvas.create_rectangle(self.head[0] * SCALE, self.head[1] * SCALE, (self.head[0] + SCALE) * SCALE, (self.head[1] + SCALE) * SCALE, fill="white")
        
        if len(self.body) > 0:
            for pos in self.body:
                self.canvas.create_rectangle(pos[0], pos[1], pos[0] + SCALE, pos[1] + SCALE, fill="white")


    def update(self):
        food = Food(self.canvas)

        self.show()
        food.show()

        food_pos = food.pos

        while True:
            self.head += self.speed * SCALE
            if len(self.body) > 0:
                for pos in self.body:
                    pos += self.speed * SCALE

            if self.is_collision():
                print("Game Over!")
                break

            if self.head == food_pos:
                self.eat(food.pos)
                food_pos = food.get_new_position()

            self.canvas.update()
            self.show()

            time.sleep(FRAME_RATE)


if __name__ == "__main__":
    main()