class Garden (): 
    def __init__(self): 
        self.bed =  [" ", " "," ", " "]
        self.plant_one = None
        self.plant_two = None
        self.plant_three = None
        self.plant_four = None
        self.index = None
        self.days = 1
        self.all = [self.plant_one, self.plant_two, self.plant_three, self.plant_four]

    def print_bed(self):
            print (self.bed)
            print ("  1    2    3    4")

    def fill_bed(self):
        plant_number = int(input("What spot do you want to plant?"))
        self.index = plant_number
        self.bed[plant_number - 1]= "🌱"
    
  
    def bloom_calc (self):
        for self.plant in self.all:
            print (self.plant)
            # if plant == None:
            #     continue
            # if plant.bloom_days > 0: 
            #     plant.bloom_days -= 1
            # elif plant.bloom_days == 0: 
            #     print ("Your flower has bloomed!")
            #     flower_bloom(self, plant)

    def flower_bloom (self, plant):
        self.bed[plant.index] = plant.display


class Flower():
    def __init__ (self, kind):
        self.kind = kind
        
        if kind == "Hibiscus":
            self.index = None
            self.display = '🌺'
            self.bloom_days = 4
            self.water_days = 5
            self.water_level = 30
        
        if kind == "Sunflower":
            self.index = None
            self.display = '🌻'
            self.bloom_days = 3
            self.water_days = 1
            self.water_level = 100
        
        
        if kind  == "Cherry Blossom":
            self.index = None
            self.display = '🌸'
            self.bloom_days = 2
            self.water_days= 2
            self.water_level = 50
    
        
        

new_plot = Garden()


def set_flower_from_user ():

    type_of_plant = input("""
            New sunflowers? Press s.
            New Cherry Blossom? Press c.
             New Hibiscus? Press h.\n""")
    

    if type_of_plant == "s": 
        print ("You picked a\033[93m sunflower \033[00m.\n")
        print ("\033[93mSunflowers \033[00mneed to be watered every day.\n")
        print ("\033[93mSunflowers \033[00mwill bloom after 4 days.\n")
        new_plot.fill_bed()
        new_plot.print_bed()
        plant_number= (new_plot.index)
        kind = "Sunflower"
        
    if type_of_plant == "c":
        print ("You picked a\033[95m cherry blossom\033[00m.\n")
        print ("\033[95m Cherry blossoms \033[00mneed to be watered every 2 days.\n")
        print ("\033[95m Cherry blossoms \033[00mwill bloom after 5 days.\n")
        new_plot.fill_bed()
        new_plot.print_bed()
        plant_number= (new_plot.index)
        kind = "Cherry Blossom"

    if type_of_plant == "h": 
        print ("You picked a\033[91m hibiscus\033[00m.\n")
        print ("\033[91m Hibiscuses \033[00mneed to be watered every 3 days.\n")
        print ("\033[91m Hibiscuses \033[00mwill bloom after 3 days.\n")
        new_plot.fill_bed()
        new_plot.print_bed()
        plant_number= (new_plot.index)
        kind = "Hibiscus"

       
    if plant_number == 1: 
        new_plot.plant_one = Flower(kind)
        new_plot.plant_one.index = 0
    
    if plant_number == 2: 
        new_plot.plant_two = Flower(kind)
        new_plot.plant_two.index = 1
        
    if plant_number == 3: 
        new_plot.plant_three = Flower(kind)
        new_plot.plant_two.index = 2
        
    if plant_number == 4: 
        new_plot.plant_four = Flower(kind)
        new_plot.plant_two.index = 3

    else: 
        print ("Please select a flower from the list!")

def water_plants(number):
        if number ==1:
            new_plot.plant_one.water_level += 10
            print (F"Your water level is {new_plot.plant_one.water_level}!")
        if number == 2:
            new_plot.plant_two.water_level +=10
            print (F"Your water level is {new_plot.plant_two.water_level}!")
        if number == 3: 
            new_plot.plant_three.water_level += 10
            print (F"Your water level is {new_plot.plant_three.water_level}!")
        if number == 4: 
            new.plot.plant_four.water_level +=10
            print (F"Your water level is {new_plot.plant_four.water_level}!")

def get_water_levels():
    
    if new_plot.plant_one == None: 
        print ("Spot #1 has not been planted.")
    
    if new_plot.plant_one !=None: 
        print (F"Plant #1 has a water level of {new_plot.plant_one.water_level}\n.")
    
    if new_plot.plant_two == None: 
         print ("Spot #2 has not been planted.")

    if new_plot.plant_two!= None: 
        print (F"Plant #2 has a water level of {new_plot.plant_two.water_level}\n.")
    
    if new_plot.plant_three == None: 
        print ("Spot #3 has not been planted.\n")

    if new_plot.plant_three != None: 
        print (F"Plant #3 has a water level of {new_plot.plant_three.water_level}\n.")
        
    if new_plot.plant_four == None: 
        print ("Spot #4 has not been planted.\n")
    
    if new_plot.plant_four != None:
        print (F"Plant #4 has a water level of {new_plot.plant_four.water_level}\n.")


while True: 
    print ("Hey there! Welcome to your garden!\n")
    print (f"Today is day {new_plot.days} on DC_Crossing.")
    
    new_plot.print_bed()
    
    next_move = int (input ("""
    What would you like to do?
    1.) New plant
    2.) Check plant levels
    3.) Water a plant
    4.) try your luck
    5.) quit game 
     """))
    
    if next_move == 1: 
        set_flower_from_user()
   
    if next_move == 2: 
        get_water_levels()
    
    if next_move == 3: 
       plant_to_water = int(input("What plant do you want to water?"))
       water_plants(plant_to_water)

    if next_move == 5: 
        print ("See you next time! :)")
        exit ()

    new_plot.days += 1
    print (new_plot.plant_one.bloom_days)
    print(new_plot.plant_one.display)
    



