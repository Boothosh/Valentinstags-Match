import ast
klasse = input("Klasse (in Großbuchstaben, z.B. \"9A\"): ")
anzahlDerMatches = 3

f = open("./Stufen/" + klasse + ".txt", "r")
lines = f.readlines()
for i in lines:
    name = i.split(";")[0]
    eigeneAnworten = []
    stehtAufJungs = False
    stehtAufMaedchen = False
    eigenesGeschlechtIstJunge = False

    for i in lines:
        neuersplit = i.split(";")
        if neuersplit[0] == name:
            eigenesGeschlechtIstJunge = neuersplit[1] == "M"
            stehtAufJungs = neuersplit[2] == "Ja"
            stehtAufMaedchen = neuersplit[3] == "Ja"
            eigeneAnworten = ast.literal_eval(neuersplit[4])
            break
    # Nach möglichen Treffern suchen
    scores = []
    for i in lines:
        neuersplit = i.split(";")
        score = 0
        if neuersplit[0] != name:
            antworten = ast.literal_eval(neuersplit[4])
            for i in range(14):
                if antworten[i] == eigeneAnworten[i]:
                    score += 1
        
        # Steh ich auf das Geschlecht der Person?
        # Wenn ja dann soll das stark gewichtet werden
        if (stehtAufJungs and (neuersplit[1] == "M")) or (stehtAufMaedchen and (neuersplit[1] == "W")):
            score *= 10

        # Steht die Person auf das Geschlecht von mir?
        # Wenn ja dann soll das stark gewichtet werden
        if (eigenesGeschlechtIstJunge and (neuersplit[2] == "Ja")) or (not eigenesGeschlechtIstJunge) and (split[3] == "Ja"):
            score *= 10
        
        # Begründung für die starken Gewichte:
        # Ich will ja nicht mit meinem besten Freund gematched werden, nur
        # weil der die gleichen Antworten gegeben hat wie ich.

        scores.append((neuersplit[0], score))

    scores.sort(key=lambda schueler: schueler[1], reverse=True)
    print(name)
    for i in range(anzahlDerMatches):
        print(str(i+1) + ". " + scores[i][0])
    print("---")
        