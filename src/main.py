import pyfiglet
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from CCoinBox import CCoinBox
f = pyfiglet.Figlet(font='slant')
print(f.renderText("CCoinBox"))



def main():
    coinBox = CCoinBox()
    action = True
    while action is not None:
        action = inquirer.select(
            message="Sélectionnez une option:",
            choices=[
                "Reset",
                "Vente",
                "Ajouter 25c",
                "Retourner monnaie",
                Choice(value=None, name="Exit"),
            ],
            default=None,
        ).execute()
        print(Separator())
        if action == "Reset":
            coinBox.reset()
        elif action == "Vente":
            coinBox.vente()
        elif action == "Ajouter 25c":
            coinBox.ajouter_25c()
        elif action == "Retourner monnaie":
            coinBox.retourne_monnaie()
        print(Separator())


if __name__ == "__main__":
    main()

#print("Sélectionnez une option: [Reset][Vente][Ajouter 25c][Retourner monnaie]")