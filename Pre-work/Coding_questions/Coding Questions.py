

# Question 1

def hello_name(user_name):
    """a function to print hello_USERNAME"""
    print("hello, "+ user_name.title()+"!")
"""Let's call "hello_name" function"""
hello_name("john")



# Question 2
def first_odds():
     """a function that prints the odd numbers from 1-100 and returns nothing"""
       
     for num in range(100):

       if num % 2== 1:  # num%2!=0 will get the same result
           print(num)
    
first_odds()     

# Question 3

a_list = [5, 101, 110, 20, 105, 300, 17, 250, 75]
def max_num_in_list(a_list):
   """ a function to find the maximum number in a list"""
   maximum = max(a_list) # this function would still work without the variable declaration
   print("The Maximum number in a_list is ", max(a_list))
max_num_in_list(a_list)

# Question 4

def is_leap_year(a_year):  
 """ a function to return if the given year is a leap year """
 if a_year % 400 == 0 and a_year % 100 == 0:
   print(a_year, "is a leap year")
 # not divided by 100 means not a century year
 # year divided by 4 is a leap year
 elif a_year % 4 ==0 and a_year % 100 != 0:
    print(a_year, "is a leap year")
 else:
   print(a_year, "is not a leap year")
is_leap_year(2000)


# Question 5
def is_consecutive(a_list):
 """ a function to check to see if all numbers in list are consecutive numbers """
 a_list_sorted=sorted(a_list)
 for i in range(1,len(a_list)):   
        if  a_list_sorted[i] ==  a_list_sorted[i-1] + 1:
            return True
        else:
            return False
    
print(is_consecutive(a_list=[2,3,5,4,6]))
