from abc import ABC, abstractmethod


class Courrier(ABC):
    def __init__(self, poids, mode_expedition, adresse_destination, adresse_expedition):
        self.poids = poids  # en grammes
        self.mode_expedition = mode_expedition  # "normal" ou "rapide"
        self.adresse_destination = adresse_destination
        self.adresse_expedition = adresse_expedition

    def poids_kg(self):
        return self.poids / 1000

    def appliquer_mode(self, prix):
        if self.mode_expedition == "rapide":
            return prix * 2
        return prix

    @abstractmethod
    def calcul_affranchissement(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Lettre(Courrier):
    def __init__(self, poids, mode_expedition,
                 adresse_destination, adresse_expedition,
                 format_lettre):
        super().__init__(poids, mode_expedition,
                         adresse_destination, adresse_expedition)
        self.format_lettre = format_lettre  # "A3" ou "A4"

    def calcul_affranchissement(self):

        if self.format_lettre == "A4":
            tarif_base = 2.50
        elif self.format_lettre == "A3":
            tarif_base = 3.50
        else:
            raise ValueError("Format de lettre invalide")

        prix = tarif_base + self.poids_kg()
        return self.appliquer_mode(prix)

    def __str__(self):
        return (
            f"Lettre {self.format_lettre} - "
            f"{self.poids} g - "
            f"mode : {self.mode_expedition} - "
            f"de {self.adresse_expedition} à {self.adresse_destination} - "
            f"prix : {self.calcul_affranchissement():.2f} €"
        )


class Colis(Courrier):
    def __init__(self, poids, mode_expedition,
                 adresse_destination, adresse_expedition,
                 volume):
        super().__init__(poids, mode_expedition,
                         adresse_destination, adresse_expedition)
        self.volume = volume  # en litres

    def calcul_affranchissement(self):

        prix = (self.volume / 4) + self.poids_kg()
        return self.appliquer_mode(prix)

    def __str__(self):
        return (
            f"Colis {self.volume} L - "
            f"{self.poids} g - "
            f"mode : {self.mode_expedition} - "
            f"de {self.adresse_expedition} à {self.adresse_destination} - "
            f"prix : {self.calcul_affranchissement():.2f} €"
        )


class BoiteAuxLettres:
    def __init__(self):
        self.courriers = []

    def ajouter_courrier(self, courrier):
        self.courriers.append(courrier)

    def total_affranchissement(self):
        return sum(c.calcul_affranchissement() for c in self.courriers)

    def __str__(self):
        resultat = "Boîte aux lettres :\n"
        for c in self.courriers:
            resultat += str(c) + "\n"
        resultat += f"Total : {self.total_affranchissement():.2f} €"
        return resultat