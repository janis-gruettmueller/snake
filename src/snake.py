def main():
    return 0


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.body = []

    def eat(self, food): self.append(food)

    def move_left(self): 
        self.x -= 1
        if len(self.body) > 0:
            for part in self.body:
                part[0] -= 1


    def move_right(self):
        self.x += 1
        if len(self.body) > 0:
            for part in self.body:
                part[0] += 1


    def move_up(self):
        self.y -= 1
        if len(self.body) > 0:
            for part in self.body:
                part[1] -= 1


    def move_down(self):
        self.y += 1
        if len(self.body) > 0:
            for part in self.body:
                part[1] += 1


if __name__ == "__main__":
    main()
