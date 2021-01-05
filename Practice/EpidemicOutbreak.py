#Epidemic Outbreak Program
#By MJK618
import random

#The Epidemic
#Helper Class
class Outbreak():
    """This will be the outbreak controller class,It will be a helper class""" 
    def __init__(self):
        """Initialise Attributes"""

        self.day_num = 1

        #Get inputs from the user about the population size
        self.population = int(input("\nEnter the population size of the community : "))

        #take the input for the initial percent of people of being infected
        self.initial_infection_percent = float(input("\nEnter the percentage of population infected initially : "))
        self.initial_infection_percent /= 100

        #Know the risk of spread from the user
        self.spread_prob = float(input("\nEnter the risk on scale of [1-100] of a person to spread and contract the infection : "))
        
        #take input for the duration of the infection to be exposed to the community        
        self.infection_exposure_days = int(input("\nHow many days this infection will be exposed to the Community? => "))

        #Mortality Rate
        self.mort_rate = float(input("\nWhat is the mortality rate of the infected community? => "))

        #Duration of the outbreak to run
        self.duration = int(input("For how many days you want to run this Simulation? => "))
        
#Living being we would test on
class LivingBeing():
    """this will define the individual attributes of a being from the community"""

    def __init__(self):
        """Initialise the attributes"""
        self.infected = False #All Beings are healthy initially
        self.alive = True #Is dead or alive
        self.days_infected = 0 #It will track the number of days of the being infected    
        
    def getInfected(self, outbreak):
        """This will infect beings based on the outbreak attributes"""
        #being will get infected if random integer gets less than the spread probablity
        if random.randint(1,100) < outbreak.spread_prob:
            self.infected = True

    def getCured(self):
        """This method will cure the infected beings"""
        self.infected = False
        self.days_infected = 0
        
    def die(self):
        """This will kill the infected people by considering the number of days they are already infected from"""
        self.alive = False

    def showStatus(self, outbreak):
        """this will keep track of days infected,dead or alive, infected or healed and will update accordingly"""
        if self.alive:
            if self.infected:
                self.days_infected += 1
                #randomising death
                if random.randint(0,100) < outbreak.mort_rate:
                    self.die()
                #Curing those infected beings whose days of infected = days of simulation 
                elif self.days_infected == outbreak.duration:
                    self.getCured()

#Population
class Community():
    """This will create a whole community/population the the being class objects"""

    def __init__(self, outbreak):
        """initialising atributes of the community"""
        self.population_list = [] #Will store each object of LivingBeing

        #Creating instances of beings and appending them into the population list
        for i in range(outbreak.population):
            being = LivingBeing()
            self.population_list.append(being) 

    def infection_start(self, outbreak):
        """This will infect acertain popukation inititialy"""
        #Will take the initial infection count by multipying the initial spread percentage with toatl population
        #Needs to be an integer beacuse it will be used in a for loop
        initially_infected_num = int(round(outbreak.initial_infection_percent * outbreak.population, 0))

        #infecting the initial population
        for i in range(initially_infected_num):
            self.population_list[i].infected = True
            self.population_list[i].days_infected = 1

        #Suffling the population list to spread the infection randomly
        random.shuffle(self.population_list)   
        
    def spread(self, outbreak):
        """This will spread the infection to the adjacent being of the population"""

        for i in range(len(self.population_list)):

            # i th being is alive as dead person wont infect 
            if self.population_list[i].alive:

                #if i is the first being then it will only check to its right
                if i == 0:
                    if self.population_list[i+1].infected:
                        self.population_list[i].getInfected(outbreak)                       

                #If the being is from the middle of the list then it can infect both the being adjacent to him
                elif i < len(self.population_list) - 1:
                    if self.population_list[i-1].infected or self.population_list[i+1]:
                        self.population_list[i].getInfected(outbreak)
                        

                #if the  being is on the extreme right of the list then he can only infect the adjacent left one
                elif i == len(self.population_list) - 1:
                    if self.population_list[i-1].infected:
                        self.population_list[i].getInfected(outbreak)
                        
    def update(self, outbreak):
        """This will update the each population being"""
        outbreak.day_num += 1

        #Updating all beings status    
        for being in self.population_list:
            being.showStatus(outbreak)

    def showStats(self, outbreak):
        """This will display the summary of the outbreak"""

        total_infected_num = 0
        total_dead_num = 0
        
        #Going through the population list
        for being in self.population_list:

            #Infected Beings Increment
            if being.infected:
                total_infected_num += 1

                #Dead beings Increment
                if being.alive == False:
                    total_dead_num += 1

        #Find out the % of dead and infected
        dead_percent = round(100*(total_dead_num/outbreak.population),4)            
        infected_percent = round(100*(total_infected_num/outbreak.population),4)

        #Summarise the data to be displayed
        print("\n\t\t\tDAY : " +str(outbreak.day_num))
        print("\tPercentage of Population Infected => " + str(infected_percent) + "%.")
        print("\tPercentage of Population Died => " + str(dead_percent) +"%.")
        print("\tTotal Infected Beings => " + str(total_infected_num)+"/" + str(outbreak.population) +".")
        print("\tTotal Deaths => " + str(total_dead_num)+"/" + str(outbreak.population) +".")

    def showGraphics(self):
        """This will represnt the beings of the population as infected, healthy or dead by I,H,D respectively"""

        pop_list = []#List to hold the beings of population to represent the outbreak
        for being in self.population_list:

            #If being has died
            if being.alive == False:
                char = 'D'
            else:

                #If person is just infected
                if being.infected:
                    char = "I"
                else:
                    char = "H"
            pop_list.append(char)

        #the display of beings as characters
        for char in pop_list:
            print(char,end="-")


#The Main Code
#Create Outbreak and Community object
corona = Outbreak()
human_being = Community(corona)

#Setting up the initial infection conditions
human_being.infection_start(corona)
human_being.showStats(corona)
human_being.showGraphics()
input("\nPress Enter to initiate the outbreak : ")


#Conduct Outbreak
for i in range(1,corona.duration):
    human_being.spread(corona)
    human_being.update(corona)
    human_being.showStats(corona)
    human_being.showGraphics()

    if i != corona.duration - 1:
        input("\nPress Enter to see the status for next day. ")


























