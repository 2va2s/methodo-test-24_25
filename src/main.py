import datetime

def get_terme(now):
    termes = ["Bonjour", "Bonne après-midi", "Bonsoir"]
    if now.hour < 12:
        return termes[0]
    elif now.hour < 18:
        return termes[1]
    else:
        return termes[2]

def is_valid_input(user_input):
    return all(char.isalpha() or char.isspace() for char in user_input)

def is_palindrome(cleaned_input):
    return cleaned_input == cleaned_input[::-1]

def main():
    while True:
        now = datetime.datetime.now()
        exit_message = "(Entrez 'exit' pour quitter)"
        terme = get_terme(now)
        
        user_input = input(f"{terme} {exit_message} \n")
        if user_input == "exit":
            print(f"{terme}")
            break

        if not is_valid_input(user_input):
            print("Je n'accepte que des mots en entrée")
            continue

        cleaned_input = user_input.replace(" ", "")
        if is_palindrome(cleaned_input):
            print("Bien joué")
        else:
            print(user_input[::-1])

if __name__ == "__main__":
    main()