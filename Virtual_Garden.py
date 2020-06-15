import json
from typing import NamedTuple, List
from HighScore import save_score, get_scores, Score


NUMBER_OF_ROUNDS = 7
class Garden (): 
    def __init__(self): 
        self.bed =  [" ", " "," ", " "]
    
        self.plants = {
            "plant_one": None,
            "plant_two": None,
            "plant_three": None,
            "plant_four": None
        }

        self.index = None
        self.money = 0

    def print_bed(self):
            print (self.bed)
            print ("  1    2    3    4")

    def get_valid_fill_bed(self):
        while True:
            try:
                plant_number = int(input("What spot do you want to plant?\n"))
            except ValueError:
                print ("""\033[96m 
    
        ****

        You did not pick a number!

        ****
                        \033[00m"""
                        )
                continue

            if plant_number > 4 or plant_number < 1: 
                print (" please select a valid planter number!\n" )
                continue

            if plant_number >= 1 or plant_number <=4: 
                returned_val = self.replace_flower(plant_number)
                if returned_val == None: 
                    continue
                else: 
                    return returned_val



    def replace_flower (self, plant_number):
            while True:
                if self.bed [plant_number -1] != " ":
                    are_you_sure = (input("There is already a plant in this spot.\n\nDo you want to replace this plant? Yes or No?\n")).lower()
                    if are_you_sure == "yes":
                        return plant_number
                    if  are_you_sure == "no": 
                        return None
                    else: 
                        print ("I didn't quite understand your response.\n")
                        continue
                elif self.bed [plant_number -1] == " ":
                    return plant_number

    def fill_bed(self):
        plant_number = self.get_valid_fill_bed()
        if plant_number != None: 
            self.index = plant_number
            self.bed[plant_number - 1]= "🌱"
    
  
    def bloom_calc (self):
        for plant in self.plants:
            if self.plants[plant] == None:
                continue
            if self.plants[plant].bloom_days > 0: 
                self.plants[plant].bloom_days -= 1
            elif self.plants[plant].bloom_days <= 0 and self.plants[plant].bloom_days > -3: 
                print ("Your flower has bloomed!\n")
                self.bed[self.plants[plant].index] = self.plants[plant].display
                self.plants[plant].bloom_days -= 1
            elif self.plants[plant].bloom_days == -2:
                print ("Uh-oh!Your plant has died!\n")
                self.bed[self.plants[plant].index]= '❌'
            elif self.plants[plant].bloom_days == -3: 
                self.bed[self.plants[plant].index] = " "
                self.plants[plant] = None
    
    def harvest_plants (self):
        for plant in self.plants: 
            if self.plants[plant] == None:
                continue
            if self.plants[plant].bloom_days <= -1 and self.plants[plant].bloom_days > -3:
                self.bed[self.plants[plant].index] = " "
                self.money += self.plants[plant].price
                self.plants[plant] = None


        
        print (F"""
        
        Congratulations!You now have {self.money}💰💰 dollars!
        
        
        """)

    def water_calc(self):
        for plant in self.plants: 
            if self.plants[plant] == None:
                continue
            if self.plants[plant].water_level > 0:
                self.plants[plant].water_level -= 10
            elif self.plants[plant].water_level ==0:
                print ("Eek! You didn't water your plant! Your plant has died!")
                self.bed[self.plants[plant].index]= '❌'
            elif self.plants[plant].bloom_days < 0 : 
                self.bed[self.plants[plant].index] = " "
                self.plants[plant] = None


class Flower():
    def __init__ (self, kind):
        self.kind = kind
        
        if kind == "Hibiscus":
            self.index = None
            self.display = '🌺'
            self.bloom_days = 4
            self.water_added = 30
            self.water_level = 40
            self.price = 6
    
        if kind == "Sunflower":
            self.index = None
            self.display = '🌻'
            self.bloom_days = 2
            self.water_added = 30
            self.water_level = 40
            self.price = 3
        
        
        if kind  == "Cherry Blossom":
            self.index = None
            self.display = '🌸'
            self.bloom_days = 5
            self.water_added = 20
            self.water_level = 30
            self.price = 10
             

new_plot = Garden()


VALID_INPUTS = ["s", "h", "c"]
def get_valid_flower_input():

    while True:
        type_of_plant = input("""
            New sunflower 🌻? Press s.
            New Cherry Blossom 🌸? Press c.
            New Hibiscus 🌺? Press h.\n""")

        if type_of_plant.lower() in VALID_INPUTS:
            return type_of_plant.lower()



