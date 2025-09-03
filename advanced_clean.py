#!/usr/bin/env python3
import os
import re
from bs4 import BeautifulSoup

def clean_html_advanced(html_content):
    """Nettoyage avancé du HTML"""
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Supprimer tous les divs Elementor et leurs attributs
    elementor_patterns = [
        'elementor-section',
        'elementor-container', 
        'elementor-row',
        'elementor-column',
        'elementor-column-wrap',
        'elementor-widget-wrap',
        'elementor-widget-container',
        'elementor-element',
        'elementor-inner',
        'elementor-section-wrap'
    ]
    
    # Supprimer les divs avec des classes Elementor
    for pattern in elementor_patterns:
        elements = soup.find_all('div', class_=re.compile(pattern))
        for element in elements:
            # Extraire le contenu
            content = element.decode_contents()
            # Remplacer par le contenu directement
            element.replace_with(BeautifulSoup(content, 'html.parser'))
    
    # Supprimer les divs vides
    empty_divs = soup.find_all('div')
    for div in empty_divs:
        if not div.get_text(strip=True) and not div.find_all(['img', 'a', 'script', 'style']):
            div.decompose()
    
    # Nettoyer les attributs data-* d'Elementor
    for element in soup.find_all():
        if element.attrs:
            attrs_to_remove = []
            for attr, value in element.attrs.items():
                if attr.startswith('data-') and 'elementor' in str(value):
                    attrs_to_remove.append(attr)
            for attr in attrs_to_remove:
                del element[attr]
    
    # Nettoyer les classes Elementor
    for element in soup.find_all(class_=True):
        classes = element.get('class', [])
        clean_classes = [cls for cls in classes if 'elementor' not in cls]
        if clean_classes:
            element['class'] = clean_classes
        else:
            del element['class']
    
    # Supprimer les divs avec seulement des attributs data-*
    for div in soup.find_all('div'):
        if div.attrs and all(attr.startswith('data-') for attr in div.attrs.keys()):
            content = div.decode_contents()
            div.replace_with(BeautifulSoup(content, 'html.parser'))
    
    # Nettoyer les sections vides
    sections = soup.find_all('section')
    for section in sections:
        if not section.get_text(strip=True) and not section.find_all(['img', 'a', 'script', 'style']):
            section.decompose()
    
    return str(soup)

def clean_html_file_advanced(file_path):
    """Nettoie un fichier HTML avec la méthode avancée"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"🧹 Nettoyage avancé de {file_path}...")
        
        # Nettoyer le contenu
        cleaned_content = clean_html_advanced(content)
        
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
    print("🧹 Nettoyage avancé du HTML...")
    print("=" * 50)
    
    # Trouver tous les fichiers HTML à la racine
    html_files = []
    for file in os.listdir('.'):
        if file.endswith('.html') and file != 'index-backup.html':
            html_files.append(file)
    
    print(f"📄 Trouvé {len(html_files)} fichiers HTML à nettoyer")
    
    cleaned_files = 0
    
    for html_file in html_files:
        if clean_html_file_advanced(html_file):
            cleaned_files += 1
    
    print(f"\n✅ {cleaned_files} fichiers nettoyés")
    print("🎯 Le code HTML a été considérablement simplifié!")

if __name__ == "__main__":
    main()

