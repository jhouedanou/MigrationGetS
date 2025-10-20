# Configuration GitHub Actions pour Déploiement FTP Automatique

Ce guide vous explique comment configurer le déploiement automatique de votre site sur OVH via GitHub Actions, **sans exposer vos identifiants** dans le code.

## 🎯 Avantages de cette solution

✅ **Sécurisé** : Les identifiants FTP sont stockés dans GitHub Secrets (chiffrés)
✅ **Automatique** : Déploie automatiquement à chaque push sur la branche `main`
✅ **Traçable** : Historique complet des déploiements dans l'onglet Actions
✅ **Manuel aussi** : Possibilité de déclencher manuellement un déploiement
✅ **Zéro configuration locale** : Pas besoin d'installer git-ftp sur votre machine

---

## 📋 Prérequis

1. Votre projet doit être sur GitHub
2. Vous devez avoir les droits d'administration sur le repository

---

## 🔧 Configuration (Une seule fois)

### Étape 1 : Pousser le workflow sur GitHub

Le fichier `.github/workflows/deploy-ftp.yml` a déjà été créé. Il suffit de le commiter et pusher :

```bash
git add .github/workflows/deploy-ftp.yml
git commit -m "Add GitHub Actions workflow for FTP deployment"
git push origin main
```

### Étape 2 : Configurer les Secrets GitHub

1. **Aller sur votre repository GitHub**
   - Ouvrez `https://github.com/VOTRE_USERNAME/VOTRE_REPO`

2. **Accéder aux Settings**
   - Cliquez sur l'onglet **Settings** (Paramètres)
   - Dans le menu de gauche, cliquez sur **Secrets and variables** → **Actions**

3. **Ajouter les secrets suivants** (cliquez sur "New repository secret" pour chacun) :

   | Nom du secret | Valeur | Description |
   |--------------|--------|-------------|
   | `FTP_HOST` | `ftp.cluster002.hosting.ovh.net` | Serveur FTP OVH |
   | `FTP_USER` | `gets` | Nom d'utilisateur FTP |
   | `FTP_PASSWORD` | `Hs9Txr5H4` | Mot de passe FTP |
   | `FTP_PATH` | `/` | Chemin sur le serveur (généralement `/`) |

   **Capture d'écran du processus :**
   ```
   Settings → Secrets and variables → Actions → New repository secret

   Name:  FTP_HOST
   Secret: ftp.cluster002.hosting.ovh.net
   → Add secret

   (Répéter pour les 4 secrets)
   ```

### Étape 3 : Vérification

Une fois les secrets configurés, vous devriez voir ceci dans Settings → Secrets :

```
Repository secrets (4)
├─ FTP_HOST
├─ FTP_USER
├─ FTP_PASSWORD
└─ FTP_PATH
```

✅ **C'est tout !** Le déploiement automatique est maintenant configuré.

---

## 🚀 Utilisation

### Déploiement Automatique

Chaque fois que vous faites un `git push` sur la branche `main`, le déploiement se lance automatiquement :

```bash
# Workflow habituel
git add .
git commit -m "Mise à jour de la page certificat-centrale"
git push origin main

# ✨ GitHub Actions déploie automatiquement sur OVH !
```

### Déploiement Manuel

Vous pouvez aussi déclencher un déploiement manuellement depuis GitHub :

1. Allez sur votre repository GitHub
2. Cliquez sur l'onglet **Actions**
3. Dans la liste des workflows à gauche, cliquez sur **"Deploy to OVH via FTP"**
4. Cliquez sur **"Run workflow"** (bouton gris à droite)
5. Sélectionnez la branche `main`
6. Cliquez sur **"Run workflow"** (bouton vert)

### Voir l'historique des déploiements

1. Allez sur l'onglet **Actions** de votre repository
2. Vous verrez la liste de tous les déploiements
3. Cliquez sur un déploiement pour voir les logs détaillés

**États possibles :**
- ✅ Vert = Déploiement réussi
- ❌ Rouge = Déploiement échoué (voir les logs)
- 🟡 Jaune = Déploiement en cours
- ⭕ Gris = En attente

