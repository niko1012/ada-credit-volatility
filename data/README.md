# Sources des données

Le script `python scripts/download_data.py` obtient les fichiers ci-dessous sans
compte ni clé API. Ils ne sont pas redistribués dans ce dépôt.

| Fichier local | Source | Fréquence | Utilisation |
|---|---|---|---|
| `raw/ebp.csv` | Federal Reserve Board | Mensuelle | Colonne `ebp` : indicateur de crédit |
| `raw/vix.csv` | Cboe | Quotidienne | Colonne `CLOSE` : VIX en clôture |
| `raw/ff_daily.zip` | Kenneth French Data Library | Quotidienne | `Mkt-RF` et `RF` : rendement du marché américain |

## Définitions et accès officiels

- Fed : [note de présentation](https://www.federalreserve.gov/econres/notes/feds-notes/updating-the-recession-risk-and-the-excess-bond-premium-20161006.html),
  [CSV](https://www.federalreserve.gov/econres/notes/feds-notes/ebp_csv.csv).
  L'EBP est exprimé en points de pourcentage. Il peut être négatif ; ce n'est
  pas une probabilité. La date désigne le mois de référence, pas la publication.
  Les autres colonnes ne sont pas ajoutées au modèle prévu.
- Cboe : [historique VIX](https://www.cboe.com/tradable-products/vix/vix-historical-data),
  [CSV](https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv).
  Un niveau de 20 correspond à une volatilité implicite annualisée de 20 %,
  liée à un horizon d'environ 30 jours sur le S&P 500.
- French : [définitions](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_factors.html),
  [ZIP quotidien](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip).
  Les rendements sont en pourcentage. Le rendement total utilisé est
  `(Mkt-RF + RF) / 100`. Ce marché large n'est pas le S&P 500.
  Le fichier comporte un préambule et un pied de page ; le notebook isole
  uniquement les lignes dont la première colonne est une date à huit chiffres.

## Période et conventions

La période envisagée est janvier 1990–décembre 2025, afin de travailler sur des
années complètes communes aux sources. Les lignes plus récentes téléchargées sont
conservées dans les fichiers bruts, mais exclues des graphiques de préparation.
Le notebook vérifie la couverture et les valeurs manquantes avant les graphiques.

Une première série descriptive de volatilité mensuelle est calculée comme
l'écart-type échantillonnal (`ddof=1`) des rendements quotidiens d'un mois,
multiplié par `sqrt(252)`, puis par 100 pour l'afficher en pourcentage annualisé.
Les mois ne sont pas des périodes de 21 jours glissants. Aucun décalage de
prévision ni alignement de disponibilité de l'EBP n'est appliqué à ce stade.

Les fichiers officiels peuvent changer. `raw/download_manifest.json` conserve
l'URL, la date de téléchargement et l'empreinte de chaque copie locale.
Une date inconnue reste vide si des fichiers ont été copiés manuellement.
Conserver la copie utilisée pour le projet. Le retard de publication et les
révisions de l'EBP devront être traités dans la construction des variables,
avant tout entraînement.
