# Код
with open("recipes.txt", mode="r") as file_object:
    recipes = ""
    for line in file_object:
        recipes += line
cook_book = {}
for line in recipes.split("\n\n"):
    recipe = line.split("\n")
    name = recipe[0]
    num_of_ingr = int(recipe[1])
    ingr_list = []
    for _ in range(2, 2 + num_of_ingr):
        ingredients = {}
        ingredients["ingredient_name"] = recipe[_].split(" | ")[0]
        ingredients["quantity"] = recipe[_].split(" | ")[1]
        ingredients["measure"] = recipe[_].split(" | ")[2]
        ingr_list.append(ingredients)
    cook_book[name] = ingr_list

ava_dishes_list = []
for k in cook_book.keys():
    ava_dishes_list.append(k)


def get_shop_list_by_dishes(dishes, person_count):
    list_of_ingr_to_shop = {}
    for k, v in cook_book.items():
        if k in dishes:
            for _ in v:
                num_of_ingr_to_shop = {}
                num_of_ingr_to_shop["measure"] = _["measure"]
                if _["ingredient_name"] not in list_of_ingr_to_shop:
                    num_of_ingr_to_shop["quantity"] = int(_["quantity"]) * person_count
                else:
                    num_of_ingr_to_shop["quantity"] = list_of_ingr_to_shop[_["ingredient_name"]]["quantity"] + int(
                    _["quantity"]) * person_count
                list_of_ingr_to_shop[_["ingredient_name"]] = num_of_ingr_to_shop
    print("Список необходимых ингредиентов:")
    for k,v in list_of_ingr_to_shop.items():
        print(k, v)


dishes = []
while True:
    for number in range(1, len(ava_dishes_list)+1):
        print(f"", number, " : ", ava_dishes_list[number-1])
    dish_number = int(input("Выберите номер блюда из доступных: "))
    dishes.append(ava_dishes_list[dish_number-1])
    print(f"Вы выбрали", ava_dishes_list[dish_number-1])
    action = input("Хотите добавить еще одно блюдо? (да/нет) ")
    if action == "нет":
        break
person_count = int(input("Укажите количество персон:" ))
print(f"Вы выбрали", dishes, "на", person_count, "персон")

get_shop_list_by_dishes(dishes, person_count)


# Тестирование кода

# print(cook_book)
