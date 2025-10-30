my_string = "heLLo"
print(my_string)
my_string = "hELlo"
print(my_string)
my_string = my_string[0].upper() + my_string[1:].lower()

user_name = input("What is your name?\n")

if (user_name == "") :
    print(f"Now that is a error.")
else:
    print(f'{my_string} {user_name}.')
    print(f"{12/5.3}")

def get_user_age():
    global user_age
    user_age = int(input(f"How old are you {user_name}?\n"))

    if (user_age <= 1):
        print(f"Now that is a age error")
    else:
        print(f"Well, thats good news. Now I know that {user_name} is {user_age} years old.")

get_user_age()

if user_age >= 18:
    print('You are an adult')
elif user_age >= 13:
    print('You are a teenager')
else:
    print('You are a child')

def sum(num1,num2):
    return(f"\n{num1}+{num2}={num1+num2}\n")

result = sum(int(input("the first number:\n")),int(input("the second number:\n")))

print(result)

def say_bye():
   return 'Bye ' + user_name

def uppercase_decorator(func):
   def wrapper():
       original_func = func()
       modified_func = original_func.upper()
       return modified_func
   return wrapper

say_hello_res = uppercase_decorator(say_bye)

print(say_hello_res())

is_student = False

if user_age < 18 or is_student:
    print('You are eligible for a student discount')
else:
    print('You are not eligible for a student discount')

# For all arch users: I use Nixos btw.
# Js && = Py and
# Js || = Py or
# Js ! = Py not