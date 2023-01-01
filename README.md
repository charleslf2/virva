# Virva

Virva is the simplest fake dataframe generator 

# Purpose of the package
+  The purpose of this package is to provide the world simplest fake dataframe generator


# Features
+ Generate fake dataframe of any lenght 
+ Random names generations
+ Random cities generations
+ Random jobs title generations
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
>>> names= Generator.generate_names("Names", number=50)

# generate 50 random age's between 5 and  18 year old
>>> ages =Generator.generate_integers("Ages", number=50, 5, 18)

# generate 50 random  scores between 1.0 and 5.0
>>> scores=Generator.generate_floats("stars", number=50, 1.0, 5.1)

# generate 50 random gender type between Male (M) and Female (F)
>>> gender=Generator.generate_objects("Gender", number=50,  ["M", "F"])

# generate 50 random jobs
>>> jobs= Generator.generate_jobs("Jobs", number=50)

# generate 50 random cities
>>> cities= Generator.generate_cities("Cities", number=50)

# generate 50 random diseases
>>> diseases=Generator.generate_diseases("diseases", number=50)

# generate 50 random foods
>>> foods=Generator.generate_foods("foods", number=50)

# generate 50 random us_states
>>> us_states=Generator.generate_us_states("us_states", number=50)

# generate 50 random contries
>>> countries=Generator.generate_countries("Countries", number=50)


#generate csv file with above dataframe with the name "my_shynthetic_dataframe"
>>> list_of_dataframe=[names, ages, scores, gender, jobs, cities, diseases, foods, us_states, countries]

>>>Generator.assemble("path/to/your/directory", list_of_dataframe, "my_shynthetic_dataframe")
```

### Contribution
Contribution are welcome.
Notice a bug ? let us know. Thanks you

### Author
+ Main Maitainer : Charles TCHANAKE
+ email : datadevfernolf@gmail.com 
