
 




burgers = [" чизбургер ", " гамбургер ", " двойной чизбургер ", " двойной гамбургер "]
add_ons = [" с беконом "," с яйцом "," с картошкой фри"," с перцем чили "]

print (f"Доступные бургеры:\n {','.join(burgers) }")
print (f"Доступные дополнения:\n {','.join(add_ons) }")

while True:
    burger = input("\n Введите номер или 'q' для выхода:")
    if burger == 'q':
        break 
    elif burger.isnumeric():
        try:
            burger = int(burger) -1 
        except ValueError: 
            print("\n Неверный ввод! Попробуйте еще раз")
            continue 
    else: 
        print("\n Наверное введен номер! Введите число или 'q' для выхода")        
        continue 
    addon = input("Хотите добавить что нибудь к вашему заказу? Ввудите 'да' или 'нет':  ")
    while addon not in ("да","нет"):
        addon = input("Пожалуйста ответте 'да' или 'нет'. \n")
        
    