import os

# Fichiers test
bash_aliases_path = "/home/erann/Documents/programmation/add-alias/.test-bashrc"
text = "/home/erann/Documents/programmation/add-alias/test.txt"

# vrai fichiers
tmp_file = "/home/erann/Documents/programmation/add-alias/.tmp_file"
# bash_aliases_path = "/home/erann/.bash_aliases"
# text = "/home/erann/Documents/programmation/add-alias/alias.txt"


print(r"""
+================================================================================================+
|                   _   _                   _                                    _ _             |
|                  | | (_)                 | |                                  | (_)            |
|    __ _  ___  ___| |_ _  ___  _ __     __| | ___   _ __ ___   ___  ___    __ _| |_  __ _ ___   |
|   / _` |/ _ \/ __| __| |/ _ \| '_ \   / _` |/ _ \ | '_ ` _ \ / _ \/ __|  / _` | | |/ _` / __|  |
|  | (_| |  __/\__ \ |_| | (_) | | | | | (_| |  __/ | | | | | |  __/\__ \ | (_| | | | (_| \__ \  |
|   \__, |\___||___/\__|_|\___/|_| |_|  \__,_|\___| |_| |_| |_|\___||___/  \__,_|_|_|\__,_|___/  |
|    __/ |                                                                                       |
|   |___/                                                                             By Erann   |
|                                                                                                |
+================================================================================================+
|                                                                                                |
|  Ajouter, modifier ou supprimer un élément:                                                    |
|                                                                                                |
|  - a: Ajouter                                                                                  |
|  - S: Supprimer                                                                                |
|  - m: Modifier                                                                                 |
|                                                                                                |
+================================================================================================+
""")
action = input("--> ")

if action == "a":
    user_alias_name = input("Nom de l'alias: ")
    user_alias_command = input("Commande de l'alias: ")
    user_alias_description = input("Description de l'alias: ")

    with open(bash_aliases_path, "a") as bashrc_file:
        bashrc_file.write("\nalias " + user_alias_name + "='" + user_alias_command + "'")

    with open(text, "a") as txt_file:
        txt_file.write("\n+ " + user_alias_name + " => " + user_alias_description + "\n")

    print("Alias ajouter !")

elif action == "s":
    with open(text, "r+") as txt_file:
        print(txt_file.read())

    del_item = input("\nElement à supprimer (ecrire le nom de l'alias): ")
   
    with open(bash_aliases_path, "r+") as bashrc_file:
        with open(tmp_file, "w+") as temporary_file:
            for line in bashrc_file:
                if del_item not in line.strip("\n"):
                    temporary_file.write(line)

    os.replace(tmp_file, bash_aliases_path)

    with open(text, "r+") as bashrc_file:
        with open(tmp_file, "w+") as temporary_file:
            for line in bashrc_file:
                if del_item not in line.strip("\n"):
                    temporary_file.write(line)

    os.replace(tmp_file, text)

    print("Alias '" + del_item + "' supprimer.")

elif action == "m":
    print("modifier")
    
else:
    print("Tu t'es planter mec !!!")