def set_flower_from_user ():

    type_of_plant = get_valid_flower_input()

    if type_of_plant == "s": 
        print ("You picked a\033[93m sunflower\033[00m 🌻.\n")
        print ("\033[93mSunflowers \033[00mneed to be watered every 3 days.\n")
        print ("\033[93mSunflowers \033[00mwill bloom after 2 days.\n")
        new_plot.fill_bed()
        new_plot.print_bed()
        plant_number = (new_plot.index)
        kind = "Sunflower"
        
    if type_of_plant == "c":
        print ("You picked a\033[95m cherry blossom\033[00m 🌸.\n")
        print ("\033[95m Cherry blossoms \033[00mneed to be watered every 2 days.\n")
        print ("\033[95m Cherry blossoms \033[00mwill bloom after 5 days.\n")
        new_plot.fill_bed()
        new_plot.print_bed()
        plant_number= (new_plot.index)
        kind = "Cherry Blossom"

    if type_of_plant == "h": 
        print ("You picked a\033[91m hibiscus\033[00m 🌺.\n")
        print ("\033[91m Hibiscuses \033[00mneed to be watered every 3 days.\n")
        print ("\033[91m Hibiscuses \033[00mwill bloom after 4 days.\n")
        new_plot.fill_bed()
        new_plot.print_bed()
        plant_number= (new_plot.index)
        kind = "Hibiscus"

       
    if plant_number == 1: 
        new_plot.plants['plant_one'] = Flower(kind)
        new_plot.plants['plant_one'].index = 0

    
    if plant_number == 2: 
        new_plot.plants['plant_two'] = Flower(kind)
        new_plot.plants['plant_two'].index = 1
        
    if plant_number == 3: 
        new_plot.plants['plant_three'] = Flower(kind)
        new_plot.plants['plant_three'].index = 2
        
    if plant_number == 4: 
        new_plot.plants['plant_four'] = Flower(kind)
        new_plot.plants['plant_four'].index = 3

    else: 
        print ("Please select a flower from the list!\n")

def water_valid_plant():
    
    
    while True:
        try: 
            plant_to_water = int(input("What plant do you want to water?\n"))
        except ValueError: 
            print ("""\033[96m 
    
        ****

        You did not pick a number!

        ****
                        \033[00m"""
                       )
            continue
        
        if plant_to_water > 4 or plant_to_water < 1: 
            print ("""\033[96m 
    
        ****

        Please print a valid number!

        ****
                        \033[00m""")
            continue
        
        if plant_to_water <=4 and plant_to_water >= 1: 
            
            acc = 1
            for item in new_plot.plants:
                if acc == plant_to_water: 
                    if new_plot.plants[item] == None:
                        print ("No plant has been planted here yet \n")
                        break
                    else:
                        return plant_to_water
               
                acc +=1
    
    
def water_plants():
    if (new_plot.plants['plant_one']== None and new_plot.plants['plant_two']==None 
    and new_plot.plants['plant_three']==None and new_plot.plants['plant_four']==None): 
        print ("You do not have any plants!! This move will NOT be counted as one of your days!\n")
        return 1

    number = water_valid_plant()

    if number ==1:
        new_plot.plants['plant_one'].water_level += new_plot.plants['plant_one'].water_added
        print (F"Your water level is {new_plot.plants['plant_one'].water_level}!\n")
    
    if number == 2:
        new_plot.plants['plant_two'].water_level += new_plot.plants['plant_two'].water_added
        print (F"Your water level is {new_plot.plants['plant_two'].water_level}!\n")
        
        
    if number == 3: 
        new_plot.plants['plant_three'].water_level += new_plot.plants['plant_three'].water_added
        print (F"Your water level is {new_plot.plants['plant_three'].water_level}!\n")
    
    if number == 4: 
        new_plot.plants['plant_four'].water_level += new_plot.plants['plant_four'].water_added
        print (F"Your water level is {new_plot.plants['plant_four'].water_level}!\n")
    

    return 0

def get_water_levels():
    
    if new_plot.plants['plant_one'] == None: 
        print ("Spot #1 has not been planted.\n")
    
    if new_plot.plants['plant_one']!=None: 
        print (F"Plant #1 has a water level of {new_plot.plants['plant_one'].water_level}\n.")
    
    if new_plot.plants['plant_two'] == None: 
         print ("Spot #2 has not been planted.\n")

    if new_plot.plants['plant_two']!= None: 
        print (F"Plant #2 has a water level of {new_plot.plants['plant_two'].water_level}\n.")
    
    if new_plot.plants['plant_three'] == None: 
        print ("Spot #3 has not been planted.\n")

    if new_plot.plants['plant_three'] != None: 
        print (F"Plant #3 has a water level of {new_plot.plants['plant_three'].water_level}\n.")
        
    if new_plot.plants['plant_four'] == None: 
        print ("Spot #4 has not been planted.\n")
    
    if new_plot.plants['plant_four'] != None:
        print (F"Plant #4 has a water level of {new_plot.plants['plant_four'].water_level}\n.")





