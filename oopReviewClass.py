# your class goes here

from ast import Num


class Pet:
    def __init__(self, type, weight, limbs, age, name):
        self.__type = type
        self.__weight = weight
        self.__limbs = limbs
        self.__age = age
        self.__name = name

    def get_type(self):
        return self.__type

    def get_weight(self):
        return self.__weight

    def get_limbs(self):
        return self.__limbs

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def move(self, num):
        self.__distance = int(self.__limbs) * num 
        
    def get_move(self):
        return self.__distance


