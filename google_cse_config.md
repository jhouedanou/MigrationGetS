# Configuration Google Custom Search Engine pour limiter la recherche

## 🔧 Configuration dans Google CSE Console

### 1. Accéder à la console Google CSE
- Allez sur : https://cse.google.com/cse/
- Connectez-vous avec votre compte Google
- Sélectionnez votre moteur de recherche existant

### 2. Configuration des sites à indexer

#### Option A : Limitation par domaine
```
Sites à rechercher :
- https://g-et-s.com/*
- https://jhouedanou.github.io/MigrationGetS/*
```

#### Option B : Exclusion de pages spécifiques
```
Pages à exclure :
- https://g-et-s.com/wp-admin/*
- https://g-et-s.com/wp-includes/*
- https://g-et-s.com/wp-content/plugins/*
```

### 3. Paramètres avancés
```
- Recherche uniquement dans les pages indexées : ✅ Activé
- Inclure les pages liées : ❌ Désactivé
- Recherche dans les images : ❌ Désactivé (si non nécessaire)
```

## 📝 Modification du code HTML

### Option 1 : Ajouter des paramètres de configuration
```html
<script async src="https://cse.google.com/cse.js?cx=5241dfaf922d443f2"></script>
<div class="gcse-search" data-queryParameterName="q" data-siteSearch="https://g-et-s.com" data-siteSearchFilter="i"></div>
```

### Option 2 : Configuration JavaScript avancée
```html
<script>
window.__gcse = {
  parsetags: 'explicit',
  callback: function() {
    var element = google.search.cse.element.getElement('searchresults-only0');
    element.execute('site:g-et-s.com');
  }
};
</script>
<script async src="https://cse.google.com/cse.js?cx=5241dfaf922d443f2"></script>
<div class="gcse-search" data-gname="searchresults-only0"></div>
```

## 🎯 Recommandations

### Pour votre site G-ET-S :
1. **Limiter au domaine principal** : `g-et-s.com`
2. **Exclure les pages d'administration** : `wp-admin/*`
3. **Inclure les sous-domaines** si nécessaire
4. **Configurer les métadonnées** pour une meilleure indexation

### Paramètres recommandés :
- **Sites à rechercher** : `https://g-et-s.com/*`
- **Exclusions** : 
  - `https://g-et-s.com/wp-admin/*`
  - `https://g-et-s.com/wp-includes/*`
  - `https://g-et-s.com/wp-content/plugins/*`
- **Langue** : Français
- **Région** : France
