#Capital => initial number, apy => 8% => 0.08, paymentDuration => every day 365 every week 52 every months 12, year => total number years invest
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



# Appel de la fonction
print(compoundInterest(100, 0.1, 52, 2)) #122.11681962413883
#print(compoundInterest(250, 0.08, 365, 3))#317.80393001291145
#print(compoundInterest(2369, 0.08, 12, 22))#13689.473815862011
