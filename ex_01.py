# Quotes
quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau etre ou ne pas etre, nous sommes !" , "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]

characters = ["alvin et les Chipmunks", "babar", "betty boop", "calimero", "casper", "le chat potte"]
def show_random_quote(my_list):
    # - Get a random number
    item = my_list[0] # Get a quote from a list
    return item # Returned value

user_answer = input('Tapez entree pour connaitre une autre citation ou B pour quitter le programme')
while user_answer != "B":
    print(show_random_quote(quotes))
    user_answer = input('Tapez entree pour connaitre une autre citation ou B pour quitter le programme')

for character in characters:
    n_character = character.capitalize()
    print(n_character)
