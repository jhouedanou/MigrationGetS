#!/usr/bin/env python3
import os
import re
from bs4 import BeautifulSoup

def aggressive_clean_html(html_content):
    """Nettoyage agressif du HTML - suppression de tous les divs inutiles"""
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Supprimer tous les divs vides de manière agressive
    def remove_empty_divs_aggressive():
        """Supprime tous les divs vides de manière agressive"""
        while True:
            divs = soup.find_all('div')
            removed_count = 0
            
            for div in divs:
                # Vérifier si le div est vide ou ne contient que des divs vides
                has_text = div.get_text(strip=True)
                has_important = div.find_all(['img', 'a', 'script', 'style', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'li', 'table', 'form', 'nav', 'header', 'footer', 'main', 'article', 'section'])
                
                if not has_text and not has_important:
                    div.decompose()
                    removed_count += 1
            
            # Si aucun div n'a été supprimé, arrêter
            if removed_count == 0:
                break
    
    # Appliquer le nettoyage agressif
    remove_empty_divs_aggressive()
    
    # Supprimer les sections vides
    sections = soup.find_all('section')
    for section in sections:
        if not section.get_text(strip=True) and not section.find_all(['img', 'a', 'script', 'style', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'li', 'table', 'form']):
            section.decompose()
    
    # Supprimer tous les attributs data-*
    for element in soup.find_all():
        if element.attrs:
            attrs_to_remove = []
            for attr in element.attrs.keys():
                if attr.startswith('data-'):
                    attrs_to_remove.append(attr)
            for attr in attrs_to_remove:
                del element[attr]
    
    # Nettoyer les classes vides
    for element in soup.find_all(class_=True):
        if not element['class']:
            del element['class']
    
    return str(soup)

def clean_file_aggressive(file_path):
    """Nettoie un fichier HTML avec la méthode agressive"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"🧹 Nettoyage agressif de {file_path}...")
        
        # Nettoyer le contenu
        cleaned_content = aggressive_clean_html(content)
        
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
    print("🧹 Nettoyage agressif du HTML...")
    print("=" * 50)
    
    # Trouver tous les fichiers HTML à la racine
    html_files = []
    for file in os.listdir('.'):
        if file.endswith('.html') and file != 'index-backup.html':
            html_files.append(file)
    
    print(f"📄 Trouvé {len(html_files)} fichiers HTML à nettoyer")
    
    cleaned_files = 0
    
    for html_file in html_files:
        if clean_file_aggressive(html_file):
            cleaned_files += 1
    
    print(f"\n✅ {cleaned_files} fichiers nettoyés")
    print("🎯 Le code HTML est maintenant ultra-propre!")

if __name__ == "__main__":
    main()

