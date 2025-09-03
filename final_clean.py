#!/usr/bin/env python3
import os
import re
from bs4 import BeautifulSoup

def final_clean_html(html_content):
    """Nettoyage final du HTML - suppression de tous les divs vides et inutiles"""
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Supprimer tous les divs vides
    def remove_empty_divs(element):
        """Supprime récursivement les divs vides"""
        divs = element.find_all('div', recursive=False)
        for div in divs:
            # Vérifier si le div est vide ou ne contient que des divs vides
            has_content = div.get_text(strip=True)
            has_important_elements = div.find_all(['img', 'a', 'script', 'style', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'li', 'table', 'form'])
            
            if not has_content and not has_important_elements:
                # Le div est vide, le supprimer
                div.decompose()
            else:
                # Récursivement nettoyer les divs enfants
                remove_empty_divs(div)
    
    # Appliquer le nettoyage récursif
    remove_empty_divs(soup)
    
    # Supprimer les sections vides
    sections = soup.find_all('section')
    for section in sections:
        if not section.get_text(strip=True) and not section.find_all(['img', 'a', 'script', 'style', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'li', 'table', 'form']):
            section.decompose()
    
    # Supprimer les attributs data-* restants
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

def clean_file_final(file_path):
    """Nettoie un fichier HTML avec la méthode finale"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"🧹 Nettoyage final de {file_path}...")
        
        # Nettoyer le contenu
        cleaned_content = final_clean_html(content)
        
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
    print("🧹 Nettoyage final du HTML...")
    print("=" * 50)
    
    # Trouver tous les fichiers HTML à la racine
    html_files = []
    for file in os.listdir('.'):
        if file.endswith('.html') and file != 'index-backup.html':
            html_files.append(file)
    
    print(f"📄 Trouvé {len(html_files)} fichiers HTML à nettoyer")
    
    cleaned_files = 0
    
    for html_file in html_files:
        if clean_file_final(html_file):
            cleaned_files += 1
    
    print(f"\n✅ {cleaned_files} fichiers nettoyés")
    print("🎯 Le code HTML est maintenant propre et optimisé!")

if __name__ == "__main__":
    main()

