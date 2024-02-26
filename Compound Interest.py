# Capital => initial number, apy => 8% => 0.08, paymentDuration => every day 365 every week 52 every months 12, year => total number years invest
def compoundInterest(capital, apy, paymentDuration, years):
    totalPayment = paymentDuration * years
    eachPayment = 0
    while eachPayment < totalPayment:
        capital += (capital * apy) / paymentDuration
        eachPayment += 1
    print(capital)
    return capital


# Demander à l'utilisateur d'entrer les valeurs nécessaires
capital = float(input("Entrez le capital initial : "))
apy = float(input("Entrez le taux d'intérêt annuel (sous forme décimale) : "))
paymentDuration = int(input("Entrez la durée du paiement (annuel: 1, mensuel: 12, hebdomadaire: 52, journalier: 365) : "))
years = int(input("Entrez le nombre d'années : "))

# Appel de la fonction
compoundInterest(capital, apy, paymentDuration, years)