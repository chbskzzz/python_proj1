# SYNTAX : [expression(variable) for variable in input_set[predicate][,...]]
x = set(i*2 for i in range(4) if i%2==0)
print(x)

y = set(i for i in [1,2,3,4] if i%2==0)
print(y)

z = set((a,b) for b in range(3) for a in range(4))
print(z)