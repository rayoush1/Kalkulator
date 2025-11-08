class Calculator:
    """A class to represent calculators"""
    def __init__(self, op1: float, op2: float):
        self.__op1 = op1
        self.__op2 = op2

    def sum(self) -> float:
        """Sum two numbers"""
        try:
            return self.__op1 + self.__op2
        except:
            print("Error!")

    def subtract(self) -> float:
        """Subtract two numbers"""
        try:
            return self.__op1 - self.__op2
        except:
            print("Error!")

    def multiply(self) -> float:
        """Multiply two numbers"""
        try:
            return self.__op1 * self.__op2
        except:
            print("Error!")

    def divide(self) -> float:
        """Divide two numbers"""
        if self.__op2 == 0:
            print("Division by zero")
        else:
            try:
                return self.__op1 / self.__op2
            except:
                print("Error!")


def main(): # pragma: no cover
    #Example code
    calculator = Calculator(op1=64, op2=8)

    print("Our calculator in action:")
    print("64+8=",calculator.sum())
    print("64-8=",calculator.subtract())
    print("64*8=",calculator.multiply())
    print("64/8=",calculator.divide())

if __name__ == "__main__": # pragma: no cover
    main()