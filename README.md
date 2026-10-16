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

## Pre-processing 
Le dossier **preprocessing** contient le code et les explications des différentes étapes de préparation des données qui ont permis d'obtenir un dataset propre pour notre cas à partir de données désagrégées disponibles en ligne. 

## Data
Les données du projet sont disponibles sur Zenodo à l'URL suivante : [INSERT URL]. 
En important le fichier clean_dataset_annotated.csv dans ActiveTigger, les utilisateurs peuvent choisir d'importer les annotations existantes ou de les ignorer.   
 
## Results
Le fichier **results.ipynb** présente le processing des prédictions, en particulier la création des graphiques sur les variables concernées par nos questions de recherche. 

