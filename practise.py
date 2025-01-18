# # This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the 
# order using loop.
# fruits = ['banana', 'orange', 'mango', 'lemon']

fruitList = ['banana','orange','mango','lemon']
newList=[]
for i in range(1,len(fruitList)+1):
 newList.append(fruitList[-i])
 print(newList)