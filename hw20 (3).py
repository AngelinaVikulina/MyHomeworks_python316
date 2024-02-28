
import json


def check_city(user_city, cities_set):
    if user_city in cities_set:
        print("Человек, город найден")
        return True
    else:
        print("Человек, город не найден")
        return False


def check_last_letter(computer_city, user_city):
    if computer_city and computer_city[-1].lower() != user_city[0].lower():
        print("Человек, ты проиграл")
        return True
    return False


def main():
    with open("cities.json", "r", encoding="windows-1251") as file:
        cities = json.load(file)

    cities_set = {city["name"] for city in cities}
    computer_city = None
    last_letter_index = -1

    while True:
        user_city = input("Введите город: ")

        if user_city.lower() == 'стоп':
            print("Человек, ты проиграл")
            break

        if not check_city(user_city, cities_set):
            print("Человек, ты проиграл")
            break

        if check_last_letter(computer_city, user_city):
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


if __name__ == "__main__":
    main()
