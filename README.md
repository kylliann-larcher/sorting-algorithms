# Sorting Algorithms Visualizer 🧠🎨

Ce projet Python permet de **visualiser étape par étape différents algorithmes de tri** à l'aide de **Pygame**.  
Tu peux choisir l'algorithme, le nombre d'éléments à trier, et voir en temps réel comment les données sont triées, avec des animations claires et une interface intuitive.

---

## 🚀 Fonctionnalités

- Menu interactif pour choisir :
  - l'**algorithme** de tri
  - le **nombre d'éléments**
- Visualisation graphique dynamique avec :
  - Barres verticales animées
  - Couleurs d'action (comparaison, trié)
  - **Chronomètre** précis
  - **Règle graduée centrale**
  - **Message de fin animé + son de confirmation**
- Possibilité de :
  - Recommencer le tri
  - Revenir au menu

---

## 📦 Algorithmes disponibles

- 🔁 Tri à bulle (Bubble Sort)
- 🪜 Insertion Sort
- 🔍 Selection Sort
- 🏗 Heap Sort
- 🧬 Merge Sort
- 🦷 Comb Sort (Tri à peigne)

---

## 📁 Arborescence

```
sorting-algorithms/
├── assets/
│   └── done.wav               # Son de confirmation
├── src/
│   ├── main.py                # Lancement de l'app
│   ├── menu.py                # Menu de sélection interactif
│   ├── display_tri.py         # Interface graphique Pygame
│   ├── animator.py            # Animation des algorithmes (step by step)
│   └── sorting.py             # Implémentations brutes des algos
```

---

## ▶️ Utilisation

### 1. Installe les dépendances

```bash
pip install pygame
```

### 2. Lance le programme

Depuis le dossier racine :

```bash
python src/main.py
```

---

## 🛠 Technologies utilisées

- Python 3
- Pygame

---

## 🙋‍♂️ Auteur

**Kylliann LARCHER**,  
Alexandre Chevalier,
Perla Assuied

Projet développé dans le cadre de ma spécialisation en intelligence artificielle chez La Plateforme.

---

## 🧠 Idées futures

- Ajout d'une interface HTML (web visualizer)
- Plus d'algorithmes : Radix, Shell, Cocktail...
- Personnalisation des couleurs
- Export vidéo du tri

---

## 📜 Licence

Ce projet est open-source sous licence MIT.
