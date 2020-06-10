class Garden (): 
    def __init__(self, plant): 
        self.plant = plant
        self.height = 0
        self.water_level = 50

    def water_plant(self):
        self.water_level +=10
        print(self.water_level)
        self.height +=1
    

while True: 

    garden_plot = [[" ", " "], 
                   [" ", " "]]

    def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
    def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
    print ("Hey there! Welcome to your garden!\n")
   
    
    for item in garden_plot: 
        print (item)

    print ("\n")

    next_move = int (input ("""
    What would you like to do today?
    1.) New plant
    2.) Check plant levels
    3.) Water a plant
    4.) try your luck
    5.) quit game """))

    if next_move == 1: 
        type_of_plant = input("""
                New sunflowers? Press s.
                New Cherry Blossom? Press c.
                New Hibiscus? Press h.\n""")
        
        if type_of_plant == "s": 
            print ("You picked a\033[93m sunflower \033[00m \n")
            print ("Sunflowers need to be watered every day.\n Sunflowers will loom after 5 days.")
            new_plant = Garden("sunflower")
            exit()
    