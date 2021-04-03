# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:43:44 2021

@author: franklin_sandjong
"""
import random
import string

from abc import ABC, abstractmethod

#Enter our target 
print("Enter your target       NB: Your target has to be an an character")
target = input()



# Generate a string with a precise size
class AbstractString_generator(ABC):   
    @abstractmethod
    def string_generatorbel():
        pass
 
class ConcreteString_generator(AbstractString_generator):
    def string_generator(size):
        #define uppercase and lowercase string with white spaces
        chars = string.ascii_uppercase + string.ascii_lowercase + string.whitespace
        return ''.join(random.choice(chars) for _ in range(size))




#To verify if a list belong to a list of list    
class AbstractBelong(ABC):   
    @abstractmethod
    def belong():
        pass
 
class ConcreteBelong(AbstractBelong):
    def belong(word, alist):
        index_belong = []
        for number_word in range(len(alist)):
            index_belong = []
            index_belong.append(number_word)
            if word in alist[number_word]:
                index_belong.append(True)
                return(index_belong)
                break
        index_belong.append(False)
        return(index_belong)


#Creating our population    
class AbstractInitialization(ABC):   
    @abstractmethod
    def initialization():
        pass
 
class ConcreteInitialization(AbstractInitialization):
    def initialization(target):
        #entring and creating the target
        print("Enter your number population" )
        number_of_population = int(input())
        population = []
        for numero_personne in range(0,number_of_population):
            one_individual = []
            personne = "personne"+ str(numero_personne)
            one_individual.append(personne)
            DNA = ConcreteString_generator.string_generator(len(target))
            one_individual.append(DNA)
            population.append(one_individual)
        return(population)




 #Adding the fitness  to each individual  
class AbstractComparaison(ABC):   
    @abstractmethod
    def initialization():
        pass
 
class ConcreteComparaison(AbstractComparaison):
    def comparaison(first_population):
        
        for numero_personne in range(0,len(first_population)):
            fitness_number = 0
            for letter in range(0, len(target)):
                if target[letter] == first_population[numero_personne][1][letter]:
                    fitness_number = fitness_number + 1
            fitness =  fitness_number/len(target)
            first_population[numero_personne].append(fitness)
        return(first_population)




#Retrieving the most powerful individuals
class AbstractRecuperation(ABC):   
    @abstractmethod
    def initialization():
        pass
 
class ConcreteRecuperation(AbstractRecuperation):
    def Recuperation(a_population):
        list_population = sorted(a_population, reverse = True, key=lambda a_population: a_population[2])
        best_population = []
        for number_of_best in range(0, int(0.1 * len(a_population))):
            best_population.append(list_population[number_of_best])
        return(best_population)
    
 
    
 
    
# Crossover between the most powerful population
class AbstractCrossover(ABC):   
    @abstractmethod
    def initialization():
        pass
 
class ConcreteCrossover(AbstractCrossover):
    def crossover(thebest_population):
        index_first_parent = random.randint(0, len(thebest_population)-1)
        index_second_parent = random.randint(0, len(thebest_population)-1)
        crossover_parameter = random.randint(0, len(target)-1)
        child = ""
        for number_letter in range(0, crossover_parameter):
            child = child + thebest_population[index_first_parent][1][number_letter]
        for number_letter in range(crossover_parameter, len(target)):
            child = child + thebest_population[index_second_parent][1][number_letter]
        return(child) 
 
    
 
    
 
    
#Generate a new population
class AbstractGenerate(ABC):   
    @abstractmethod
    def initialization():
        pass
 
class ConcreteGenerate(AbstractGenerate):
    def generate(my_population, crossover):
        new_generation = []
        for number_crossover in range(0, crossover):
            one_individual = []
            personne = "personne"+ str(number_crossover)
            one_individual.append(personne)
            one_individual.append(ConcreteCrossover.crossover(my_population))
            new_generation.append(one_individual)
        return(new_generation)




#Mutate the population
class AbstractMutation(ABC):   
    @abstractmethod
    def initialization():
        pass
 
class ConcreteMutation(AbstractMutation):
    def mutation(new_population,rate):
        random_rate_individual = random.randint(0, 100)
        for number_crossover in range(0, len(new_population)):
            if(random_rate_individual < rate):
                random_index = random.randint(0, len(target)-1)
                random_letter = ConcreteString_generator.string_generator(len(target))
                list_mot = list(new_population[number_crossover][1])
                list_mot[random_index] = random_letter
                mot = ""
                for num_mot in range(0, len(list_mot)):
                    mot = mot + list_mot[num_mot]                   
                new_population[number_crossover][1] = mot               
        return(new_population)
    
    
    
    
class AbstractBelonging(ABC):   
    @abstractmethod
    def belonging():
        pass

class ConcreteBelonging(AbstractBelonging):
    def belonging():  
        a = ConcreteInitialization.initialization(target)
        b = ConcreteComparaison.comparaison(a)
        print("Entrer the rate ")
        rate1 = int(input())
        print("Entrer the number of crossover you want")
        crossover1 = int(input())
        c = ConcreteRecuperation.Recuperation(b)
        A = 0
        #print(ConcreteBelong.belong(target, c)[1])
        while ConcreteBelong.belong(target, c)[1] == False:
            d = ConcreteGenerate.generate(c,crossover1)
            e = ConcreteMutation.mutation(d,rate1)
            A = A+1
            f = ConcreteComparaison.comparaison(e)
            c = ConcreteRecuperation.Recuperation(f)
            #print(A)
        print("le numéro de la génération est        ", A)
        print("la personne la plus éfficace à les carractéristiques suivantes ",c[ConcreteBelong.belong(target, c)[0]])
        print(c)

ConcreteBelonging.belonging()      
       

