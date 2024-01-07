class Robot:
    
    #construktor
    def __init__(self, baterie, delka):
        self.bat = baterie
        self.dl = delka
        self.ukony_kontrola = 100

    def krok_vpred(self):
        print("posunul sem se vpred")
        self.ukony_kontrola-=1
        print(f"Ukonu do kotroly:{self.ukony_kontrola}") 

    def krok_vzad(self):
      print("posunul sem se vzad")
      self.ukony_kontrola-=1     
      print(f"Ukonu do kotroly:{self.ukony_kontrola}")  
    

robot1 = Robot(24,0.6)
robot2 = Robot(70,0.7)


print(robot1.ukony_kontrola)
print(robot1.bat, robot2.dl)

robot1.krok_vpred()
robot1.krok_vzad()
