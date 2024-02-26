# Capital => initial number, apy => 8% => 0.08, paymentDuration => every day 365 every week 52 every months 12, year => total number years invest
def compoundInterest(capital, apy, paymentDuration, years):
    totalPayment = paymentDuration * years
    eachPayment = 0
    while eachPayment < totalPayment:
        capital += (capital * apy) / paymentDuration
        eachPayment += 1
    return capital

