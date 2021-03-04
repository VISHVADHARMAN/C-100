class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.company=company
        self.speed_limit=speed_limit
        self.model=model
    
    def start(self):
        print("Started")

    def stop(self):
        print("Stop")
    
    def accelerate(self):
        print("Accelerating")
    
    def change_gear(self):
        print("Gear Changed")

audi=Car("A6","red","audi","80")
audi.color
print(audi.color)
print(audi.model)