# amai
Auto map (recursively) and insert json/dict to a sql table. **There is no conventional way of doing it** so this is just one solution. You could use *pandas* to convert a json to a dataframe but first you need to normalize and it is no recursive, you have to be very specific: [see](https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd). This was made by a lazy programmer but not so lazy as others... know that [Oracle supports json objects](https://docs.oracle.com/en/database/oracle/oracle-database/19/adjsn/index.html)!


# Instructions
1. Import the class, then pass the dict and a root path (remember to use the same root for the same table):

```python
from amai import amai

MY_DICT = {'name':'gabriel', 'pets': [{'name':'bit','type':'cat'},{'type':'tamagochi','brand':'tanagotchi'}]}
MY_ROOT = "X"
m = amai(MY_DICT, MY_ROOT)
```
2. Use `insert` method to insert results in an existing table (you need to pass a db connection object)

```python
MY_TABLE = 'domestic'
m.insert(MY_TABLE,DB_CONNECTION)
```

3. Done! In this example you should have two insertions, one for each pet (since it is a list). Common fields are duplicated and each field maps to a column, if the column doesn't exist it is created.

X_NAME | X_PETS_NAME | X_PETS_TYPE | X_PETS_BRAND
---|---|---|---
gabriel | bit | cat | Null
gabriel | Null | tamagochi | tanagotchi

# What do you get?
* `self.fields` : a set of normalized keys
* `self.rows` : a list of normalized dicts, one for each insertion needed

# How does it work?
A recursive normalization of the dict that saves list index information. Check the code for details.
