class Garden (): 
    def __init__(self): 
        self.bed =  [[" ", " "], 
                     [" ", " "]]
       
        self.number_of_plants = 0
    
    def print_plot(self): 
        for item in self.bed: 
            print (item)

    def water_plant(self):
        self.water_level +=10
        self.height += 1
        print(F"Your plants water level is now {self.water_level}.")
        print(F"Your plants water level is now {self.height} inches.")
    
    def add_plant(self):
        start = 0
        while start < 2: 
            
            for i in range (0,2):
                if self.bed[start][i]== " ":
                    self.bed[start][i] = '🌱'
                    self.number_of_plants +=1
                    start =2
                    break

                else: 
                    print ("\033[93m ***** Your bed is full! ***** \033[00m")
                    
                
            start += 1
    
    def create_plant_name(self): 
       plant_name = Flower(F"plant{self.number_of_plants}")


class Flower():
    def __init__(self, name): 
        self.name = name
        self.display_bud = '🌱'
        self.display_flower = None
        self.age = 0
        self.height = 0
    
class Cherry_Blossoms(Flower):
    def __init__ (name):
        super().__init__(name,display_bud,display_flower,age)
        self.name = "Cherry Blossom"
        self.display_flower = '🌸'
        self.bloomdays = 7
        self.watering = 2

class Sunflower (Flower): 
    def __init__ (self):
        super().__init__(display_bud,display_flower,age)
        self.name = "Sunflower"
        self.display_flower = '🌻'
        self.bloomdays = 6
        self.watering = 1

class Hibiscus (Flower): 
    def __init__ (self):
        super().__init__(display_bud,display_flower,age)
        self.name = "Hibiscus"
        self.display_flower = '🌺'
        self.bloomdays = 5
        self.watering = 5

new_plot = Garden()  
while True: 
    print ("Hey there! Welcome to your garden!\n")
    
    print (new_plot.print_plot())
    
    next_move = int (input ("""
    What would you like to do today?
    1.) New plant
    2.) Check plant levels
    3.) Water a plant
    4.) try your luck
    5.) quit game 
     """))

    if next_move == 1: 

        type_of_plant = input("""
                New sunflowers? Press s.
                New Cherry Blossom? Press c.
                New Hibiscus? Press h.\n""")
        
        new_plot.add_plant()
        
        if type_of_plant == "s": 
            print ("You picked a\033[93m sunflower \033[00m \n")
            print ("\033[93mSunflowers \033[00mneed to be watered every day.\n")
            print ("\033[93mSunflowers \033[00mwill bloom after 5 days.\n")

        
        if type_of_plant == "c": 
            print ("You picked a\033[95m cherry blossom\033[00m\n")
            print ("Cherry blossoms need to be watered every 2 days.\n\nCherry Blossoms will bloom after 7 days.\n")


        if type_of_plant == "h": 
            print ("You picked a\033[91m hibiscus \033[00m\n")
            print ("Hibiscuses need to be watered every 3 days.\n\nCherry Blossoms will bloom after 6 days.\n")

    if next_move == 3: 

        plant_to_water = int(input ('What plant do you want to water?\n'))
    
    if next_move ==4: 
        print ("you lost the game!")
    if next_move ==5: 
        exit()
            
    
    