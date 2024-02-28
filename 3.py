#задание 1
# запрашиваем у пользователя номер телефона
phone_number = input("Введите номер телефона: ")

# удаляем все символы, кроме цифр и плюса
digits = "".join(filter(str.isdigit, phone_number))

# проверяем длину номера
if len(digits) != 11:
    print("Номер телефона должен содержать 11 цифр")
#проверка на то что номер начинается на +7 или 8
elif not (digits.startswith('8') or digits.startswith('7')):
    print("Номер телефона должен начинаться с + или 8")
#проверка на то что номер не содержит букв
elif not digits[1:].isdigit():
    print("Номер телефона должен состоять только из цифр")
else:
    print("Номер телефона введен корректно")

#задание 2
password = input("Введите пароль: ")

if len(password) < 8:
    print("Пароль слишком короткий, придумайте другой.")
elif ' ' in password:
    print("Пароль не может содержать пробелы, придумайте другой.")
elif not any(char.isupper() for char in password):
    print("Пароль должен содержать хотя бы одну заглавную букву, придумайте другой.")
elif not any(char.islower() for char in password):
    print("Пароль должен содержать хотя бы одну строчную букву, придумайте другой.")
elif not any(char.isdigit() for char in password):
    print("Пароль должен содержать хотя бы одну цифру, придумайте другой.")
else:
    print("Пароль надежный!")

#задание 3
secret_letter = [['DFВsjl24sfFFяВАДОd24fssflj234'], ['asdfFп234рFFdо24с$#afdFFтasfо'],
['оafбasdf%^о^FFжа$#af243ю'],['afпFsfайFтFsfо13н'],
['fн13Fа1234де123юsdсsfь'], ['чFFтF#Fsfsdf$$о'],
['и$ #sfF'], ['вSFSDам'],['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
['FFэasdfтDFsfоasdfFт'], ['FяDSFзFFsыSfкFFf']]

small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

decoded_letter = []
for word in secret_letter:
    # Преобразуем слово в строку
    word_str = ''.join(word)
    decoded_word = ''
    for char in word_str:
        # Если символ является маленькой русской буквой, добавляем его в расшифрованное слово
        if char.lower() in small_rus:
            decoded_word += char
    # Добавляем расшифрованное слово в список decoded_letter
    decoded_letter.append(decoded_word)

print(' '.join(decoded_letter))








