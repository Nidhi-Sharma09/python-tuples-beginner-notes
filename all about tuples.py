#tuples are similar to lists but they are immutable, 
# meaning that once a tuple is created, its elements cannot be modified. 
# Tuples are defined using parentheses () instead of square brackets [].
#Creating a tuple
my_tuple = (1,2,3,4,5)
print(type(my_tuple)) # Output: <class 'tuple'>

mixed_tuple = (1, "Hello", 3.14, [1, 2, 3])
print(type(mixed_tuple)) # Output: <class 'tuple'>


#Accessing elements in a tuple
print(my_tuple[0]) # Output: 1
print(mixed_tuple[1]) # Output: Hello


#tuple slicing
print(my_tuple[1:4]) # Output: (2, 3, 4)


#concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple) # Output: (1, 2, 3, 4, 5, 6)

print(my_tuple + mixed_tuple) # Output: (1, 2, 3, 4, 5, 1, 'Hello', 3.14, [1, 2, 3])


#repeating tuples
repeated_tuple = tuple1 * 3
print(repeated_tuple) # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)


#countering elements in a tuple
print(my_tuple.count(2)) # Output: 1 in this tuple id not repeated and present only for once thus count is 1


#finding the index of an element in a tuple
print(my_tuple.index(3)) # Output: 2 caus ethe value 3 is present at index 2 in the tuple


#packing and unpacking tuples
#packing
packed_tuple = 1, "Hello", 3.14
print(packed_tuple) # Output: (1, 'Hello', 3.14)
#unpacking
a, b, c = packed_tuple
print(a) # Output: 1
print(b) # Output: Hello
print(c) # Output: 3.14
#unpacking with asterisk *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first) # Output: 1
print(middle) # Output: [2, 3, 4]
print(last) # Output: 5


#nested tuples
nested_tuple = ((1, 2, 3, 4), ('a', 'b', 'c'),(True, False))
#accessing elements in a nested tuple
print(nested_tuple[0]) # Output: (1, 2, 3, 4)
print(nested_tuple[1][1]) # Output: b from the second tuple we are accessing the element at index 1 which is 'b'
print(nested_tuple[2][0]) # Output: True from the third tuple we are accessing the element at index 0 which is True