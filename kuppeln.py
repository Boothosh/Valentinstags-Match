import ast
stufe = input("Stufe: ")

f = open("./Stufen/" + stufe + ".txt", "r")
out = open("./Output/" + stufe + ".txt", "w")
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
    jungsScores = []
    maedchenScores = []
    gemischtScores = []
    for i in lines:
        neuersplit = i.split(";")
        score = 0
        if neuersplit[0] != name:
            antworten = ast.literal_eval(neuersplit[4])
            for i in range(14):
                if antworten[i] == eigeneAnworten[i]:
                    score += 1

        if (neuersplit[1] == "M"):
            jungsScores.append((neuersplit[0], score))
        else:
            maedchenScores.append((neuersplit[0], score))
        gemischtScores.append((neuersplit[0], score))

    jungsScores.sort(key=lambda schueler: schueler[1], reverse=True)
    maedchenScores.sort(key=lambda schueler: schueler[1], reverse=True)
    gemischtScores.sort(key=lambda schueler: schueler[1], reverse=True)
    
    out.write(name)
    out.write("\n\nJungen-Matches:\n")
    for i in range(3):
        out.write(str(i+1) + ". " + jungsScores[i][0])
        out.write("\n")
    out.write("\nMädchen-Matches:\n")
    for i in range(3):
        out.write(str(i+1) + ". " + maedchenScores[i][0])
        out.write("\n")
    out.write("\nGemischt-Matches:\n")
    for i in range(3):
        out.write(str(i+1) + ". " + gemischtScores[i][0])
        out.write("\n")
    out.write("\n---\n\n")
        