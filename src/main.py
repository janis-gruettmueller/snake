import time
import sys
import random
from tkinter import *


WIDTH = 600
HEIGHT = 600
SCALE = 20
FRAME_RATE = 0.1

root = Tk()
board = Canvas(root, width=WIDTH, height=HEIGHT, bg="grey")

def main():
    board.pack()

    snake = Snake()
    snake.update()

    root.mainloop()
    

class Food():
    def __init__(self):
        self.pos = (random.randint(0, int(WIDTH/SCALE - 1)), random.randint(0, int(HEIGHT/SCALE - 1)))

    def show(self):
        return board.create_rectangle(self.pos[0] * SCALE, self.pos[1] * SCALE, self.pos[0] * SCALE + SCALE, self.pos[1] * SCALE + SCALE, fill="red")


class Snake():
    def __init__(self):
        root.bind("<Left>", self.move_left)
        root.bind("<Right>", self.move_right)
        root.bind("<Up>", self.move_up)
        root.bind("<Down>", self.move_down)

        self.speed = (0, 0)
        self.body = [(WIDTH/(2*SCALE), HEIGHT/(2*SCALE))]

    def set_direction(self, x, y): 
        self.speed = (x, y)

    def move_left(self, event): 
        self.set_direction(-1, 0)

    def move_right(self, event): 
        self.set_direction(1, 0)

    def move_up(self, event): 
        self.set_direction(0, -1)

    def move_down(self, event): 
        self.set_direction(0, 1)

    def eat(self, food):
        self.body.append((food[0] - self.speed[0], food[1] - self.speed[1]))


    def is_collision(self):
        # wall collision
        if not (0 <= self.body[0][0] <= WIDTH/SCALE - 1 and 0 <= self.body[0][1] <= HEIGHT/SCALE - 1):
            return True
        
        # body collision
        
        
        return False


    def show(self, pos):
        return board.create_rectangle(pos[0] * SCALE, pos[1] * SCALE, pos[0] * SCALE + SCALE, pos[1] * SCALE + SCALE, fill="white")
    
    def update_pos(self):
        if len(self.body) > 1:
            for i in range(len(self.body)-1, 0, -1):
                self.body[i] = self.body[i - 1]

        self.body[0] = (self.body[0][0] + self.speed[0], self.body[0][1] + self.speed[1])


    def update(self):
        food = Food()
        food_obj = food.show()
        snake_obj = []

        while True:
            for pos in self.body:
                snake_obj.append(self.show(pos))

            self.update_pos()

            if self.is_collision():
                sys.exit("Game Over!")

            if self.body[-1] == food.pos:
                self.eat(food.pos)
                food = Food()

                board.delete(food_obj)
                food_obj = food.show()

            board.update()

            for obj in snake_obj:
                board.delete(obj)

            snake_obj.clear()

            time.sleep(FRAME_RATE)


if __name__ == "__main__":
    main()