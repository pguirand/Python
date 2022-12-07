
def extraire_extension(nom_fichier):
    fichier_split = nom_fichier.split(".")
    # print(fichier_split)
    if len(fichier_split) > 1:
        return fichier_split[-1]
    return None


def get_ext_definition(extension, definition):
    for d in definition:
        if d[0].lower() == extension.lower():
            return d[1]
    return None
    





fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document Word"),
                        ("exe", "Executable"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))

"""definition_extensions_dict = {"doc": "Document Word",
                        "exe": "Executable",
                        "txt": "Document Texte",
                        "jpeg": "Image JPEG"}"""

a = "test.doc"

for fichier in fichiers:
    ext = extraire_extension(fichier)
    if ext:
        definition = get_ext_definition(ext, definition_extensions)
        if not definition:
            definition = "Extension non connue"
    else:
        definition = "Aucune extension"
    print(fichier, "("+ definition + ")")


#s = a[::-1] remember the reverse
#a_split = a.split(".")

# print(a_split)
# if len(a_split) > 1:
#     exten = a_split[-1]
#     print(exten)
# else:
#     print("pas d'extension")

# print(extraire_extension(a))
