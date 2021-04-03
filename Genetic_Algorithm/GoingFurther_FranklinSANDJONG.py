# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:42:12 2021

@author: franklin_sandjong
"""
from abc import ABC, abstractmethod
from numpy.random import default_rng
import math

print("Enter your target which represent the perimiter of te circle of tour towns      NB: Your target has to be an an character")
target = float(input())
print("Enter your number of towns" )
number_of_towns = int(input())
print("Enter the number of roads of the population")
number_population = int(input())



# Returning a list of random numbers 
class AbstractDigit_generator(ABC):   
    @abstractmethod
    def digit_generator():
        pass
 
class ConcreteDigit_generator(AbstractDigit_generator):
    def digit_generator(size):
        rng = default_rng()
        numbers = rng.choice(10, size, replace=False)
        numbers = list(numbers)
        return(numbers)


#Initialising towns and  their position on the circle
class AbstractInitializationtown(ABC):   
    @abstractmethod
    def initializationtown():
        pass
 
class ConcreteInitializationtown(AbstractInitializationtown):
    def initializationtown():
        #entring and creating the target
        teta = 360/number_of_towns
        teta_individual = 0
        all_towns = []
        for numero_personne in range(0,number_of_towns):
            one_individual = []
            aroad = "town"+ str(numero_personne)
            one_individual.append(aroad)
            one_individual.append(teta_individual)
            all_towns.append(one_individual)
            teta_individual = teta_individual + teta
        return(all_towns)
    



# Creating a road    
class AbstractInitializationroad(ABC):   
    @abstractmethod
    def initializationroad():
        pass
 
class ConcreteInitializationroad(AbstractInitializationroad):
    def initializationroad():
        towns = []
        random_road = ConcreteDigit_generator.digit_generator(number_of_towns)
        random_road = list(random_road)
        for numero_personne in range(0,number_of_towns):        
            aroad = "town"+ str(random_road[numero_personne])
            towns.append(aroad)
            
        return(towns)
 
    
 
#Creating a population( it is compose of multiple roads which represent here the individuals)
class AbstractInitializationpop(ABC):   
    @abstractmethod
    def initializationpop():
        pass
 
class ConcreteInitializationpop(AbstractInitializationpop):
    def initializationpop():
        population =[]
        a = ConcreteInitializationroad.initializationroad()
        #create all the roads
        while (len(population) < number_population):
            a = ConcreteInitializationroad.initializationroad()
            #DONT take a road whic repeat
            while(a in population == True ):
                a = ConcreteInitializationroad.initializationroad()
            population.append(a)    
        return(population)
 
    
 
    
 
# Add parameters to the chosen road 
class AbstractParamroad(ABC):   
    @abstractmethod
    def paramroad():
        pass
 
class ConcreteParamroad(AbstractParamroad):
    def paramroad(atown, alist_town_parameter):
        indiv = [atown]
        for number_word in range(len(alist_town_parameter)):
            if atown in alist_town_parameter[number_word]:
                indiv.append(alist_town_parameter[number_word][1])
                return(indiv)
                break
            
 
            
 # Calculate the distance between two towns
class AbstractDistance2town(ABC):   
    @abstractmethod
    def distance2town():
        pass
 
class ConcreteDistance2town(AbstractParamroad):
    def distance2town(onetown, twotown, mytownparamlist):
        teta_1town =ConcreteParamroad.paramroad(onetown,mytownparamlist)[1]
        teta_2town =ConcreteParamroad.paramroad(twotown,mytownparamlist)[1]
        distance = 2 * (target / 2 * math.pi) * math.sin((teta_1town - teta_2town)/2)
        if(distance < 0):
            distance = distance * (-1)
        return(distance)
    
 
    
# Compute te total distance of a road 
class AbstractDistanceroad(ABC):   
    @abstractmethod
    def distanceroad():
        pass
 
class ConcreteDistanceroad(AbstractDistanceroad):
    def distanceroad(road):
        sum = 0 
        for num_town in range(0, len(road)-1):
            asum = ConcreteDistance2town.distance2town(road[num_town],road[num_town + 1],ConcreteInitializationtown.initializationtown())
            sum = sum + asum
        return(sum)
     
        
b = ConcreteInitializationpop.initializationpop()
print(ConcreteDistanceroad.distanceroad(b[1]))

