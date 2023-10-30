import configparser
import os
import shutil

def getPath(appExt,extension):
    path=""
    for fileType in appExt:
        if extension in fileType[1].split(","):
            path=fileType[0]
    return path

def main():

    config = configparser.ConfigParser()
    config.read(r"config.ini")
    dest_folder="D:\\main"
    
    chemins=config.get("Chemins","links").split(";")
    appExt=config.items("Extentions")


    for chemin in chemins:
        fichiers = os.listdir(chemin)
        for fichierPath in fichiers:
            extension = os.path.splitext(fichierPath)[1].replace(".","")
            folder=getPath(appExt,extension)
            if folder!="":
                fichier=os.path.join(chemin,fichierPath)
                dossier_destination=os.path.join(dest_folder,folder)
                print(fichier)
                print(dossier_destination)
                shutil.move(fichier, dossier_destination)

if __name__ == "__main__":
    main()
