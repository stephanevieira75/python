
# Quote
quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau etre ou ne pas etre, nous sommes !" , "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]
user_answer = input('Tapez entree pour connaitre une autre citation ou B pour quitter le programme')
# If user_answer == "B":
if user_answer == "B":
    # - Leave the program
    print('Bye bye !') + exit()
# Elif
elif user_answer == "C":
    print("C pas la bonne reponse, Et G pas d'\humour, je C ...")
# Else: 
else:
    pass
    # - Show another quote

def show_random_quote(my_list):
    # - Get a random number
    item = my_list[0] # Get a quote from a list
    print(item) # Show the quote in the interpreter
    return "Program is over" # Returned value

print(show_random_quote(quotes))