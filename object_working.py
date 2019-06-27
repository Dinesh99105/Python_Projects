class Egg:
     def __init__(self,kind = "fried"):
        self.kind = kind
     def whatkind(self):
        return self.kind
def main():
    fried = Egg()
    scramble = Egg("scramble")
    print(scramble.whatkind())
    print(fried.whatkind())
if __name__ == "__main__": main()
