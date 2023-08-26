#!/usr/bin/env python3
#Temprature converter from Fahrenheit to Celsius

def convert_to_celsius(fahrenheit):
    if(fahrenheit == -459.67):
        celsius = (fahrenheit - 32) * (5/9)
        celsius = round(celsius, 2)
    else:
        celsius = (fahrenheit - 32) * (5/9)
    return celsius

