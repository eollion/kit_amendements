#!/usr/bin/env python3
"""
Parcourt récursivement un dossier contenant des fichiers XML d'amendements
(Assemblée nationale) et extrait les informations clés dans un fichier CSV.
Aucune dépendance externe requise (uniquement la bibliothèque standard Python).

Usage :
    python extraire_amendements.py <dossier_racine> [fichier_sortie_sans_extension]

Exemple :
    python extraire_amendements.py ./DLR5L17N54308 amendements
"""

import csv
import re
import sys
import html
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {"a": "http://schemas.assemblee-nationale.fr/referentiel"}

CHAMPS = [
    "fichier", "erreur", "uid", "legislature", "numero", "texte_legislatif_ref",
    "auteur_type", "auteur_acteur_ref", "auteur_groupe_politique_ref",
    "nb_cosignataires", "libelle_signataires", "division_titre",
    "division_designation", "article_additionnel", "date_depot",
    "date_publication", "soumis_article_40", "etat_code", "etat_libelle",
    "sort", "date_sort", "code_loi", "division_code_loi", "dispositif",
    "expose_sommaire",
]


def texte(elem, chemin, defaut=None):
    """Récupère le texte d'un sous-élément (avec namespace), ou une valeur par défaut."""
    if elem is None:
        return defaut
    trouve = elem.find(chemin, NS)
    if trouve is None or trouve.text is None:
        return defaut
    return trouve.text.strip()


def nettoyer_html(texte_brut):
    """Supprime les balises HTML et décode les entités (&#x2013; etc.) d'un champ texte."""
    if not texte_brut:
        return ""
    sans_balises = re.sub(r"<[^>]+>", " ", texte_brut)
    decode = html.unescape(sans_balises)
    return re.sub(r"\s+", " ", decode).strip()


def extraire_un_fichier(chemin_fichier: Path) -> dict:
    """Extrait les champs clés d'un fichier XML d'amendement."""
    try:
        arbre = ET.parse(chemin_fichier)
    except ET.ParseError as e:
        return {"fichier": str(chemin_fichier), "erreur": f"XML invalide : {e}"}

    racine = arbre.getroot()

    auteur = racine.find("a:signataires/a:auteur", NS)
    cosignataires = racine.findall("a:signataires/a:cosignataires/a:acteurRef", NS)
    division = racine.find("a:pointeurFragmentTexte/a:division", NS)
    cycle = racine.find("a:cycleDeVie", NS)
    etat = racine.find("a:cycleDeVie/a:etatDesTraitements/a:etat", NS)
    loi = racine.find("a:loiReference", NS)
    corps_auteur = racine.find("a:corps/a:contenuAuteur", NS)

    return {
        "fichier": str(chemin_fichier),
        "uid": texte(racine, "a:uid"),
        "legislature": texte(racine, "a:legislature"),
        "numero": texte(racine, "a:identification/a:numeroLong"),
        "texte_legislatif_ref": texte(racine, "a:texteLegislatifRef"),
        "auteur_type": texte(auteur, "a:typeAuteur"),
        "auteur_acteur_ref": texte(auteur, "a:acteurRef"),
        "auteur_groupe_politique_ref": texte(auteur, "a:groupePolitiqueRef"),
        "nb_cosignataires": len(cosignataires),
        "libelle_signataires": nettoyer_html(texte(racine, "a:signataires/a:libelle")),
        "division_titre": texte(division, "a:titre"),
        "division_designation": texte(division, "a:articleDesignation"),
        "article_additionnel": texte(division, "a:articleAdditionnel"),
        "date_depot": texte(cycle, "a:dateDepot"),
        "date_publication": texte(cycle, "a:datePublication"),
        "soumis_article_40": texte(cycle, "a:soumisArticle40"),
        "etat_code": texte(etat, "a:code"),
        "etat_libelle": texte(etat, "a:libelle"),
        "sort": texte(cycle, "a:sort"),
        "date_sort": texte(cycle, "a:dateSort"),
        "code_loi": texte(loi, "a:codeLoi"),
        "division_code_loi": texte(loi, "a:divisionCodeLoi"),
        "dispositif": nettoyer_html(texte(corps_auteur, "a:dispositif")),
        "expose_sommaire": nettoyer_html(texte(corps_auteur, "a:exposeSommaire")),
    }


def extraire_dossier(dossier_racine: str) -> list[dict]:
    dossier_racine = Path(dossier_racine)
    fichiers_xml = sorted(dossier_racine.rglob("*.xml"))

    if not fichiers_xml:
        print(f"Aucun fichier .xml trouvé sous {dossier_racine}")
        return []

    print(f"{len(fichiers_xml)} fichier(s) XML trouvé(s). Extraction en cours...")

    return [extraire_un_fichier(f) for f in fichiers_xml]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python extraire_amendements.py <dossier_racine> [nom_sortie]")
        sys.exit(1)

    dossier = sys.argv[1]
    nom_sortie = sys.argv[2] if len(sys.argv) > 2 else "amendements"

    lignes = extraire_dossier(dossier)

    if lignes:
        chemin_csv = f"{nom_sortie}.csv"
        with open(chemin_csv, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=CHAMPS, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(lignes)
        print(f"Terminé : {chemin_csv} généré ({len(lignes)} lignes).")