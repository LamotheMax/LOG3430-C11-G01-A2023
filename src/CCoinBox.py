import logging
logger = logging.getLogger('CCoinbox')


class CCoinBox:
    monnaie_totale = 0
    monnaie_courante = 0
    vente_permise = False

    def __init__(self):
        self.reset()

    def ajouter_25c(self):
        logger.debug("starting ajouter_25c")
        logger.debug(f"monnaie_courante before: {self.monnaie_courante}")
        self.monnaie_courante = self.monnaie_courante + 1
        if self.monnaie_courante > 1:
            self.vente_permise = True
        logger.debug(f"monnaie_courante after: {self.monnaie_courante}")
        logger.debug(f"vente_permise {self.vente_permise}")
        print("Une pièce a été ajoutée")

    def vente(self):
        logger.debug("starting vente")
        if self.vente_permise:
            logger.debug(f"vente_permise {self.vente_permise}")
            logger.debug(f"monnaie_courante before {self.monnaie_courante}")
            self.monnaie_totale = self.monnaie_totale + 2
            self.monnaie_courante = self.monnaie_courante - 1
            print("Vente! Voici votre article ...")
            logger.debug(f"monnaie_courante after {self.monnaie_courante}")
            if self.monnaie_courante < 2:
                self.vente_permise = False
                logger.debug(f"vente_permise {self.vente_permise}")

    def reset(self):
        logger.debug("starting reset")
        self.monnaie_totale = 0
        self.monnaie_courante = 0
        self.vente_permise = False
        print("Machine reset")

    def retourne_monnaie(self):
        logger.debug("starting retour monnaie")
        self.monnaie_courante = 0
        logger.debug(f"monnaie_courante = {self.monnaie_courante}")
        logger.debug(f"vente_permise = {self.vente_permise}")
        print("Voici votre monnaie")

    def get_monnaie_totale(self):
        return monnaie_totale

    def get_monnaie_courante(self):
        return monnaie_courante

    def get_vente_permise(self):
        return vente_permise