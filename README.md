# Virva
Virva is the simplest synthetic dataframe generator 

#### Purpose of the package
+  The purpose of this package is to provide to machine learning practitioners the world simplest synthetic dataframe generator


#### Features
+  synthetic dataframe generator 
+  csv export 
+ random names generations
+ random cities generations
+ random jobs title generations



### Getting Started
The package can be found on pypi hence you can install it using pip

#### Installation

```bash

pip install virva

```
### Usage
```python

# Import Virva generator
>>> from virva import Generator

# generate 50 random names
>>> dataframe_one= Generator.generate_names("Names", number=50)

# generate 50 random cities
>>>dataframe_two = Generator.generate_cities("Cities", number=50)

# generate 50 random jobs
>>>dataframe_three = Generator.generate_jobs("Jobs", number=50)

# generate 50 random age's between 5 and  18 year old
>>> dataframe_four =Generator.generate_numeric("Ages", number=50, 5, 18)

#generate csv file with above dataframe with the name "my_shynthetic_dataframe"
>>>list_of_dataframe=[dataframe_one, dataframe_two,dataframe_three,
dataframe_four]

>>>Generator.assemble(output_directory_path, list_of_dataframe, "my_shynthetic_dataframe")


```

### Contribution
Contribution are welcome.
Notice a bug ? let us know. Thanks you

### Author
+ Main Maitainer : Charles TCHANAKE
+ email : datadevfernolf@gmail.com 

### Additionnal Note
Since this package is still in alpha you can only generate 100 samples at a time 