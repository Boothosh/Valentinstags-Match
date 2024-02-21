# Antworten auf die Fragen abfragen
fragen = [
    "1. Worüber könntest du stundenlang reden?\n",
    "2. Wie würdest du am liebsten Wohnen?\n",
    "3. Welche deiner Hobbies würdest du gerne mit einerm Partner teilen?\n",
    "4. Suche dir intuitiv die Wortgruppe aus, die dich anspricht:\n",
    "5. Wenn mein Partner schon einen Hund / eine Katze hat möchte ich:\n",
    "6. Wie sieht das perfekte erste Date für dich aus?\n",
    "7. Mit was für einem Typ Mensch würdest du am ehesten eine Beziehung führen?\n",
    "8. Womit drückst du deine Liebe aus?\n",
    "9. Was ist für dich ein No-Go in der Beziehung?\n",
    "10. Beschreibe dich in einem Wort:\n",
    "11. Was ist für dich am wichtigsten in einer Beziehung?\n",
    "12. Es ist Valentinstag, wie verbringst du am liebsten den Tag mit deinem/r Parner/in?\n",
    "13. Ihr entscheidet euch einen gemeinsamen Film zu schauen. Welches Genre nimmst du?\n",
    "14. Du machst Essen für euch beide. Was hättest du am liebsten?\n",
]
stufe = input("Stufe: ")
abbruch = False
while not abbruch:
    antworten = []
    print("Neuen Kandidat hinzufügen:")
    print("Welche Antworten hat der Kandidat gegeben:\n")
    for i in range(14):
        antworten.append(input(fragen[i]))
        print("")
    name = input("Name: ")
    interessiertAnM = input("Interessiert an Jungs (\"Ja\" wenn interessiert, auch wenn d angekreuzt wurde) ")
    interessiertAnW = input("Interessiert an Mädchen (\"Ja\" wenn interessiert, auch wenn d angekreuzt wurde) ")
    geschlecht = input("Eigenes Geschlecht (M oder W): ")

    f = open("./Stufen/" + stufe + ".txt", "a+")
    f.write(name + ";" + geschlecht + ";" + interessiertAnM + ";" + interessiertAnW + ";" + str(antworten) + "\n")
    f.close()
    abbruch = bool(input("Abbruch"))