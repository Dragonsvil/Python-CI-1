def analyse_lexicale(texte):
    # rendre le texte homogene
    for c in [",", ".", "!", "?", ":", ";"]:
        texte = texte.replace(c, " ")
    mots = texte.lower().split()

    #1
    frequences = {}
    for mot in mots:
        if mot in frequences:
            frequences[mot] += 1
        else:
            frequences[mot] = 1
    mots_uniques = set(mots)

    #2
    longueurs = [len(m) for m in mots]
    longueur_moyenne = sum(longueurs) / len(longueurs)

    #3
    max_freq = max(frequences.values())
    min_freq = min(frequences.values())
    mots_plus = [mot for mot, f in frequences.items() if f == max_freq]
    mots_moins = [mot for mot, f in frequences.items() if f == min_freq]

    #4
    palindromes = []
    for mot in mots_uniques:
        if len(mot) > 1 and mot == mot[::-1]:
            palindromes.append(mot)

    print("ANALYSE LEXICALE :")
    print(f"\n1. Fréquence des mots : {frequences}")
    print(f"\n2. Longueur moyenne des mots :, {round(longueur_moyenne, 2)}")
    print(f"\n3. 1/ Mots les plus utilisés :, {mots_plus}")
    print(f"\n   2/Mots les moins utilisés :, {mots_moins}")
    if not palindromes :
        print("\n 4. Pas de palindromes detecte")
    else :
        print(f"\n4. Palindromes détectés : {palindromes}")
    
def analyse_grammaticale(texte):
    separateurs = [".", "!", "?"]
    liste_phrases = []
    phrase = ""

    #1
    for c in texte:
        phrase += c
        if c in separateurs:
            liste_phrases.append(phrase.strip())
            phrase = ""
    if phrase.strip():
        liste_phrases.append(phrase.strip())
    nb_phrases = len(liste_phrases)

    #2
    longueurs_phrases = [len(p.split()) for p in liste_phrases]
    longueur_moyenne = sum(longueurs_phrases) / nb_phrases

    #3
    ponctuation = {".": 0, "!": 0, "?": 0, ",": 0, ";": 0, ":" : 0}
    for c in texte:
        if c in ponctuation:
            ponctuation[c] += 1
    
    #4
    stats_mots = {"noms_propres": 0, "adverbes": 0, "adjectifs": 0, "autres": 0}
    mots = texte.replace(".", "").replace(",", "").split()
    for mot in mots:
        if mot[0].isupper():
            stats_mots["noms_propres"] += 1
        elif mot.endswith("ment"):
            stats_mots["adverbes"] += 1
        elif mot.endswith("e"):
            stats_mots["adjectifs"] += 1
        else:
            stats_mots["autres"] += 1

    print("\nANALYSE GRAMMATICALE :")
    print(f"\n1. Nombre de phrases : {nb_phrases}")
    print(f"\n2. Longueur moyenne des phrases (en mots) : {round(longueur_moyenne, 2)}")
    print(f"\n3. Types de ponctuation utilisés : {ponctuation}")
    print(f"\n4. Statistiques par type de mot : {stats_mots}")

def rapports(texte):
    for c in [",", ";", ":", "(", ")", "\"", "'"]:
        texte = texte.replace(c, "")
    separateurs = [".", "!", "?"]
    phrases = []
    phrase = ""

    for c in texte:
        phrase += c
        if c in separateurs:
            phrases.append(phrase.strip())
            phrase = ""
    if phrase.strip():
        phrases.append(phrase.strip())

    mots = []
    for p in phrases:
        mots += p.lower().replace(".", "").replace("!", "").replace("?", "").split()

    #1
    freqs = {}
    for mot in mots:
        freqs[mot] = freqs.get(mot, 0) + 1
    mots_uniques = set(mots)
    top_10 = sorted(freqs.items(), key=lambda x: x[1], reverse=True)[:10]

    #2
    longueurs = [len(p.split()) for p in phrases]
    max_len = max(longueurs) if longueurs else 0
    phrases_longues = [p for p in phrases if len(p.split()) == max_len]

    #3
    diversite = (len(mots_uniques) / len(mots)) * 100
    
    #4
    patterns = {}
    for i in range(len(mots) - 1):
        paire = mots[i] + " " + mots[i + 1]
        patterns[paire] = patterns.get(paire, 0) + 1
    patterns_repetitifs = [p for p, f in patterns.items() if f > 1]

    print("\nRAPPORTS :")
    print(f"\n1. Top 10 des mots : {top_10}")
    print(f"\n2. Phrases les plus longues : ({max_len} mots) :")
    for p in phrases_longues:
        print("  -", p)
    print(f"\n3. Diversité du vocabulaire : {diversite:.2f}%")
    print("\n4. Patterns répétitifs :", patterns_repetitifs)

# execution test du programme
with open("texte.txt", "r") as f:
    texte = f.read()
    analyse_lexicale(texte)
    analyse_grammaticale(texte)
    rapports(texte)