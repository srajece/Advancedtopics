def my_function(): 
    """Demonstrate docstrings and does nothing really."""
   
    return None
  
print ("Using __doc__:")
print (my_function.__doc__ )
  
print ("Using help:")
help(my_function)

#One-line Docstrings
'''
def power(a, b): 
    """Returns arg1 raised to power arg2."""
   
    return a**b 
  
print power.__doc__ 
'''
#Multi-line Docstrings
def my_function(arg1): 
    """
    1.The doc string line should begin with a capital letter and end with a period.
    2.The first line should be a short description.
    3.If there are more lines in the documentation string,
    the second line should be blank, visually separating the summary from the rest of the description.
    4.The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc.

    eg:
    Summary line. 
  
    Extended description of function. 
  
    Parameters: 
    arg1 (int): Description of arg1 
  
    Returns: 
    int: Description of return value 
  
    """
  
    return arg1 
  
print (my_function.__doc__ )
