class Calulator:
    def __init__(self ,num1,num2):
        self.num1 = num1
        self.num2 = num2
        pass

    def add(self):
        result = self.num1 + self.num2
        return result

    def sub(self):
        result = self.num1 - self.num2
        return result

    def multi(self):
        result = self.num1 * self.num2
        return result

    def divide(self):
        result = self.num1 / self.num2
        return result
