from курсы.cities import cities
cities_set = {city["name"] for city in cities}
print(cities_set)
computer_city = None
last_letter_index = -1
while True:
    user_city = input("Введите город: ")
    if user_city.lower() == 'стоп':
        print("Человек, ты проиграл")
        break
    if user_city in cities_set:
        print("Человек, город найден")
    else:
        print("Человек, город не найден")
        print("Человек, ты проиграл")
        break

    if computer_city and computer_city[last_letter_index].lower != user_city[0].lower():
        print("Человек, ты проиграл")
        break


    cities_set.remove(user_city)

    for city in cities_set:
        if city[0].lower() == user_city[last_letter_index]:
            computer_city = city
            print(f"Компьютер: {computer_city}")
            cities_set.remove(city)
            break
    else:
        print("Человек, ты выиграл!")
        break