# Capital => initial number, apy => 8% => 0.08, paymentDuration => every day 365 every week 52 every months 12, year => total number years invest
def compoundInterest(capital, apy, paymentDuration, years):
    totalDays = years * 365
    days = 1
    i = 0
    while days < totalDays:
       if days % paymentDuration == 0:
            interest = (capital * apy) / (365 / paymentDuration)
            capital += interest
            print("Hello {}".format(i))
       days += 1
    print("Voici votre capital au bout de {} ans: {}".format(years, capital))
    return capital




# Demander à l'utilisateur d'entrer les valeurs nécessaires
capital = float(input("Entrez le capital initial : "))
apy = float(input("Entrez le taux d'intérêt annuel (sous forme décimale) : "))
paymentDuration = int(input("Entrez la durée du paiement (annuel: 1, mensuel: 12, hebdomadaire: 52, journalier: 365) : "))
years = int(input("Entrez le nombre d'années : "))

# Appel de la fonction
compoundInterest(capital, apy, paymentDuration, years)