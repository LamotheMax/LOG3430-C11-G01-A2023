import pyfiglet
import logging
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from CCoinBox_w_logs import CCoinBox


# create logger
logger = logging.getLogger('CCoinbox')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.FileHandler('CCoinbox.log')
#ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


f = pyfiglet.Figlet(font='slant')
print(f.renderText("CCoinBox"))

def main():
    logger.info("Debut de programme")

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
    logger.info('Fin de Log')


if __name__ == "__main__":
    main()

#print("Sélectionnez une option: [Reset][Vente][Ajouter 25c][Retourner monnaie]")