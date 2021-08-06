#cook_book = {}
with open('recipes.txt', 'r', encoding='utf-8') as menu:
    for line in menu:
        ingredients = []
        cook_book = {}
        recipe_name = line.strip()
        ingredients_amount = int(menu.readline().strip())
        for i in range(ingredients_amount):
            #menu.readline().strip()
            name, count, mesure = menu.readline().strip().split("|")
            ingredients.append({'ingredient_name': name.strip(),'quantity': int(count), 'measure': mesure.strip() })
        menu.readline()
        cook_book[recipe_name] = ingredients
        print(cook_book)

print('exercise 2:')
shop_list = {}

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for key, value in cook_book.items():
    if dishes == key:
      shop_list.add(value)
      shop_list['quantity'] * person_count
      print(shop_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)