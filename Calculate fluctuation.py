def calculateDluctuation(initialPrice, finalPrice, years):
    fluctuation = ((finalPrice / initialPrice) ** (1 / years)) - 1
    percentage = fluctuation * 100
    decimal = fluctuation
    
    print("La fluctuation annuelle de l'actif est de {:.2f}%".format(percentage))
    print("Cela correspond à une valeur décimale de {:.10f}".format(decimal))
    return percentage, decimal

calculateDluctuation(70000, 600000, 20)