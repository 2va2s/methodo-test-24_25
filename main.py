import datetime

def main():
    while True:
        now = datetime.datetime.now()
        exit_message = "(Entrez 'exit' pour quitter)"
        termes = ["Bonjour", "Bonne après-midi", "Bonsoir"]
        
        if now.hour < 12:
            terme = termes[0]
        elif now.hour < 18:
            terme = termes[1]
        else:
            terme = termes[2]
        
        user_input = input(f"{terme} {exit_message} \n")
        if user_input == "exit":
            print(f"{terme}")
            break


        if not all(char.isalpha() or char.isspace() for char in user_input):
            print("Je n'accepte que des mots en entrée")
            continue

        cleaned_input = user_input.replace(" ", "")
        if cleaned_input[::-1] == cleaned_input:
            print("Bien joué")
        else:
            print(user_input[::-1])

if __name__ == "__main__":
    main()