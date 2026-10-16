#!/usr/bin/env python3
"""
Extrait le(s) fichier(s) XML contenu(s) dans une archive .zip déjà présente sur le disque,
et les enregistre dans le même dossier que le zip.
"""

import zipfile
import sys
from pathlib import Path


def extraire_xml(chemin_zip: str) -> list[str]:
    """
    Extrait les fichiers XML d'une archive zip locale, dans le même dossier que le zip.

    Args:
        chemin_zip: Chemin vers le fichier .zip (ex: "fichier.xml.zip").

    Returns:
        Liste des chemins des fichiers XML extraits.
    """
    chemin_zip = Path(chemin_zip)

    if not chemin_zip.exists():
        raise FileNotFoundError(f"Fichier introuvable : {chemin_zip}")

    dossier_sortie = chemin_zip.parent  # même dossier que le zip
    fichiers_xml_extraits = []

    with zipfile.ZipFile(chemin_zip) as archive:
        noms_fichiers = archive.namelist()
        print(f"Contenu de l'archive : {noms_fichiers}")

        for nom in noms_fichiers:
            if nom.lower().endswith(".xml"):
                archive.extract(nom, path=dossier_sortie)
                chemin_extrait = dossier_sortie / nom
                fichiers_xml_extraits.append(str(chemin_extrait))
                print(f"Fichier XML extrait : {chemin_extrait}")

    if not fichiers_xml_extraits:
        print("Aucun fichier XML trouvé dans l'archive.")

    return fichiers_xml_extraits


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python extraire_xml.py <chemin_du_fichier_zip>")
        sys.exit(1)

    chemin_zip = sys.argv[1]
    extraire_xml(chemin_zip)