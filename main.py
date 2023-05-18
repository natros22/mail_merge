with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for i in names:
        name = i.strip()
        with open("./Input/Letters/starting_letter.txt") as txt:
            contents = txt.read()
            x = contents.replace("{name}", name)
        with open(f"./Output/ReadyToSend/{name}", mode="w") as letter:
            letter.write(x)