---

## 📁 Fichiers exclus du déploiement

Le fichier `.git-ftp-ignore` (déjà créé) exclut automatiquement :

- Fichiers Git (`.git/`, `.gitignore`)
- Fichiers système (`.DS_Store`)
- Fichiers de développement (`.vscode/`, `node_modules/`)
- Scripts de déploiement local
- Documentation de développement

Pour exclure d'autres fichiers, modifiez `.git-ftp-ignore`.

---

## 🔒 Sécurité

### ✅ Bonnes pratiques appliquées

1. **Secrets chiffrés** : GitHub chiffre tous les secrets avec AES-256
2. **Pas de logs** : Les secrets ne sont jamais affichés dans les logs
3. **Accès restreint** : Seuls les admins du repo peuvent voir/modifier les secrets
4. **Pas dans le code** : Les identifiants ne sont jamais dans le code source

### 🔄 Rotation des secrets

Si vous changez votre mot de passe FTP :

1. Allez dans **Settings → Secrets and variables → Actions**
2. Cliquez sur le crayon à côté de `FTP_PASSWORD`
3. Entrez le nouveau mot de passe
4. Cliquez sur **Update secret**

---

## 🐛 Dépannage

### Le déploiement échoue

1. **Vérifier les secrets**
   - Assurez-vous que tous les 4 secrets sont bien configurés
   - Vérifiez qu'il n'y a pas d'espaces avant/après les valeurs

2. **Vérifier les logs**
   - Allez dans Actions → Cliquez sur le déploiement échoué
   - Lisez les logs pour identifier l'erreur

3. **Erreur "fatal: Could not get advertised url"**
   - Le serveur FTP est inaccessible
   - Vérifiez `FTP_HOST` et votre connexion internet

4. **Erreur "Login incorrect"**
   - Le mot de passe est incorrect
   - Vérifiez `FTP_USER` et `FTP_PASSWORD`

### Forcer un déploiement complet

Si vous voulez forcer un upload de tous les fichiers :

1. Allez dans `.github/workflows/deploy-ftp.yml`
2. Ligne 39, remplacez `git ftp push` par `git ftp init --force`
3. Commitez et pushez
4. Remettez `git ftp push` après le déploiement

---

## 📊 Comparaison : Local vs GitHub Actions

| Aspect | Script Local | GitHub Actions |
|--------|-------------|----------------|
| **Sécurité** | ⚠️ Identifiants dans le code | ✅ Secrets chiffrés |
| **Automatisation** | ❌ Manuel | ✅ Automatique |
| **Traçabilité** | ❌ Aucune | ✅ Historique complet |
| **Installation** | ⚠️ Nécessite git-ftp local | ✅ Rien à installer |
| **Équipe** | ❌ Chacun doit configurer | ✅ Une seule config pour tous |

---

## 🎓 Pour aller plus loin

### Déployer uniquement certaines branches

Modifier `.github/workflows/deploy-ftp.yml` ligne 5-6 :

```yaml
on:
  push:
    branches:
      - main
      - production  # Ajouter d'autres branches
```

### Notifications par email

Ajoutez cette étape à la fin du workflow :

```yaml
- name: Send email notification
  if: failure()
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: smtp.gmail.com
    server_port: 465
    username: ${{ secrets.EMAIL_USERNAME }}
    password: ${{ secrets.EMAIL_PASSWORD }}
    subject: Déploiement FTP échoué
    to: votre-email@example.com
    from: GitHub Actions
    body: Le déploiement a échoué. Voir ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}
```

### Déploiement sur plusieurs environnements

Créez plusieurs workflows pour `staging`, `production`, etc.

---

## 📞 Support

- **Documentation GitHub Actions** : https://docs.github.com/actions
- **Documentation git-ftp** : https://github.com/git-ftp/git-ftp
- **Support OVH** : https://www.ovh.com/fr/support/

---

## 🎉 Félicitations !

Votre déploiement automatique est maintenant configuré et sécurisé !

À chaque push, votre site sera automatiquement mis à jour sur OVH, sans que vous ayez à vous soucier du déploiement. 🚀
