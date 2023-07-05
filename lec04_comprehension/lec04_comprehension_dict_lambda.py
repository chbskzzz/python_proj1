feh = {'temp1':10, 'temp2':20, 'temp3':30, 'temp4':40}

# 1
cel = list(map(lambda x: (float(5)/9)*(x-32), feh.values()))
cel_dict = dict(zip(feh.keys(), cel))
print(cel_dict)
# 2
cel_dict = {k:(float(5)/9)*(v-32) for (k,v) in feh.items()}
print(cel_dict)

# 3
dict = {'a':1, 'b':2, 'c':3, 'd':4}

new_dict = {k:v for (k,v) in dict.items() if v>3}
new_dict1 = {k:('even No' if v%2==0 else 'oddNo') for (k,v) in dict.items()}
print(new_dict)
print(new_dict1)
# 4
dict = {'a':1,'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
new_dict2 = {k:v for (k,v) in dict.items() if v>3 if v%2==0}
print(new_dict2)