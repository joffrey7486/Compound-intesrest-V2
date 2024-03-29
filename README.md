# Calculateur d'Intérêts Composés

Ce script Python permet de calculer la valeur future d'un investissement en fonction du capital initial, du taux d'intérêt annuel, de la fréquence de paiement et de la durée de l'investissement, en utilisant la formule des intérêts composés.

## Comment Utiliser

1. **Exécution du Script** : Assurez-vous d'avoir Python installé sur votre système. Lancez le script dans votre environnement Python préféré.

2. **Entrée des Valeurs** : Lorsque le programme s'exécute, suivez les instructions pour entrer les valeurs requises :
   - `capital` : Montant initial de l'investissement.
   - `apy` : Taux d'intérêt annuel en décimale (par exemple, 8% doit être entré comme 0.08).
   - `paymentDuration` : Fréquence de paiement (annuel: 1, mensuel: 12, hebdomadaire: 52, quotidien: 365).
   - `years` : Nombre d'années pour l'investissement.

3. **Visualisation du Résultat** : Une fois que toutes les valeurs ont été saisies, le script affichera le capital accumulé à la fin de la période spécifiée.

## Fonctionnement du Code

- La fonction `compoundInterest` calcule la valeur future de l'investissement en utilisant la formule des intérêts composés.
- Elle prend quatre paramètres : `capital`, `apy`, `paymentDuration`, et `years`.
- Le script utilise une boucle `while` pour itérer sur la période de l'investissement et calcule la valeur future en ajoutant les intérêts accumulés à chaque période de paiement.
- Une fois les calculs terminés, le script affiche le capital accumulé à la fin de la période spécifiée.

## Contributions

Les contributions visant à améliorer la fonctionnalité, la lisibilité ou à ajouter des fonctionnalités supplémentaires sont les bienvenues.
