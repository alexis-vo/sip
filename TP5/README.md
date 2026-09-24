# Gestionnaire de Mots de Passe (Pykey) - TP5

Mini-projet réalisé dans le cadre du module **1CC1000 - Systèmes d'Information et Programmation (CentraleSupélec)**. Il s'agit d'un gestionnaire de mots de passe en ligne de commande sécurisé.

## Fonctionnalités

* **Génération de mots de passe forts** : Respect des critères de robustesse (minuscules, majuscules, chiffres, caractères spéciaux).
* **Chiffrement symétrique** : Utilisation de l'algorithme **AES (Fernet)** de la bibliothèque `cryptography` pour protéger le stockage des données.
* **Dérivation de clé (KDF)** : Utilisation de **PBKDF2HMAC** (avec SHA-256 et un sel) pour générer une clé de chiffrement robuste à partir d'un mot de passe maître.
* **Gestion des erreurs** : Capture des exceptions (ex: `InvalidToken`) en cas de saisie d'un mauvais mot de passe maître.

## Prérequis

Assurez-vous d'avoir installé la bibliothèque `cryptography` :
```bash
python -m pip install cryptography
