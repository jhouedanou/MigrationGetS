#!/usr/bin/env python3
import os
from datetime import datetime

def generate_sitemap():
    """Generate a sitemap.xml file for the website"""
    
    # Base URL (à modifier selon votre domaine)
    base_url = "https://g-et-s.com"
    
    # Date actuelle
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Pages principales
    pages = [
        {
            "url": "/",
            "priority": "1.0",
            "changefreq": "weekly",
            "lastmod": current_date
        },
        {
            "url": "/contact/",
            "priority": "0.8",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/mentions-legales-confidentialite/",
            "priority": "0.3",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/politique-de-confidentialite/",
            "priority": "0.3",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/plan-du-site/",
            "priority": "0.5",
            "changefreq": "monthly",
            "lastmod": current_date
        }
    ]
    
    # Pages du menu principal
    menu_pages = [
        {
            "url": "/pages/missions.html",
            "priority": "0.9",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/evaluation-diagnostic-dun-conseil-dadministration-ou-de-surveilance.html",
            "priority": "0.8",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/recherche-de-mandataires-sociaux.html",
            "priority": "0.8",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/enquetes-et-etudes.html",
            "priority": "0.8",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/les-administrateurs-et-lomnipresence-du-numerique.html",
            "priority": "0.8",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/gouvernance-advisors.html",
            "priority": "0.8",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/formations-dadministrateurs.html",
            "priority": "0.8",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/candidats-mandataires-administratrices-administrateurs-7.html",
            "priority": "0.8",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/sites-interesssants.html",
            "priority": "0.7",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/bibliographie-corporate-governance.html",
            "priority": "0.7",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/la-presse-parle-de-gouvernance-structures.html",
            "priority": "0.7",
            "changefreq": "weekly",
            "lastmod": current_date
        }
    ]
    
    # Pages des colonnes de la page d'accueil
    column_pages = [
        {
            "url": "/pages/generalites-corporate-governance.html",
            "priority": "0.6",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/historique.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/organisation-gs.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/loi-zimmerman.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/loi-rixain.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/directive-europeenne.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/questionnaire-rixain.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/questionnaire-rixain-societes.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/certificat-centrale.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/cours-inseec.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/assises-parite.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/soiree-lancement.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/etude-juin-2025.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/informatique.html",
            "priority": "0.6",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/monde-numerique.html",
            "priority": "0.6",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/conseils-numerique.html",
            "priority": "0.6",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/ia-compliance.html",
            "priority": "0.6",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/intelligence-collective.html",
            "priority": "0.6",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/entreprise-liberee.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/livre-eti.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/couverture-harmattan.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/catalogue-documents.html",
            "priority": "0.6",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/information-administrateurs.html",
            "priority": "0.6",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/diagnostics-ca.html",
            "priority": "0.6",
            "changefreq": "monthly",
            "lastmod": current_date
        },
        {
            "url": "/pages/shadow-conseil.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/video-glp-vl.html",
            "priority": "0.6",
            "changefreq": "yearly",
            "lastmod": current_date
        },
        {
            "url": "/pages/articles-presse.html",
            "priority": "0.6",
            "changefreq": "weekly",
            "lastmod": current_date
        }
    ]
    
    # Combiner toutes les pages
    all_pages = pages + menu_pages + column_pages
    
    # Générer le XML du sitemap
    sitemap_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
    
    for page in all_pages:
        sitemap_xml += f'''    <url>
        <loc>{base_url}{page['url']}</loc>
        <lastmod>{page['lastmod']}</lastmod>
        <changefreq>{page['changefreq']}</changefreq>
        <priority>{page['priority']}</priority>
    </url>
'''
    
    sitemap_xml += '''</urlset>'''
    
    # Écrire le fichier sitemap.xml
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)
    
    print(f"✅ Sitemap généré: sitemap.xml")
    print(f"📊 {len(all_pages)} pages incluses dans le sitemap")
    print(f"🌐 URL de base: {base_url}")
    print(f"📅 Date de génération: {current_date}")

if __name__ == "__main__":
    generate_sitemap()