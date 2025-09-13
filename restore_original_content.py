#!/usr/bin/env python3
import os
import shutil

# Mapping des pages avec leur contenu original
page_mappings = {
    "missions": {
        "source": "missions/index.html",
        "title": "MISSIONS - G-ET-S"
    },
    "evaluation-diagnostic-dun-conseil-dadministration-ou-de-surveilance": {
        "source": "missions/evaluation-diagnostic-dun-conseil-dadministration-ou-de-surveilance/index.html",
        "title": "Diagnostic de Conseil d'Administration - G-ET-S"
    },
    "recherche-de-mandataires-sociaux": {
        "source": "missions/recherche-de-mandataires-sociaux/index.html",
        "title": "Recherche mandataires sociaux - G-ET-S"
    },
    "enquetes-et-etudes": {
        "source": "missions/enquetes-et-etudes/index.html",
        "title": "Enquêtes et études - G-ET-S"
    },
    "les-administrateurs-et-lomnipresence-du-numerique": {
        "source": "missions/les-administrateurs-et-lomnipresence-du-numerique/index.html",
        "title": "Les administrateurs et l'omniprésence du numérique - G-ET-S"
    },
    "gouvernance-advisors": {
        "source": "gouvernance-advisors/index.html",
        "title": "Gouvernance Advisors - G-ET-S"
    },
    "formations-dadministrateurs": {
        "source": "formations-dadministrateurs/index.html",
        "title": "Formations d'Administrateurs - G-ET-S"
    },
    "candidats-mandataires-administratrices-administrateurs-7": {
        "source": "candidats-mandataires-administratrices-administrateurs-7/index.html",
        "title": "Candidats Mandataires Sociaux - G-ET-S"
    },
    "sites-interesssants": {
        "source": "sites-interesssants/index.html",
        "title": "Sites Intéressants - G-ET-S"
    },
    "bibliographie-corporate-governance": {
        "source": "bibliographie-corporate-governance/index.html",
        "title": "Bibliographies - G-ET-S"
    },
    "la-presse-parle-de-gouvernance-structures": {
        "source": "la-presse-parle-de-gouvernance-structures/index.html",
        "title": "Presse - G-ET-S"
    }
}

def restore_original_content():
    """Restore original content for pages that have source files"""
    restored_count = 0
    
    for page_name, page_info in page_mappings.items():
        source_file = page_info["source"]
        target_file = f"pages/{page_name}.html"
        
        if os.path.exists(source_file):
            # Read the original content
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update the title if needed
            if page_info["title"]:
                content = content.replace(
                    f'<title>{page_info["title"]}</title>',
                    f'<title>{page_info["title"]}</title>'
                )
            
            # Write to the pages directory
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Restauré: {target_file} depuis {source_file}")
            restored_count += 1
        else:
            print(f"⚠️  Source non trouvée: {source_file}")
    
    print(f"\n📊 {restored_count} pages restaurées avec leur contenu original")
    return restored_count

if __name__ == "__main__":
    restore_original_content()