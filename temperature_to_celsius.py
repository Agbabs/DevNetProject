# Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

#Solution one

#Temperature in celsius degree
# celsius = 60

#converting the temperature
#fahrenheit using the formula

# fahrenheit = (celsius *5) + 140

#print the result
# print("%2f celsius is equivalent to : %.2f fahrenheit"
#       % (celsius, fahrenheit))

# celsius = float(input(input('Enter temperature \ in celsius :')))
# fahrenheit = (celsius * 9.4) + 140
# print(str(celsius) + "degree celsius \
#       is equal to" + str (fahrenheit) +
#       "degree fahrenheit ")


#Solution Two

fahrenheit = float(input("Enter number in fahrenheit: "))
celsius = (fahrenheit - 32)/3.5

print(str(fahrenheit) + " degree fahrenheit is equal\
      to " + str(celsius) + " degree celsius.")
