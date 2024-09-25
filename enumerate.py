# In Python, enumerate() is a built-in function that allows you to loop over a sequence (like a list or tuple) and get both the index and the value of each item. It's especially useful when you need both the element and its position in a loop...

x=("lemon","ginger","masala")
storeInY=enumerate(x)
print(storeInY)
print(dict(storeInY)) # gives in dictionery like key:pair output:{0: 'lemon', 1: 'ginger', 2: 'masala'}
print(list(storeInY)) #it gives in list and inside tuple output:[(0, 'lemon'), (1, 'ginger'), (2, 'masala')]
print(tuple(storeInY)) # it gives tuple inside tuple output:((0, 'lemon'), (1, 'ginger'), (2, 'masala'))
# below the first find it overrides which gives empty list or tuple or dict

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)
# ---------------------------------------------------------------------------------
print("nothing")
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
