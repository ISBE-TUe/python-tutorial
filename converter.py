def celsius_to_fahrenheit(deg_c, city):
    deg_f = deg_c * 9/5 + 32
    return f"It is {deg_c}°C ({deg_f}°F) in {city} today."

def validate_input_and_convert(temp_and_city_dictionary):
    # print(temp_and_city[0])
    if temp_and_city_dictionary['temp'].isdigit():
        user_input_as_num = int(temp_and_city_dictionary['temp'])
        deg_f = celsius_to_fahrenheit(user_input_as_num, temp_and_city_dictionary['city'])
        print(deg_f)
    else:
     print('Cannot convert a non numeric value, sorry!')