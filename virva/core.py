#version Alpha : 0.0.8

import random
import pandas as pd
import os
from rich.traceback import install

install()

random.seed(random.randint(0, 1000000000))

class RandomNumber:
    def __init__(self):
        pass
    def integer(a, b):
        randominteger=random.randint(a,b)
        return randominteger
    def floats(a,b):
        randomfloat=random.uniform(a,b)
        return randomfloat


def Constructor(path, column_name, number):
    list=[]
    path=path
    infile=open(path, "r")
    aline=infile.readline()
    aline_length= len(aline.split(","))

    for i in range(0, number):
        n_random=random.randint(0,aline_length-1)
        name=aline.split(",")[n_random]
        list.append(name)
        d={column_name:list}
        dataframe=pd.DataFrame(data=d)

    return dataframe


class Generator:
    
    def __init__(self):
        pass

#===============================================================
    def generate_integers(column_name:str, number:int, gen_start:int, gen_end:int):

        """
        This function generate random  integer values acording to your params

        Params:
        ---------

        column_name(String|required)="The name of the column"

        number(Integer|required)= "The number of sample you want to generate"

        gen_start(Integer|required)="The starting number of generation"

        gen_end(Integer|required)="The end number of generation"

        Usages:
        ---------

        >>> Generator.generate_numeric(column_name="Monthly_salary", number=50, gen_start=1000, gen_end=10000) 
        """
            
        
        list=[]
        for i in range(0, number):
            list.append(RandomNumber.integer(gen_start,gen_end))
            d={column_name:list}
            dataframe=pd.DataFrame(data=d)

        return dataframe
        
#==============================================================
    def generate_floats(column_name:str, number:int, gen_start:float, gen_end:float):

        """
        This function generate random  float  values acording to your params

        Params:
        ---------

        column_name(String|required)="The name of the column"

        number(Integer|required)= "The number of sample you want to generate"

        gen_start(Float|required)="The starting number of generation"

        gen_end(Float|required)="The end number of generation"

        Usages:
        ---------

        >>> Generator.generate_floats(column_name="Tax", number=50, gen_start=10.56, gen_end=20.56) 
        """


        list=[]
        for i in range(0, number):
            list.append(RandomNumber.floats(gen_start,gen_end))
            d={column_name:list}
            dataframe=pd.DataFrame(data=d)

        return dataframe

#======================================================

    def generate_objects(column_name:str, number:int, list_of_object):

        """
        This function generate random variables (with dtype == objects) according to your params

        Params:
        ---------
        column_name(String|required)="The name of the column"

        number(Integer|required)= "The number of sample you want to generate"

        list_of_object(List|required)= "Represent the database for the generator"

        Usages:
        --------

        >>> Generator.generate_objects(column_name="Gender", number=50, list_of_object=["M", "F"] )

        """
        list=[]
        list_of_object=list_of_object
        list_lenght=len(list_of_object)

        for i in range(0, number):
            n_random=random.randint(0,list_lenght-1)
            name=list_of_object[n_random]
            list.append(name)
            d={column_name:list}
            dataframe=pd.DataFrame(data=d)

        return dataframe


#===================================================
    def generate_names(column_name:str, number:int):

        """
        This function generate random names 

        Params:
        ---------

        column_name(String|required)="The name of the column"

        number(Integer|required)= "The number of sample you want to generate"

        Usages:
        ---------

        >>> Generator.generate_names(column_name="Names", number=50) 
        """

        url=r"data\names.txt"

        return Constructor(url, column_name, number)
        
#==========================================================
    def generate_jobs(column_name:str, number:int):

        """
        This function generate random jobs

        Params:
        ---------

        column_name(String|required)="The name of the column"

        number(Integer|required)= "The number of sample you want to generate"

        Usages:
        ---------

        >>> Generator.generate_jobs(column_name="Names", number=50) 
        """
        path=r"data\jobs.txt"

        return Constructor(path, column_name, number)

#==============================================================


    def generate_cities(column_name:str, number:int):

        """
        This function generate random cities

        Params:
        ---------

        column_name(String|required)="The name of the column"

        number(Integer|required)= "The number of sample you want to generate"

        Usages:
        --------

        >>> Generator.generate_cities(column_name="Cities", number=50) 
        """


        path=r"data\cities.txt"
        return Constructor(path, column_name, number)

#===========================================================

    def generate_zipcodes(column_name:str, number:int):

        """
        This function generate random zipcode

        Params:
        ---------

        column_name(String|required)="The name of the column"

        number(Integer|required)= "The number of sample you want to generate"

        Usages:
        --------

        >>> Generator.generate_zipcodes(column_name="Zipcodes", number=50) 
        """

        path=r"data\zipcodes.txt"

        return Constructor(path, column_name, number)
    

#=============================================================

    def generate_diseases(column_name:str, number:int):

        """
        This function generate random diseases

        Params:
        ---------

        column_name(String|required)="The name of the column"

        number(Integer|required)= "The number of sample you want to generate"

        Usages:
        --------

        >>> Generator.generate_diseases(column_name="Diseases", number=50) 
        """


        path=r"data\diseases.txt"

        return Constructor(path, column_name, number)
    
#=============================================================

    def generate_foods(column_name:str, number:int):

        """
        This function generate random foods

        Params:
        ---------

        column_name(String|required)="The name of the column"

        number(Integer|required)= "The number of sample you want to generate"

        Usages:
        --------

        >>> Generator.generate_foods(column_name="Diseases", number=50) 
        """


        path=r"data\foods.txt"

        return Constructor(path, column_name, number)

#=============================================================

    def generate_us_states(column_name:str, number:int):

        """
        This function generate random US states

        Params:
        ---------

        column_name(String|required)="The name of the column"

        number(Integer|required)= "The number of sample you want to generate"

        Usages:
        --------

        >>> Generator.generate_us_states(column_name="US states", number=50) 
        """


        path=r"data\us_states.txt"

        return Constructor(path, column_name, number)

#=============================================================

    def generate_countries(column_name:str, number:int):

        """
        This function generate random countries

        Params:
        ---------

        column_name(String|required)="The name of the column"

        number(Integer|required)= "The number of sample you want to generate"

        Usages:
        --------

        >>> Generator.generate_countries(column_name="Countries", number=50) 
        """


        path=r"data\countries.txt"

        return Constructor(path, column_name, number)

#=============================================================
    def assemble(path, list_of_data, name:str):

        """
        This function assemble your generated dataframe in one, compact csv file

        Params:
        ---------

        path(required)=The output directory ; Should be a directory

        list_of_data(List|required)=The list of data to concatenate ; Should be a list of data you want to assemble 

        name(String|required)= The name  of the csv file 

        Usages:
        --------

        >>> Generator.assemble(your_directory_path, [dataframe_1, dataframe_2, dataframe3] , "my_synthetic_dataset")
        """

        if type(list_of_data)==list:
            pass
        else:
            raise ValueError("list_of_data should be a list of dataframes")

        isdir=os.path.isdir(path)
        
        if isdir ==True:
            pass
        else:
            raise ValueError("The path should be a directory")
            
        data=pd.concat(list_of_data, axis=1)

        path=path
        data.to_csv(os.path.join(path, name+".csv"), sep=",")


