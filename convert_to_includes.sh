#!/bin/bash

# Script pour convertir tous les fichiers index.html des sous-dossiers au système d'includes

echo "Conversion des fichiers index.html au système d'includes..."

# Liste des fichiers index.html dans les sous-dossiers
FILES=$(find . -name "index.html" -not -path "./index.html")

for file in $FILES; do
    echo "Traitement de $file..."
    
    # Créer un fichier temporaire
    TEMP_FILE="/tmp/$(basename "$file")_temp.html"
    
    # Étape 1: Ajouter jQuery et includes.js avant </head>
    sed 's|</head>|	<!-- jQuery for includes -->\
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>\
	<!-- Custom includes script -->\
	<script src="../js/includes.js"></script>\
	</head>|g' "$file" > "$TEMP_FILE"
    
    # Étape 2: Ajouter les placeholders après <body>
    sed 's|<body\([^>]*\)>|<body\1>\
	<!-- Header include -->\
	<div id="header-placeholder"></div>\
	<!-- Navigation include -->\
	<div id="nav-placeholder"></div>|g' "$TEMP_FILE" > "${TEMP_FILE}.step2"
    
    # Étape 3: Supprimer tout à partir de <div class="site-footer"> et ajouter le footer placeholder
    awk '/<div class="site-footer">/ {print "\n<!-- Footer include -->"; print "<div id=\"footer-placeholder\"></div>"; print "\n</body>"; print "</html>"; exit} {print}' "${TEMP_FILE}.step2" > "${TEMP_FILE}.final"
    
    # Remplacer le fichier original
    mv "${TEMP_FILE}.final" "$file"
    
    # Nettoyer les fichiers temporaires
    rm -f "$TEMP_FILE" "${TEMP_FILE}.step2"
    
    echo "✓ $file converti"
done

echo "Conversion terminée pour tous les fichiers !"