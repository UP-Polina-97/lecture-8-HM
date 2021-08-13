from pprint import pprint
cook_book = {}

def record_cook_book(file):
  with open(file, 'r', encoding='utf-8') as menu:
    for line in menu:
        ingredients = []
        recipe_name = line.strip()
        ingredients_amount = int(menu.readline().strip())
        for i in range(ingredients_amount):
            name, count, mesure = menu.readline().strip().split("|")
            ingredients.append({'ingredient_name': name.strip(),'quantity': int(count), 'measure': mesure.strip(),})
        menu.readline()
        cook_book[recipe_name] = ingredients

  return (cook_book)
p = record_cook_book('recipes.txt')
print(p)

print('')
print('exercise 2:')
print('')

shop_list = {}

def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        for ingredients in cook_book[dish]:
            shop_list[ingredients['ingredient_name']] = {'measure': ingredients['measure'], 'quantity': int(ingredients['quantity'] * person_count)}
        [print(key, ':', value) for key, value in shop_list.items()]




list_for_shop = get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)
print(list_for_shop)
