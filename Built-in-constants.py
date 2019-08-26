# In conjunction with the built-in datatypes there are a small number of built-in constants in the built-in namespace:
#     True : The true value of the built-in type bool
#     False : The false value of the built-in type bool
#     None : A singleton object used to signal that a value is absent.
#     Ellipsis or ... : used in core Python3+ anywhere and limited usage in Python2.7+ as part of array notation.
#         numpy and related packages use this as a 'include everything' reference in arrays.
#     NotImplemented : a singleton used to indicate to Python that a special method doesn't support the specific
#         arguments, and Python will try alternatives if available.


a = None # No value will be assigned. Any valid datatype can be assigned later

# In python, we can check the datatype of an object using the built-in function type .

a = '123'
print(type(a))

# In conditional statements it is possible to test the datatype with isinstance . However, it is usually not encouraged
# to rely on the type of the variable.

i = '7' 

if isinstance(i, int): 
    print('Inside If')
    i +=1
elif isinstance(i, str):
    i = int(i)
    print('Inside Else If')
    i += 1 

print(i)

# Examples of immutable Data Types:
#     int , long , float , complex
#     str
#     bytes
#     tuple
#     frozenset

# Examples of mutable Data Types:

    # bytearray
    # list
    # set
    # dict

