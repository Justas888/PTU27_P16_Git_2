while True:
    print("kartojimo")
    print("1. išeiti iš kartojimo bloko\n"
          "2. vėl parodyti meniu(praleidžiam 1-ą kartojimą)")

    pasirinkimas = input()

    if pasirinkimas == "2":
        continue

    elif pasirinkimas == "0":
        break
    print(f"Jūs įvedėte {pasirinkimas}")
    print("kartojimo bloko pabaiga")
print("programos pabaiga")