# temperature converter
temperature_celsius = float(input(" Enter the degree celsius: "))
temperature_kelvin = temperature_celsius + 273.15
temperature_fahrenheit = (temperature_celsius* 9/5) + 32
if temperature_celsius < -273.15:
   print("invalid temperature below absolute zero")
else:
   temperature = input("Do you want in 'Kelvin'or 'Fahrenheit'? ")
   if temperature == "Kelvin":
       print(f"temperature in kelvin = {temperature_kelvin:.2f}")
   elif temperature == "Fahrenheit":
       print(f"temperature in fahrenheit = { temperature_fahrenheit:.2f}")
   else:
       print("Invalid input")
