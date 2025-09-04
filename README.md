# Ecommerce Analytics Project

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-Yes-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)


## 📖 Description

Ce projet vise à collecter, nettoyer, enrichir et agréger des données issues d’un site e-commerce et de points de vente physiques afin de générer des indicateurs clés (KPI) quotidiens et mensuels.

**Workflow :**

1. Extraction (Google Drive + SQLite)
2. Nettoyage (doublons, valeurs manquantes)
3. Enrichissement (calcul du chiffre d’affaires)
4. Agrégation (KPI par jour et par mois)


## 🗂️ Structure du projet

```bash
commerce-analytics/
├── data/
│   ├── raw_data/         # Données brutes
│   ├── cleaned_data/     # Données nettoyées
│   ├── enriched_data/    # Données enrichies
│   └── aggregated_data/  # Données agrégées
├── dags/common/
│   ├── extract.py
│   ├── transform.py
│   ├── enrich.py
│   └── aggregate.py
├── requirements.txt
└── README.md
```


## ⚙️ Installation

1. Cloner le projet :

```bash
git clone <URL_DU_PROJET>
cd ecommerce-analytics
```

2. Créer et activer un environnement virtuel :

```bash
python -m venv dahvenv
source dahvenv/bin/activate   # Linux/Mac
dahvenv\Scripts\activate      # Windows
```

3. Installer les dépendances :

```bash
pip install -r requirements.txt
```

4. Ajouter le fichier Service Account JSON dans `dags/common/`.


## 🚀 Exécution

1️⃣ Extraction :

```bash
cd dags/common
python extract.py
```

2️⃣ Nettoyage :

```bash
python transform.py
```

3️⃣ Enrichissement :

```bash
python enrich.py
```

4️⃣ Agrégation :

```bash
python aggregate.py
```


## 📊 KPI générés

| Type               | Source                 | Indicateur         | Périodicité |
| ------------------ | ---------------------- | ------------------ | ----------- |
| Clients            | cleaned\_data/clients  | Clients uniques    | Quotidien   |
| Stock              | cleaned\_data/products | Stock disponible   | Quotidien   |
| Chiffre d’affaires | enriched\_data/orders  | Somme du `revenue` | Mensuel     |


## 🛠️ Dépendances

* Python 3.11
* pandas
* google-api-python-client
* google-auth
* sqlite3 (standard)
* pathlib (standard)


## 🔑 Bonnes pratiques

* Respecter la structure `année/mois/jour` pour tous les fichiers.
* Vérifier la présence du fichier Service Account JSON avant exécution.
* Exécuter les scripts dans l’ordre :
  `extract.py → transform.py → enrich.py → aggregate.py`.
