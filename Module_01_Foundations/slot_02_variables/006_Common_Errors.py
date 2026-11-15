#ERROR 1: using a variable before defining it
print(score)        #NameError

#ERROR 2:forgetting quotes
name = SHEETAL    #NameError (Python thinks Sheetal is a variable

#FIX:
name = "SHEETAL"

#ERROR 3 (conceptual trap): number stored as string
age = "22"
print(type(age))   # <class 'str'>  -- NOT int, even though it looks like one!