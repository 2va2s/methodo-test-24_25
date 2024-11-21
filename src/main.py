import datetime

def process_input(user_input, now):
    """
    Traite l'entrée utilisateur et retourne le message à afficher.
    """
    termes = ["Bonjour", "Bonne après-midi", "Bonsoir"]
    if now.hour < 12:
        terme = termes[0]
    elif now.hour < 18:
        terme = termes[1]
    else:
        terme = termes[2]

    if user_input == "exit":
        return f"{terme}", True

    if not all(char.isalpha() or char.isspace() for char in user_input):
        return "Je n'accepte que des mots en entrée", False

    cleaned_input = user_input.replace(" ", "")
    if cleaned_input == cleaned_input[::-1]:
        return "Bien joué", False
    else:
        return user_input[::-1], False
    


def main():
    while True:
        now = datetime.datetime.now()
        exit_message = "(Entrez 'exit' pour quitter)"
        user_input = input(f"{now.hour < 12 and 'Bonjour' or now.hour < 18 and 'Bonne après-midi' or 'Bonsoir'} {exit_message} \n")
        
        response, should_exit = process_input(user_input, now)
        print(response)

        if should_exit:
            break

if __name__ == "__main__":
    main()
