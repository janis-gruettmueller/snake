import time
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
        
    def get_new_position(self):
        self.pos = (random.randint(0, int(WIDTH/SCALE - 1)), random.randint(0, int(HEIGHT/SCALE - 1)))


class Snake():
    def __init__(self):
        root.bind("<Left>", self.move_left)
        root.bind("<Right>", self.move_right)
        root.bind("<Up>", self.move_up)
        root.bind("<Down>", self.move_down)

        self.head = (WIDTH/(2*SCALE), HEIGHT/(2*SCALE))
        self.speed = (0, 0)
        self.body = []

    def set_direction(self, x, y): self.speed = (x, y)

    def move_left(self, event): 
        self.set_direction(-1, 0)

    def move_right(self, event): self.set_direction(1, 0)

    def move_up(self, event): self.set_direction(0, -1)

    def move_down(self, event): self.set_direction(0, 1)

    def eat(self, food): self.body.append(food)


    def is_collision(self):
        # wall collision
        if not (0 <= self.head[0] <= WIDTH/SCALE - 1 and 0 <= self.head[1] <= HEIGHT/SCALE - 1):
            return True
        
        # body collision
        if self.head in self.body:
            return True
        
        return False


    def show(self, pos):
        return board.create_rectangle(pos[0] * SCALE, pos[1] * SCALE, pos[0] * SCALE + SCALE, pos[1] * SCALE + SCALE, fill="white")


    def update(self):
        food = Food()
        food_pos = food.pos

        snake_obj = []
        food_obj = food.show()

        while True:
            snake_obj.append(self.show(self.head))
            if len(self.body) > 0:
                for i in range(len(self.body)-1):
                    snake_obj.append(self.show(self.body[i]))
                    self.body[i] = (self.body[i][0] + self.speed[0], self.body[i][1] + self.speed[1])
                    
            self.head = (self.head[0] + self.speed[0], self.head[1] + self.speed[1])

            if self.is_collision():
                print("Game Over!")
                break

            if self.head == food_pos:
                self.eat(food_pos)
                food.get_new_position()
                food_pos = food.pos
                
                board.delete(food_obj)
                food_obj = food.show()

            board.update()

            for obj in snake_obj:
                board.delete(obj)

            time.sleep(FRAME_RATE)


if __name__ == "__main__":
    main()