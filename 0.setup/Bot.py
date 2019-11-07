class Bot:

    def __init__(self, name):
        self.name = name
        self.age = 0
        self.energy = 100
        self.shield = 100

    def display_name(self):
        print("My name is", self.name)

beep = Bot("""
  ____                  
 |  _ \                 
 | |_) | ___  ___ _ __  
 |  _ < / _ \/ _ \ '_ \ 
 | |_) |  __/  __/ |_) |
 |____/ \___|\___| .__/ 
                 | |    
                 |_|    """)

beep.display_name()
