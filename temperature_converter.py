# temprature converter
temperature_celsius = float(input(" Enter the degree celsius: "))
if temperature_celsius < -273.15:
   
   temperature_kelvin = temperature_celsius + 273.15

   temperature_fahrenheit = (temperature_celsius* 9/5) + 32

   print(f"temperature in kelvin = {temperature_kelvin:.2f}")
   print(f"temperature in fahrenheit = { temperature_fahrenheit:.2f}")
print("invalid temperature below absolute zero")