#!/usr/bin/env python3

def admin_login(username, password):
    if username.upper() == "ADMIN" and password == "12345":
        return "Access granted"
    return "Access denied"



def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 65 >= temperature >= 40:
        return "It's a little chilly out there!"
    elif 85 <= temperature:
        return "It's too dang hot out there!"
    return "It's perfect out there!"

def fizzbuzz(num):
    if not num % 15:
        return "FizzBuzz"
    if not num % 5:
        return "Buzz"
    if not num % 3:
        return "Fizz"
    return num
    

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    print ("Invalid operation!")
    return None