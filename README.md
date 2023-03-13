# amai
Auto map and insert json/dict to a sql table. Oracle supports json objects but you can have backend personnel not supporting programming... Aparently, there's no conventional way for doing this convertion so I made my own script. Feel free to suggest and adjust according to your requirements.

# Instructions
1. Import the class, then pass the dict and a root path (remember to use the same root for the same table):

```python
from amai import amai

MY_DICT = {'name':'gabriel', 'pets': [{'name':'bit','type':'cat'},{'name':None,'type':'tamagochi'}]}
MY_ROOT = "X"
m = amai(MY_DICT, MY_ROOT)
```
2. Use `insert` method to insert results in an existing table (you need to pass a db connection object)

```python
MY_TABLE = 'domestic'
m.insert(MY_TABLE,DB_CONNECTION)
```

3. Done! In this example you should have two insertions, one for each pet (since it is a list). Common fields are duplicated and each field maps to a column, if the column doesn't exist it is created.

X_NAME | X_PETS_NAME | X_PETS_TYPE
---|---|---
gabriel | bit | cat
gabriel | Null | computer

# What do you get?
* `self.fields` : a set of normalized keys
* `self.rows` : a list of normalized dicts, one for each insertion needed

# How does it work?
A recursive normalization of the dict that saves list index information. Check the code for details.
