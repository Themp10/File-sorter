import configparser
import os
import shutil

def main():
    # Open the configuration file
    config = configparser.ConfigParser()
    config.read(r"config.ini")
   
    # Get the list of paths
    # chemins = config["chemins"]
    
    paths=config.get("chemins","links").split(";")
    details_dict = config.items('extentions')[0][0].split(",")
    print(details_dict)
    # # Get the dictionary of extensions
    # dossiers_destination = {}
    # for extension, dossier in config["extentions"].items():
    #     extension = extension.strip()
    #     dossier = dossier.strip()
    #     dossiers_destination[extension] = dossier

    # # Iterate over the paths
    # for chemin in chemins:
    #     # List the files in the directory
    #     fichiers = os.listdir(chemin)
    #     print(os.path.join(chemin, fichier))

    #     # Iterate over the files
    #     for fichier in fichiers:
    #         # Get the extension of the file
    #         extension = os.path.splitext(fichier)[1]
    #         extension = extension.strip()

    #         # Get the destination directory for the file
    #         dossier_destination = dossiers_destination.get(extension)
    #         print(dossier_destination)

    #         # Move the file to the destination directory
    #         # shutil.move(os.path.join(chemin, fichier), dossier_destination)

if __name__ == "__main__":
    main()
