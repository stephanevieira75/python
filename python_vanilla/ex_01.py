import random
import json

# Read values from a JSON file
def read_value_from_json():
    values = []
    # - Open a JSON file with my objects
    with open('characters.json', 'quotes.json') as f:
    # Load all the data contained in my file. data = entries
        data = json.load(f)
        for entry in data:
            values.append(entry['character', 'quote'])
    return values

# Random Quotes function
def random_quote():
    all_values = read_value_from_json()
    return get_random_item(all_values)

# Random Characters function
def random_character():
    all_values = read_value_from_json()
    return get_random_item(all_values)

def get_random_item(my_list):
    # - Get a random number
    rand_numb = random.randint(0,len(my_list) - 1)
    item = my_list[rand_numb]# get a quote from a list
    return item # return the item

def capitalize(words):
    for word in words:
        word.capitalize()

def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{} a dit : {}".format(character, quote)

user_answer = input('Tapez ENTER pour connaitre une autre citation ou B pour quitter le programme.')

while user_answer != "B":
    print(message(random_character(), random_quote()))
    user_answer = input('Tapez ENTER pour connaitre une autre citation ou B pour quitter le programme.')