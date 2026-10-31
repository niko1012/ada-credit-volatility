# Crédit et volatilité des actions américaines

**Nikola Samardzic — Advanced Data Analytics, HEC Lausanne — 2026**

## Question du projet

Le marché du crédit apporte-t-il une information supplémentaire pour prévoir
la volatilité des actions américaines à un mois, au-delà du VIX et de la volatilité passée ?

Ce dépôt prépare la proposition du 9 novembre. Il contient uniquement une première
exploration des données ; aucun modèle prédictif n'est encore entraîné et le projet
n'a pas encore reçu son approbation.

## Démarrer dans GitHub Codespaces

1. Cliquer sur **Code → Codespaces → Create codespace on main**.
2. Attendre la fin de l'installation automatique des bibliothèques et du téléchargement.
3. Ouvrir `notebooks/01_exploration.ipynb`.
4. Si demandé, choisir le noyau **Python 3** / l'environnement Python recommandé.
5. Exécuter les cellules dans l'ordre avec **Shift + Entrée**, ou **Run All**.

Si l'installation automatique n'a pas eu lieu, exécuter dans le terminal :

```bash
python -m pip install -r requirements.txt
python scripts/download_data.py
```

En fin de séance, arrêter l'environnement depuis la page [Codespaces](https://github.com/codespaces),
menu **… → Stop codespace**. Les fichiers conservés dans Codespaces ne sont pas
automatiquement enregistrés dans le dépôt : utiliser un commit puis un push pour les sauvegarder sur GitHub.

## Contenu

- `notebooks/01_exploration.ipynb` : lecture des sources, dates, valeurs manquantes,
  unités et trois graphiques descriptifs.
- `scripts/download_data.py` : téléchargement des trois fichiers officiels.
- `data/README.md` : définitions et provenance des données.
- `docs/proposal.md` : proposition en anglais, brouillon à comprendre et relire avant envoi.
- `docs/preparation.md` : points à comprendre pour présenter le projet.
- `.devcontainer/devcontainer.json` : configuration de Codespaces.

Les données téléchargées restent dans `data/raw/`, hors Git. Le script conserve
les fichiers existants et inscrit les dates de téléchargement et empreintes SHA-256
dans `data/raw/download_manifest.json`. Les sources peuvent réviser leur historique :
conserver ces fichiers pour retrouver la même version des données.

## Comparaison envisagée après validation

La cible sera la volatilité réalisée pendant le mois suivant. Nous comparerons :

1. la volatilité passée seule ;
2. la volatilité passée et le VIX ;
3. les mêmes informations et un indicateur de crédit, l'Excess Bond Premium.

Méthodes proposées : régression linéaire, puis petit réseau de neurones dense.
L'évaluation sera chronologique, avec MAE et RMSE sur les mêmes mois.
Les détails seront fixés avant l'entraînement. Une absence de gain du crédit est
une réponse possible à la question.

## Limites déjà identifiées

- Les données French représentent un marché américain large, pas le S&P 500.
  Le VIX est lié aux options sur le S&P 500 : cette différence doit être explicitée.
- L'EBP est une estimation mensuelle publiée avec retard et susceptible de révision.
  Un décalage ne transforme pas l'historique actuel en données réellement disponibles
  à chaque date passée. L'exercice restera une évaluation sur historique révisé.
- Le notebook actuel décrit les données. Il n'est ni une prévision, ni une preuve
  d'un lien causal, ni un résultat de comparaison des modèles.

## Outils et assistance

La structure initiale, la configuration Codespaces, le script de téléchargement,
le notebook d'exploration et le brouillon de proposition ont été préparés avec
l'aide de Codex (OpenAI). Ils doivent être relus, exécutés et compris par l'auteur.
Les usages ultérieurs seront consignés dans `docs/ai-use.md`.
Les données restent la propriété de leurs fournisseurs ; aucune licence sur ces
données n'est accordée par ce dépôt.
