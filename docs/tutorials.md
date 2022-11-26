Welcome  to Virva tutorial page .

## Installation

To install Virva , copy paste this line in your terninal

```
pip install virva
```

## Basic Usage

#### Import the virva genrator 

```python
>>> from virva.core import Generator
```
#### Generate a dataframe of  50 names

```python
>>> names_dataframe=Generator.generate_names("Names", 50)

print(names_dataframe)
```

#### Generate a dataframe of 50 cities

```python
>>> cities_dataframe=Generator.generate_cities("Cities", 50)

print(cities_dataframe)
```

## Advanced Usage

#### Generate a csv dataset with the two dataframe with generate in "Basic Usage" section

* First put the two dataframe in a list

```
data=[names_dataframe, cities_dataframe ]
```

* second use the assemble method of virva to create the csv dataset

```
>>> Generator.assemble(r"your_directory_path",  data, name="my_synthetic_dataset")
```

- The first argument is the path of your output directory
- The second one  is a list of dataframe i want to assemble in one dataset
- The third one is the name you want to give to your csv files