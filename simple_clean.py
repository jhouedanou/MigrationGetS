#!/usr/bin/env python3
import os
import re

def simple_clean_html(content):
    """Nettoyage simple du HTML avec des regex"""
    
    # Supprimer les divs Elementor avec leurs attributs
    content = re.sub(r'<div[^>]*class="[^"]*elementor[^"]*"[^>]*>', '', content)
    content = re.sub(r'<div[^>]*data-[^>]*elementor[^>]*>', '', content)
    
    # Supprimer les divs vides
    content = re.sub(r'<div[^>]*>\s*</div>', '', content)
    content = re.sub(r'<div[^>]*>\s*<div[^>]*>\s*</div>\s*</div>', '', content)
    
    # Supprimer les sections vides
    content = re.sub(r'<section[^>]*>\s*</section>', '', content)
    
    # Supprimer les attributs data-*
    content = re.sub(r'\s+data-[^=]*="[^"]*"', '', content)
    
    # Nettoyer les espaces multiples
    content = re.sub(r'\s+', ' ', content)
    
    # Nettoyer les lignes vides multiples
    content = re.sub(r'\n\s*\n', '\n', content)
    
    return content

def clean_file_simple(file_path):
    """Nettoie un fichier HTML avec la méthode simple"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"🧹 Nettoyage simple de {file_path}...")
        
        # Nettoyer le contenu
        cleaned_content = simple_clean_html(content)
        
        # Écrire le fichier nettoyé
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        print(f"✅ {file_path} nettoyé")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du nettoyage de {file_path}: {e}")
        return False

def main():
    """Fonction principale"""
    print("🧹 Nettoyage simple du HTML...")
    print("=" * 50)
    
    # Trouver tous les fichiers HTML à la racine
    html_files = []
    for file in os.listdir('.'):
        if file.endswith('.html') and file != 'index-backup.html':
            html_files.append(file)
    
    print(f"📄 Trouvé {len(html_files)} fichiers HTML à nettoyer")
    
    cleaned_files = 0
    
    for html_file in html_files:
        if clean_file_simple(html_file):
            cleaned_files += 1
    
    print(f"\n✅ {cleaned_files} fichiers nettoyés")
    print("🎯 Le code HTML a été simplifié!")

if __name__ == "__main__":
    main()

