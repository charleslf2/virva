# Virva

Virva is the simplest synthetic dataframe generator 

check the  [Virva documentation](https://charleslf2.github.io/virva/) here
# Purpose of the package
+  The purpose of this package is to provide to machine learning practitioners the world simplest synthetic dataframe generator


# Features
+ Generate synthetic dataframe of any lenght 
+ Random names generations
+ Random cities generations
+ Random jobs title generations
+ Random Zipcode generations
+ Random contrie generations
+ CSV export
+ Generate custom categorical variables
+ Generate custom numerical variables
+ And much more


# Getting Started
The package can be found on pypi hence you can install it using pip

### Installation

```bash

pip install virva

```
### Usage
```python
# Import Virva generator
>>> from virva.core import Generator

# generate 50 random names
>>> dataframe_one= Generator.generate_names("Names", number=50)

# generate 50 random cities
>>> dataframe_two = Generator.generate_cities("Cities", number=50)

# generate 50 random jobs
>>> dataframe_three = Generator.generate_jobs("Jobs", number=50)

# generate 50 random age's between 5 and  18 year old
>>> dataframe_four =Generator.generate_integers("Ages", number=50, 5, 18)

#generate csv file with above dataframe with the name "my_shynthetic_dataframe"
>>> list_of_dataframe=[dataframe_one, dataframe_two,dataframe_three,
dataframe_four]

>>>Generator.assemble(output_directory_path, list_of_dataframe, "my_shynthetic_dataframe")
```

### Contribution
Contribution are welcome.
Notice a bug ? let us know. Thanks you

### Author
+ Main Maitainer : Charles TCHANAKE
+ email : datadevfernolf@gmail.com 
