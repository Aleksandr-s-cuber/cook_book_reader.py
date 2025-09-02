# Задание_1

from pprint import pprint
def create_cook_book(file_path: str) -> dict:


    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break

            ingredients_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient_line = file.readline().strip()
                ingredient, quantity, measure = ingredient_line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient,
                    'quantity': int(quantity),
                    'measure': measure
                })

            cook_book[dish_name] = ingredients
            file.readline()

    return cook_book


if __name__ == '__main__':
    file_path = 'recipes.txt'

    cook_book = create_cook_book(file_path)
    pprint(cook_book,sort_dicts=False)


# Задание_2

from typing import List, Dict

def create_cook_book(file_path: str) -> dict:


    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break

            ingredients_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient_line = file.readline().strip()
                ingredient, quantity, measure = ingredient_line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient,
                    'quantity': int(quantity),
                    'measure': measure
                })

            cook_book[dish_name] = ingredients
            file.readline()

    return cook_book



def get_shop_list_by_dishes(dishes: List[str], person_count: int, cook_book: Dict) -> Dict:

    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            print(f"Рецепт для блюда '{dish}' не найден в кулинарной книге.")
            continue

        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']

            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
            else:
                shop_list[ingredient_name]['quantity'] += quantity

    return shop_list


if __name__ == '__main__':
    file_path = 'recipes.txt'



    cook_book = create_cook_book(file_path)

    dishes_to_cook = ['Запеченный картофель', 'Омлет']
    person_count = 2

    shop_list = get_shop_list_by_dishes(dishes_to_cook, person_count, cook_book)

    for ingredient, details in shop_list.items():
        print(f"{ingredient}: {details}")



# Задание_3


from typing import List

def merge_files_by_line_count(file_names: List[str], output_file: str) -> None:


    file_data = []
    for file_name in file_names:
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                file_data.append((file_name, len(lines), lines))
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден.")
        except Exception as e:
            print(f"Ошибка при чтении файла '{file_name}': {e}")






if __name__ == '__main__':

    file1_content = ["Начальник  полиции 1\n", "лично позвонил в шестнадцатый участок. А спустя  одну минуту тридцать секунд 1\n"]
    file2_content = ["Тревога началась в тринадцать часов ноль две минуты. 2\n"]
    file3_content = [" В  это время  дня  машины текли сплошным  блестящим  потоком,  а  среди 3\n", "потока, будто  колонны из бетона  и стекла, высились  здания. Здесь,  в мире 3\n", "резких граней,  люди  на тротуарах  выглядели  несчастными и  неприкаянными. 3\n"]


    with open("1.txt", "w", encoding="utf-8") as f:
        f.writelines(file1_content)

    with open("2.txt", "w", encoding="utf-8") as f:
        f.writelines(file2_content)

    with open("3.txt", "w", encoding="utf-8") as f:
        f.writelines(file3_content)


    file_names = ["1.txt", "2.txt", "3.txt"]
    output_file = "result.txt"

    merge_files_by_line_count(file_names, output_file)

    print(f"Файлы {file_names} объединены в {output_file}")
