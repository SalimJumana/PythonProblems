# Databricks notebook source
# DBTITLE 1,a) Simple FOR LOOP
# a) Simple FOR LOOP

user_input = "The lion is the king of the jungle"
counter_dict = dict()

for char in user_input:
    if char in counter_dict.keys():
        counter_dict[char] += 1
    else:
        counter_dict[char] = 1

print(counter_dict)

# COMMAND ----------

# DBTITLE 1,b) Using count() method and set
# b) Using count() method and set

user_input = "The lion is the king of the jungle"    # input("Provide a string ==> ")
counter_dict = dict()

char_set = set(user_input)

for char in char_set:
    counter_dict[char] = user_input.count(char)
print(counter_dict)

# COMMAND ----------

# DBTITLE 1,c) Using collections library
# c) Using collections library

from collections import Counter

user_input = "The lion is the king of the jungle"    # input("Provide a string ==> ")

counter_dict = Counter(user_input)
print(counter_dict)

# COMMAND ----------

# DBTITLE 1,d) Using dict.get() method
# d) Using dict.get() method

# .get() method -> syntax : dictionary_name.get(key, default=None, /); 
# it's a builtin method and Return the value for key if key is in the dictionary, else default.

user_input = "The lion is the king of the jungle"             # input("Provide a string ==> ")
counter_dict = dict()

for char in user_input:
    counter_dict[char] = counter_dict.get(char, 0) + 1
print(counter_dict)
