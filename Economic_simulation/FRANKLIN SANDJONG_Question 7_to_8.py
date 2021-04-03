# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:21:50 2021

@author: franklin_sandjong
"""
#TP1 PROFESSIONNAL PROGRAMMING -- ECONOMIC SIMULATION

#1-- Declare a population of 1000 individuals
import random
#Librairie permettant d'importer les nombres aléatoires

from abc import ABC, abstractmethod
#Use the abstract method

class AbstractInitialization(ABC):   
    @abstractmethod
    def initialization():
        pass
 
class ConcreteInitialization(AbstractInitialization):
    def initialization():
        print("Enter number_of_individuals")
        # to inter the number of people in the population
        number_of_population = int(input())
        #Create the list of population
        list_population = []
        #Entring the same wealth for each person in the population
        
        for numero_personne in range(0,number_of_population):
            #create a list representing a person with his wealth
            wealth_personne = random.randint(0, 1000)
            #Add everybody to the list of population
            one_person = []
            personne = "personne"+ str(numero_personne)
            one_person.append(personne)
            one_person.append(wealth_personne)
            list_population.append(one_person)
        #Ascending Sort of the list of population by their wealth 
        list_population = sorted(list_population, key=lambda list_population: list_population[1])
        return(list_population)

    
    
class AbstractInteraction(ABC):
    @abstractmethod
    def interaction():
        pass

class ConcreteInteraction(AbstractInteraction):   
    def interaction(list_individual):
#random.randrange(0, 100000, 100) if i want to choose randomly the wealth
#pick two individual randomly among the population       
        list_two_individual =[]
        list_of_wealth = []
        for num_wealth in range(0,len(list_individual)):
            list_of_wealth.append(list_individual[num_wealth][0])
        first_individual = random.choice(list_of_wealth)
        second_individual = random.choice(list_of_wealth)
        list_two_individual.append(first_individual)
        list_two_individual.append(second_individual)
        return(list_two_individual)
    

    
class Abstracttransaction(ABC):
    @abstractmethod
    def transaction():
        pass
        
class Concretetransaction(Abstracttransaction):
    def transaction(list_2_individual,list_population):
        #take the wealth of the two individual randomly choosen
        for num_wealth in range(0,len(list_population)):
            for num in range(2):
                if list_population[num_wealth][num] == list_2_individual[0]:
                    first_index = num_wealth
                if list_population[num_wealth][num] == list_2_individual[1]:
                    second_index = num_wealth
        #transaction between the two
        #sum of their two wealth
        summ_of_two = list_population[first_index][1] + list_population[second_index][1]
         #choose a random number between 0 and the sum of the two wealth
        value_random = random.randint(0, summ_of_two)
        #Give the random to the first and the rest to the second
        list_population[first_index][1] = value_random
        list_population[second_index][1] = summ_of_two - value_random
        #Ascending Sort of the list of population by their wealth
        list_population = sorted(list_population, key=lambda list_population: list_population[1])
        return(list_population)
    
#GLOBAL
#Creating our list of population
my_list_wealth_pop = ConcreteInitialization.initialization()

print("enter the number of interraction")
#Enter the number of interractions
number_interaction = int(input())
for numero_iteration in range(0,number_interaction):
    my_two_indivisual = ConcreteInteraction.interaction(my_list_wealth_pop)
    Concretetransaction.transaction(my_two_indivisual,my_list_wealth_pop)
    #Ascendant sorting of the population list by wealth
    my_list_wealth_pop = sorted(my_list_wealth_pop, key=lambda my_list_wealth_pop: my_list_wealth_pop[1])
  
    
#COMPUTING the gini parameter

#PARAMETER  numerator part1 gini parameter
parameter1 = 0
for numero_personne in range(0,len(my_list_wealth_pop)):
    parameter1 = parameter1 + ((numero_personne+1)*my_list_wealth_pop[numero_personne][1])
parameter1 = 2 * parameter1
    
#PARAMETER  denominator part1 gini parameter
parameter2 = 0
for numero_personne in range(0,len(my_list_wealth_pop)):
    parameter2 = parameter2 + my_list_wealth_pop[numero_personne][1]
parameter2 = len(my_list_wealth_pop) * parameter2 

#PARAMETER  part2 gini parameter
parameter3 = (len(my_list_wealth_pop) + 1)/len(my_list_wealth_pop)

#Value Gini Parameter
Gini = (parameter1/parameter2) - parameter3
print("The number of Gini is ", Gini) 
