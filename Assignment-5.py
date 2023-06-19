
#Method 1 to print smallest and largest number
lst=[23,34,18,5,98,76]
print("Smallest number is",min(lst))
print("Largest number is",max(lst))
#Method2 to print smallest and largest number
lst=[50,30,12,80,85,24]
lst.sort()
print(lst)
print("Largest Number is",lst[-1])
print("Smallest Number is",lst[0])
#Method to sort list in ascendind and descnding
value=eval(input("Enter the list"))
print(value)
value.sort()
print("Ascending list is",value)
value.sort(reverse=True)
print("Descending list is",value)
#Converting list into tuples
list=[2.0,4,"Sangram"]
print(list)
mytuple=tuple(list)
print("Tuple is",mytuple)
# Deleting list
lst=['Sangram',5.0,32,'Blue']
del lst
#Sum of elements in my list
lst=[20,34,16,5,9,6]
total=sum(lst)
print("The total is =",total)
# Smallest number is 5    
# Largest number is 98    
# [12, 24, 30, 50, 80, 85]
# Largest Number is 85    
# Smallest Number is 12   
# Enter the list[45,22,67,18,95,33]
# [45, 22, 67, 18, 95, 33]
# Ascending list is [18, 22, 33, 45, 67, 95] 
# Descending list is [95, 67, 45, 33, 22, 18]
# [2.0, 4, 'Sangram']
# Tuple is (2.0, 4, 'Sangram')
# The total is = 90