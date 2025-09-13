#!/bin/bash

# Script pour corriger tous les liens http://gets.local dans les fichiers HTML

echo "Correction des liens http://gets.local..."

# Liste des fichiers contenant des liens à corriger
FILES=$(find . -name "*.html" -exec grep -l "http://gets\.local" {} \;)

for file in $FILES; do
    echo "Traitement de $file..."
    
    # Remplacements courants
    sed -i '' 's|http://gets\.local/home/|../home/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/|../index.html|g' "$file"
    sed -i '' 's|http://gets\.local/mentions-legales-confidentialite/|../mentions-legales-confidentialite/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/plan-du-site/|../plan-du-site/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/contact/|../contact/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/missions/|../missions/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/gouvernance-advisors/|../gouvernance-advisors/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/bibliographie-corporate-governance/|../bibliographie-corporate-governance/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/sites-interesssants/|../sites-interesssants-4/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/candidats-mendataires-administratrices-administrateurs/|../candidats-mandataires-administratrices-administrateurs-7/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/la-presse-parle-de-gouvernance-structures/|../la-presse-parle-de-gouvernance-structures/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/troiminaires-interactifs-journee-proposes-dans-le-passe/|../troiminaires-interactifs-journee-proposes-dans-le-passe/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/atelier-utilisation-de-linformatique-en-liaison-avec-internet/|../atelier-utilisation-de-linformatique-en-liaison-avec-internet/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/exposes-articles-et-notes-publies-par-g-s/|../exposes-articles-et-notes-publies-par-g-s/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/formulaire-pour-candidats/|../formulaire-pour-candidats/index.html|g' "$file"
    
    # Correction des sous-pages missions
    sed -i '' 's|http://gets\.local/missions/evaluation-diagnostic-dun-conseil-dadministration-ou-de-surveilance/|../missions/evaluation-diagnostic-dun-conseil-dadministration-ou-de-surveilance/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/missions/recherche-de-mandataires-sociaux/|../missions/recherche-de-mandataires-sociaux/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/missions/enquetes-et-etudes/|../missions/enquetes-et-etudes/index.html|g' "$file"
    sed -i '' 's|http://gets\.local/missions/les-administrateurs-et-lomnipresence-du-numerique/|../missions/les-administrateurs-et-lomnipresence-du-numerique/index.html|g' "$file"
    
    # Correction des ressources
    sed -i '' 's|http://gets\.local/wp-content/uploads/|../wp-content/uploads/|g' "$file"
    sed -i '' 's|http://gets\.local/images/|../images/|g' "$file"
    sed -i '' 's|http://gets\.local/docdech/|../docdech/|g' "$file"
    
    # Correction des emails
    sed -i '' 's|info@gets\.local|info@g-et-s.com|g' "$file"
    sed -i '' 's|contact@gets\.local|contact@g-et-s.com|g' "$file"
    sed -i '' 's|webmaster@gets\.local|webmaster@g-et-s.com|g' "$file"
    
    echo "✓ $file traité"
done

echo "Correction terminée pour tous les fichiers !"