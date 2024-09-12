class calc:
    def __init__(self, x , y) -> None:
        self.x = x
        self.y = y
    def total(self):
        t = self.x + self.y
        return t
    def difference(self):
        d = self.x - self.y
        return d
if __name__ == '__main__':
    my_obj = calc(3,5)
    print(my_obj.total())
    print(my_obj.difference())
