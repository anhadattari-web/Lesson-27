class Bird:
    def __init__(self):
        print("The bird is ready")
    def whoisthis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
class Penguins(Bird):
    def __init__(self):
        super().__init__()
        print("The penguin is ready")
    def whoisthis(self):
        print("Penguin")
    def run(self):
        print("Run faster")
peng= Penguins()
peng.whoisthis()
peng.swim()
peng.run()
