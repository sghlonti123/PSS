print("Hello World")
print("Hello World", 1, 2, 3)

def my_function():
    print("Please Print Something Original")
    print("I can't :(((")

my_function()

def my_cool_function(some_variable):
    print("Well, now i can :))", some_variable)

my_cool_function("Original text from shako")
my_cool_function(100)
my_cool_function("Something cool from cool function")

def my_cool_function_with_more_variables(some_variable, some_other_variable, third_one):
    print("Well, now i can :))", some_variable, some_other_variable, third_one)

variable = 100
my_cool_function_with_more_variables(variable,2,3)


def main_function():
    user_age = read_users_info()
    check_the_age(user_age)

def read_users_info():
    age = int(input("Tell me your age: "))
    return age

def check_the_age(age):
    my_age = 24
    if age > my_age:
        print("You are older than me")
    elif age < my_age:
        print("You are not older than me")
    elif age == my_age:
        print("We are the same age")

read_users_info()


# Write Calculator Which interacts with user