counter = 0
while counter < NUMBER_OF_ROUNDS: 

    if counter ==0: 
        print ("\n\nWell hello there! Welcome to DC_Crossing.\n\nBefore I explain how to play, I need to get some information about you!\n\n")

        user_name = input("What do you want your username to be? \n")

        icon_choice = input (f"Okay {user_name} and what icon would you like to use?\n a.) 🐯 b.)🐻 c.)🐨 or d.)🦄 \n")


        def icon_generator():
            if icon_choice == 'a': 
                return '🐯'

            if icon_choice  =='b':
                return '🐻' 

            if icon_choice =='c':
                return '🐨'  

            if icon_choice =='d':
                return '🦄'
            
            else: 
                print ("You did not select a valid icon! Your default icon has been set to: 💩\n ")
                return '💩'


        icon = icon_generator()

        instructions =  (F"""
    Hey there {user_name} {icon}! 

    this game is an optimization game.

    You will have {NUMBER_OF_ROUNDS - 1} days to make the most money you can. Each decision you make represents a day.

    You make money by 🌱 \033[92mgrowing\033[00m, \033[92mharvesting\033[00m and 💰\033[92mselling\033[00m bloomed flowers. 

    In order for flowers to bloom, they must be \033[96mwatered\033[00m💦 when needed. Otherwise, they will \033[91m die\033[00m. ❌ ❌

    Flowers that are not harvested within 2 days of blooming will also\033[91m die\033[00m. ❌ ❌

    Flower \033[92mprices\033[00m are based on how long they take to bloom and how much they need to be \033[96mwatered\033[00m💦.

    there are three flowers: 
                        \033[93msunflowers\033[00m 🌻 can be sold for \033[92m 3 \033[00m dollars.
                                \033[91mhibuscuses\033[00m 🌺 can be sold for\033[92m 6 \033[00m dollars.
                                    \033[95mcherry blossoms\033[00m 🌸 can be sold for\033[92m 10 \033[00m dollars.
                                
    Now time to get \033[92mgrowing\033[00m!

""")
        print (instructions)
        counter +=1


    print (f"Today is day {counter} on DC_Crossing.\n")
    
    new_plot.print_bed()
    
    try: 
        next_move = int (input ("""
        What would you like to do today?
        1.) New plant
        2.) Check plant water levels
        3.) Water a plant
        4.) Harvest and sell your plants
        5.) quit game 
        """))
    
    except ValueError:
        print ("""\033[96m 
    
        ****

        You did not pick a number!

        ****
                        \033[00m""")
        continue

    if next_move > 5 or next_move <=0 : 
        print ("""\033[96m 
    
        ****

        Please print a valid number!

        ****
                        \033[00m""")

        continue

    if next_move == 1: 
        set_flower_from_user()
   
    if next_move == 2: 
        get_water_levels()
    
    if next_move == 3: 
      incrementer = water_plants()
      counter -= incrementer

    if next_move == 4: 
        new_plot.harvest_plants()


    new_plot.bloom_calc()
    new_plot.water_calc()
    counter +=1
    
    
    if counter == NUMBER_OF_ROUNDS or next_move== 5:
        print (F"You earned {new_plot.money} 💰dollars this game!\n")
        save_score(Score(user_name, new_plot.money))
        print ("💰💰💰 DC Crossing Leaderboard 💰💰💰\n\n\n")
        
        for i in range(0,3):
            print (F""" Place {i+1}:
                        Name: {get_scores()[i].name}
                        Score: {get_scores()[i].value} coins
                __________________________________
                        """)
        
        play_again = input("Do you want to play again Yes or No?\n").lower()

        if play_again == "yes":
            counter =0
            new_plot.plants["plant_one"] = None
            new_plot.plants["plant_two"] = None
            new_plot.plants["plant_three"] = None
            new_plot.plants["plant_four"] = None
            new_plot.bed = [" ", " "," ", " "]
            new_plot.money = 0
            new_plot.index = None

        
        else: 
            print (F"See you next time {user_name} {icon}! :)\n")
            exit()
    
    
