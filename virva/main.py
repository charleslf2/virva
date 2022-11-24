#version 0.0.2
import random
import pandas as pd
import os
from rich.traceback import install

install()

random.seed(random.randint(0, 1000000000))

class RandomIntegerNumber:
    def __init__(self):
        pass
    def integer(a, b):
        randominteger=random.randint(a,b)
        return randominteger


class Generator:
    
    def __init__(self):
        pass


    def generate_numeric(column_name:str, number:int, gen_start:int, gen_end:int):

        """
        This function generate random  numeric values acording to your params

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
        if number >100:
            raise Warning("Since this package is currently in alpha you can't generate more than 100 samples at a time")
            
        
        list=[]
        for i in range(0, number):
            list.append(RandomIntegerNumber.integer(gen_start,gen_end))
#            age_list.append(RandomIntegerNumber.integer(5, 60))
            d={column_name:list}
            dataframe=pd.DataFrame(data=d)
        #path=r"C:\Users\Charles TCHANAKE\Desktop\dev\synthetic\generated_data"
        #dataframe.to_csv(os.path.join(path, r"first_data.csv"), sep=",")
        return dataframe
        


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
        if number >100:
            raise Warning("Since this package is currently in alpha you can't generate more than 100 samples at a time")
            
        list=[]
        path=r"C:\Users\Charles TCHANAKE\Desktop\virva\data\names.txt"
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
  #          path=r"C:\Users\Charles TCHANAKE\Desktop\dev\synthetic\generated_data"
  #          dataframe.to_csv(os.path.join(path, r"names_data.csv"), sep=",")

    def generate_jobs(column_name:str, number:int):

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

        if number >100:
            raise Warning("Since this package is currently in alpha you can't generate more than 100 samples at a time")
            
        list=[]
        path=r"C:\Users\Charles TCHANAKE\Desktop\virva\data\jobs.txt"
        infile=open(path, "r")
        aline=infile.readline()
        aline_length= len(aline.split(","))
            
        for i in range(0, number):
            n_random=random.randint(0,aline_length-1)
            name=aline.split(",")[n_random]
            list.append(name)
            d={column_name:list}
            dataframe=pd.DataFrame(data=d)
                #return dataframe
   #         path=r"C:\Users\Charles TCHANAKE\Desktop\dev\synthetic\generated_data"
    #        dataframe.to_csv(os.path.join(path, r"jobs_data.csv"), sep=",")
        return dataframe

    def generate_cities(column_name:str, number:int):

        """
        This function generate random cities

        Params:
        ---------

        column_name(String|required)="The name of the column"

        number(Integer|required)= "The number of sample you want to generate"

        Usages:
        --------

        >>> Generator.generate_names(column_name="Cities", number=50) 
        """

        if number >100:
            raise Warning("Since this package is currently in alpha you can't generate more than 100 samples at a time")
            
        list=[]
        path=r"C:\Users\Charles TCHANAKE\Desktop\virva\data\cities.txt"
        infile=open(path, "r")
        aline=infile.readline()
        aline_length= len(aline.split(","))
            
        for i in range(0, number):
            n_random=random.randint(0,aline_length-1)
            name=aline.split(",")[n_random]
            list.append(name)
            d={column_name:list}
            dataframe=pd.DataFrame(data=d)
                #return dataframe
   #         path=r"C:\Users\Charles TCHANAKE\Desktop\dev\synthetic\generated_data"
    #        dataframe.to_csv(os.path.join(path, r"jobs_data.csv"), sep=",")
        return dataframe
    
    def assemble(path, data, name:str):

        """
        This function assemble your generated dataframe in one, compact csv file

        Params:
        ---------

        path(required)=The output directory ; Should be a directory

        data(List|required)=The list of data to concatenate ; Should be a list of data you want to assemble 

        name(String|required)= The name  of the csv file 
        Usages:
        ---------

        Generator.assemble(your_directory_path, [dataframe_1, dataframe_2, dataframe3])
        """

        if type(data)==list:
            pass
        else:
            raise ValueError("The data variables should be a list of multiple dataframe")

        isdir=os.path.isdir(path)
        
        if isdir ==True:
            pass
        else:
            raise ValueError("The path should be a directory")
            
        data=pd.concat(data, axis=1)

        path=path
        data.to_csv(os.path.join(path, name+".csv"), sep=",")
        

    
    

        
