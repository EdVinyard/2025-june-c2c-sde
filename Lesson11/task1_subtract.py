class Subtract:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left - self.right

print(Subtract(2, 1).evaluate())
print(Subtract(1, 2).evaluate())
