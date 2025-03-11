import os
import shutil

def organiser_dossier(chemin_dossier):
    if not os.path.exists(chemin_dossier):
        print("Le dossier spécifié n'existe pas.")
        return
    
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
        "Vidéos": [".mp4", ".avi", ".mkv", ".mov"],
        "Musique": [".mp3", " .wav", ".flac"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"]
    }
    
    dossiers_cibles = list(categories.keys()) + ["Autres"]
    for dossier in dossiers_cibles:
        chemin_categorie = os.path.join(chemin_dossier, dossier)
        if not os.path.exists(chemin_categorie):
            os.makedirs(chemin_categorie)
    
    for fichier in os.listdir(chemin_dossier):
        chemin_fichier = os.path.join(chemin_dossier, fichier)
        
        if fichier in dossiers_cibles:
            continue
        
        if os.path.isfile(chemin_fichier) or os.path.isdir(chemin_fichier):
            extension = os.path.splitext(fichier)[1].lower()
            
            destination = "Autres"
            for categorie, extensions in categories.items():
                if extension in extensions:
                    destination = categorie
                    break
            
            shutil.move(chemin_fichier, os.path.join(chemin_dossier, destination, fichier))
    
    print("Organisation terminée !")

chemin = input("Entrez le chemin du dossier à organiser : ")
organiser_dossier(chemin)