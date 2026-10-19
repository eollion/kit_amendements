# Kit amendements

Ce repository contient toutes les ressources attachées au use case "Amendements" du logiciel ActiveTigger.

L'objectif de ce use case est de prendre en main le logiciel ActiveTigger à partir d’une étude de cas simple : détecter automatiquement les amendements dits “sourcés” au sein d’un corpus d’amendements déposés par les parlementaires de l’Assemblée Nationale entre 2024 et 2026.

Plus précisément, vous trouverez dans ce repository les fichiers et dossiers suivants : 

## Presentation
Le fichier **presentation.md** présente l'entièreté du déroulé du cas, de l'introduction des données et de la question de recherche à l'entraînement des modèles et la discussion des résultats. 

## Slides
Le dossier **slides** contient des slides reprenant le contenu de presentation.md sous forme de slides en différents formats (PDF, pptx) et modalités (court, long), ainsi qu'un dossier contenant les images utilisées dans la présentation.

## Codebook
Le fichier **codebook.md** contient le codebook final élaboré par itérations successives. 

## Source 
Le dossier **source** contient les différents notebooks et scripts qui ont permis 1) la préparation des données pour obtenir un dataset prêt à utilisation sur ActiveTigger et 2) le processing des prédictions pour dégager des réponses à nos questions de recherche. 

## Data
Les données du projet sont disponibles sur Zenodo à l'URL suivante : https://doi.org/10.5281/zenodo.23474882. Elles peuvent être téléchargées puis décompressées pour être utilisées.   
- Le jeu de données **clean_dataset_annotated.csv** est celui que l'on importe dans ActiveTigger pour créer notre classification automatique. Les utilisateurs et utilisatrices de ce tutoriel peuvent choisir d'importer les annotations existantes ou de les ignorer.
- Les autres fichiers, contenus dans le dossier **data**, permettent d'exécuter le notebook présentant les résultats (results.ipynb). Pour cela, le notebook et le dossier data doivent simplement se trouver dans le même dossier.