# Answer for question 1:

Text = input()
main_text = ''.join(sorted(Text))
print(main_text)


# Answer for question 2:

a =int(input( ))
b =int(input( ))

print(a, "+", b, "is", a + b)
print(a, "-", b, "is", a - b)
print(a, "*", b, "is", a * b)
print(a, "/", b, "is", a / b)
print(a, "%", b, "is", a % b)
print(a, "^", b, "is", a ** b)

# Answer for question 3:

n =int(input())

result= {}

for i in range(1,n+1):
    result[i] =i*i
    
print(result)


# Answer for question 4:

n= int(input())

sum=n*(n+1)//2
    
print(f'The sum of the first {n} positive integers is {sum}')


#Answer for question 5:

s = input()

vowels= "aeiou"

count=0
for i in s.lower():
    if i in vowels:
        count= count +1

print(f"Number of vowels: {count}")

#Answer for question 6:

total = 0

while True:
    value =input()
    try:
        num=float(value)
    except:
        print("That wasn't a number.")
        continue
    if num == 0:
        print(f"The grand total is {total}")
        break
    total =total + num
    
    print(f"The total is now {total}")
    

#Answer for question 7:


def custom_encoder():
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    text = input("Enter text: ")
    positions = []
    
    for i in text:
        if i == ",":
            continue
        
        lower_text = i.lower()
        
        if lower_text in reference_string:
            positions.append(reference_string.index(lower_text))
        else:
            positions.append(-1)
            
    return positions

print(custom_encoder())


#Answer for question 8:

class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'Hello, my name is {self.name}')


#Anser for question 9:

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"{self.name} is open. Come on in!")
        

#Answer fof question 10:

class User:
    def __init__(self,first_name,last_name,uname,email,location):
        self.first_name = first_name
        self.last_name = last_name
        self.uname = uname
        self.email =email
        self.location = location
    
    def describe_user(self):
        print(f'Name: {self.first_name} {self.last_name} \n'
             f'Username: {self.uname}\n'
             f'Email: {self.email}\n'
             f'Location: {self.location}')

    def greet_user(self):
        print(f'Welcome back {self.uname}!')

#Answer for question 11:

def combine_lists(list1, list2):
    i = 0
    j = 0
    combined = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            combined.append(list1[i])
            i = i+ 1
        else:
            combined.append(list2[j])
            j=j+ 1

    while i < len(list1):
        combined.append(list1[i])
        i =i+ 1

    while j < len(list2):
        combined.append(list2[j])
        j =j + 1

    return combined





    
