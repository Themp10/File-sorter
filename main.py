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
    copiedFiles=0
    config = configparser.ConfigParser()
    config.read(r"config.ini")
    dest_folder=config.get("Chemins","destination")
    chemins=config.get("Chemins","searchpaths").split(",")
    appExt=config.items("Extentions")
    newLine="========================================================"

    with open('log.txt', 'a') as fd:
        fd.write(f'\n{newLine}')

    for chemin in chemins:
        fichiers = os.listdir(chemin)
        for fichierPath in fichiers:
            extension = os.path.splitext(fichierPath)[1].replace(".","")
            folder=getPath(appExt,extension)
            if folder!="":
                fichier=os.path.join(chemin,fichierPath)
                dossier_destination=os.path.join(dest_folder,folder)
                try:
                    shutil.move(fichier, dossier_destination)
                    copiedFiles+=1
                    logLine=str(copiedFiles) + " : Moved file : " + fichier + " ===> " + dossier_destination                   
                except  Exception as e:
                    logLine=e 

                with open('log.txt', 'a') as fd:
                    fd.write(f'\n{logLine}')
    if copiedFiles==0:
        newLine="No file copied"
        with open('log.txt', 'a') as fd:
            fd.write(f'\n{newLine}')

if __name__ == "__main__":
    main()
