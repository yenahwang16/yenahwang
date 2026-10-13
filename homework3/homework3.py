# 3.1 Say Goodbye
def say_goodbye(name):
    print("Goodbye,", name)

# 3.2 Area of a Circle
def circle(radius):
    print(radius ** 2 * 3.14)

# Test calls
say_goodbye("Yena")
circle(2)
circle(5)

# 4.1 Subtract, Multiply, and Divide
def subtract(a,b):
    return a - b

def multiply(c,d):
    return c * d

def divide(e,f):
    return e / f

#Test calls
print(subtract(9,2))
print(multiply(596,1873))
print(divide(17830489,2874))

#5.1 What Should I Wear?
def temperature_range(readings):
    lowest = min(readings)
    highest = max(readings)
    return (lowest, highest)

#Test calls
temperatures = [15, 30, 50, 68, 32, 59]
print(temperature_range(temperatures))

#5.2 Check if it's the Weekend

Monday=1
Tuesday=2
Wednesday=3
Thursday=4
Friday=5
Saturday=6
Sunday=7

def is_weekend(day):
    if day>=6:
        return True
    else:
        return False

#Test calls
print(is_weekend(4))
print(is_weekend(6))

#5.3 Fuel Efficiency Calculator

def fuel_efficiency(distance, fuel_used):
    return distance / fuel_used

#Test calls
print(300,15)

#5.4 Secret Code

def major_discovery(data):
    last_digit = data % 10
    remaining = data // 10
    places = len(str(data))-1
    
    return (last_digit) * 10**(places) + remaining 

#Test calls
data=5782
print(major_discovery(data))

#6.1 Oski Stole Your Power

def power(x,y):
    result = 1

    for step in range(y):
        result = result * x

    return(result)

#6.2 Min & Max with Loops!

#6.2.1
def list_min_for(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest

def list_max_for(numbers):
    biggest = numbers[0]

    for number in numbers:
        if number > biggest:
            biggest = number 
    
    return biggest

#6.2.2
def list_min_while(numbers):
    smallest = numbers[0]
    index = 0

    while index < len(numbers):
        number = numbers[index]

        if number < smallest:
            smallest = number

        index += 1
    
    return smallest

def list_max_while(numbers):
    biggest = numbers[0]
    index = 0

    while index < len(numbers):
        number = numbers[index]

        if number > biggest:
            biggest = number 
        
        index += 1

        return biggest

#6.3 Calculate the Sum

def sum(number):
    if number < 0:
        number = -number

    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number //= 10

    return total

print(sum(2468))	

number = 2468
result = sum(number)

print(f"The sum of the digits in {number} is {result}.")