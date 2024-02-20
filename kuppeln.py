import ast
name = input("Name: ")
klasse = input("Klasse (in Großbuchstaben, z.B. \"9A\"): ")
anzahlDerMatches = int(input("Anzahl der Matches: "))

f = open("./Klassen/" + klasse + ".txt", "r")
eigeneAnworten = []
stehtAufJungs = False
stehtAufMaedchen = False
eigenesGeschlechtIstJunge = False
lines = f.readlines()
for i in lines:
    split = i.split(";")
    if split[0] == name:
        eigenesGeschlechtIstJunge = split[1] == "M"
        stehtAufJungs = split[2] == "Ja"
        stehtAufMaedchen = split[3] == "Ja"
        eigeneAnworten = ast.literal_eval(split[4])
        break
# Nach möglichen Treffern suchen
scores = []
for i in lines:
    split = i.split(";")
    score = 0
    if split[0] != name:
        antworten = ast.literal_eval(split[4])
        for i in range(14):
            if antworten[i] == eigeneAnworten[i]:
                score += 1
        
        # Steh ich auf das Geschlecht der Person?
        # Wenn ja dann soll das stark gewichtet werden
        if (stehtAufJungs and (split[1] == "M")) or (stehtAufMaedchen and (split[1] == "W")):
            score *= 10

        # Steht die Person auf das Geschlecht von mir?
        # Wenn ja dann soll das stark gewichtet werden
        if (eigenesGeschlechtIstJunge and (split[2] == "Ja")) or (not eigenesGeschlechtIstJunge) and (split[3] == "Ja"):
            score *= 10
        
        # Begründung für die starken Gewichte:
        # Ich will ja nicht mit meinem besten Freund gematched werden, nur
        # weil der die gleichen Antworten gegeben hat wie ich.

        scores.append((split[0], score))

scores.sort(key=lambda schueler: schueler[1], reverse=True)
for i in range(anzahlDerMatches):
    print(str(i+1) + ". " + scores[i][0])
        