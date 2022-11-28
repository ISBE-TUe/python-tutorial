# import converter
from converter import validate_input_and_convert
from converter import validate_input_and_convert as show_temp

user_input = ''
while user_input != "exit":
    user_input = input('Give the temperature in degrees celsius and I will convert it to Fahrenheit!')
    temp_and_city = user_input.split(",")
    print(temp_and_city)
    if user_input != 'exit':
        temp_and_city_dictionary = {"temp": temp_and_city[0], "city": temp_and_city[1]}
    print(temp_and_city_dictionary)
    # converter.validate_input_and_convert(temp_and_city_dictionary)
    validate_input_and_convert(temp_and_city_dictionary)
    # show_temp(temp_and_city_dictionary)