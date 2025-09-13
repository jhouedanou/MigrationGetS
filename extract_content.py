import os
import sys
import argparse
from typing import Optional, List
from bs4 import BeautifulSoup

# Root of the project (this script is placed at repo root)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PAGES_DIR = os.path.join(ROOT_DIR, 'pages')

# Mapping heuristique pour certains slugs spéciaux
SPECIAL_MAP = {
    # missions génériques
    'missions': os.path.join(ROOT_DIR, 'missions', 'index.html.backup'),
    'missions-evaluation': os.path.join(ROOT_DIR, 'missions', 'evaluation-diagnostic-dun-conseil-dadministration-ou-de-surveilance', 'index.html'),
    'evaluation-diagnostic-dun-conseil-dadministration-ou-de-surveilance': os.path.join(ROOT_DIR, 'missions', 'evaluation-diagnostic-dun-conseil-dadministration-ou-de-surveilance', 'index.html'),
    'missions-recherche': os.path.join(ROOT_DIR, 'missions', 'recherche-de-mandataires-sociaux', 'index.html'),
    'recherche-de-mandataires-sociaux': os.path.join(ROOT_DIR, 'recherche-de-mandataires-sociaux', 'index.html'),
    'missions-enquetes': os.path.join(ROOT_DIR, 'missions', 'enquetes-et-etudes', 'index.html'),
    'enquetes-et-etudes': os.path.join(ROOT_DIR, 'missions', 'enquetes-et-etudes', 'index.html'),
    'missions-administrateurs-numerique': os.path.join(ROOT_DIR, 'missions', 'les-administrateurs-et-lomnipresence-du-numerique', 'index.html'),
    'les-administrateurs-et-lomnipresence-du-numerique': os.path.join(ROOT_DIR, 'missions', 'les-administrateurs-et-lomnipresence-du-numerique', 'index.html'),

    # pages racine fréquentes
    'gouvernance-advisors': os.path.join(ROOT_DIR, 'gouvernance-advisors', 'index.html.backup'),
    'bibliographie-corporate-governance': os.path.join(ROOT_DIR, 'bibliographie-corporate-governance', 'index.html.backup'),
    'formations-dadministrateurs': os.path.join(ROOT_DIR, 'formations-dadministrateurs', 'index.html.backup'),
    'la-presse-parle-de-gouvernance-structures': os.path.join(ROOT_DIR, 'la-presse-parle-de-gouvernance-structures', 'index.html.backup'),
    'sites-interesssants': os.path.join(ROOT_DIR, 'sites-interesssants-4', 'index.html'),
    'candidats-mandataires-administratrices-administrateurs-7': os.path.join(ROOT_DIR, 'candidats-mandataires-administratrices-administrateurs-7', 'index.html.backup'),
}


def find_source_for_slug(slug: str) -> Optional[str]:
    """Trouve le fichier source backup/index pour un slug donné."""
    # 1) mapping spécial
    if slug in SPECIAL_MAP and os.path.exists(SPECIAL_MAP[slug]):
        return SPECIAL_MAP[slug]

    # 2) dossier racine portant le même nom
    direct_dir = os.path.join(ROOT_DIR, slug)
    if os.path.isdir(direct_dir):
        for candidate in ['index.html.backup', 'index.html']:
            p = os.path.join(direct_dir, candidate)
            if os.path.exists(p):
                return p

    # 3) fallback: tenter dans missions/ sous-dossiers (match partiel)
    missions_dir = os.path.join(ROOT_DIR, 'missions')
    if os.path.isdir(missions_dir):
        for name in os.listdir(missions_dir):
            cand_dir = os.path.join(missions_dir, name)
            if os.path.isdir(cand_dir):
                # match grossier sur des mots du slug
                if all(part in name for part in slug.split('-')) or all(part in slug for part in name.split('-')):
                    for candidate in ['index.html.backup', 'index.html']:
                        p = os.path.join(cand_dir, candidate)
                        if os.path.exists(p):
                            return p

    return None


def extract_css_hrefs(backup_html: str, dst_is_pages: bool = True) -> List[str]:
    """Extrait les href des balises link rel=stylesheet depuis le backup, en ajustant les chemins pour /pages."""
    soup = BeautifulSoup(backup_html, 'html.parser')
    hrefs: List[str] = []
    for link in soup.find_all('link', rel=lambda v: v and 'stylesheet' in v):
        href = link.get('href')
        if not href:
            continue
        # Normaliser quelques chemins pour l’emplacement /pages
        if dst_is_pages:
            if href.startswith('images/'):
                href = '../' + href
            elif href.startswith('wp-') or href.startswith('wp-content'):
                href = '../' + href
            elif href.startswith('..'):
                # OK déjà relatif parent
                pass
            elif href.startswith('/'):
                # laisser tel quel (rare)
                pass
            elif href.startswith('http://') or href.startswith('https://'):
                pass
            else:
                # chemins relatifs non préfixés -> les faire remonter d’un cran
                href = '../' + href
        hrefs.append(href)
    # Dédupliquer en conservant l’ordre
    seen = set()
    uniq: List[str] = []
    for h in hrefs:
        if h not in seen:
            seen.add(h)
            uniq.append(h)
    return uniq


def extract_content_html(backup_html: str) -> Optional[str]:
    """Extrait uniquement le contenu (sans header/footer) du backup.
    On privilégie le wrapper #page puis #content, sinon les sections elementor.
    """
    soup = BeautifulSoup(backup_html, 'html.parser')

    # 1) Essayer le conteneur site/page
    page_div = soup.find('div', id='page')
    if page_div:
        return str(page_div)

    # 2) Sinon, le contenu direct
    content_div = soup.find('div', id='content')
    if content_div:
        return str(content_div)

    # 2b) Fallback: div.site-content
    site_content = soup.find('div', class_='site-content')
    if site_content:
        return str(site_content)

    # 2c) Fallback: contenu interne du <main>
    main_tag = soup.find('main')
    if main_tag:
        return main_tag.decode_contents()

    # 3) Sinon, récupérer les sections elementor top-level
    sections = soup.select('section.elementor-section.elementor-top-section')
    if sections:
        frag = '\n'.join(str(s) for s in sections)
        return frag

    # 4) Échec
    return None


def inject_css_into_head(dst_html: str, css_hrefs: List[str]) -> str:
    """Injecte des balises <link rel="stylesheet"> dans le <head> de la cible si absentes."""
    soup = BeautifulSoup(dst_html, 'html.parser')
    head = soup.find('head')
    if not head:
        return dst_html

    existing = set()
    for link in head.find_all('link', rel=lambda v: v and 'stylesheet' in v):
        href = link.get('href')
        if href:
            existing.add(href)

    # Insérer après les liens existants
    for href in css_hrefs:
        if href not in existing:
            new_link = soup.new_tag('link', rel='stylesheet', href=href)
            head.append('\n')
            head.append(new_link)
    return str(soup)


def replace_main_with_content(dst_html: str, content_html: str) -> str:
    """Remplace le contenu du tag <main> par content_html."""
    soup = BeautifulSoup(dst_html, 'html.parser')
    main = soup.find('main')
    if not main:
        # si pas de <main>, on tente d’insérer dans body avant footer placeholder
        body = soup.find('body')
        if body:
            body.append(BeautifulSoup('\n' + content_html + '\n', 'html.parser'))
            return str(soup)
        return dst_html

    # vider le main et insérer le nouveau contenu
    main.clear()
    # préserver les classes/attributs de main existants
    fragment = BeautifulSoup(content_html, 'html.parser')
    # insérer sans altérer l’indentation (BeautifulSoup gère la structure, pas l’espacement)
    main.append(fragment)
    return str(soup)


def process_target(target_page_path: str) -> None:
    with open(target_page_path, 'r', encoding='utf-8') as f:
        dst_html = f.read()

    slug = os.path.splitext(os.path.basename(target_page_path))[0]
    source_path = find_source_for_slug(slug)
    if not source_path or not os.path.exists(source_path):
        print(f"[WARN] Source introuvable pour {slug}")
        return

    with open(source_path, 'r', encoding='utf-8', errors='ignore') as f:
        backup_html = f.read()

    css_hrefs = extract_css_hrefs(backup_html, dst_is_pages=True)
    content_html = extract_content_html(backup_html)

    if not content_html:
        print(f"[WARN] Contenu non extrait pour {slug}")
        return

    # Injecter CSS dans head
    updated_html = inject_css_into_head(dst_html, css_hrefs)
    # Remplacer le contenu du <main>
    updated_html = replace_main_with_content(updated_html, content_html)

    with open(target_page_path, 'w', encoding='utf-8') as f:
        f.write(updated_html)
    print(f"[OK] Mis à jour: {target_page_path} (source: {os.path.relpath(source_path, ROOT_DIR)})")


def main():
    parser = argparse.ArgumentParser(description='Injecter contenu depuis backups vers pages/*.html')
    parser.add_argument('--targets', nargs='*', help='Liste de chemins de fichiers dans pages/ à traiter')
    args = parser.parse_args()

    targets: List[str] = []
    if args.targets:
        for t in args.targets:
            t_abs = t
            if not os.path.isabs(t_abs):
                t_abs = os.path.join(ROOT_DIR, t)
            if os.path.exists(t_abs):
                targets.append(t_abs)
            else:
                print(f"[WARN] Cible inexistante: {t}")
    else:
        # par défaut: toutes les pages
        for name in os.listdir(PAGES_DIR):
            if name.endswith('.html'):
                targets.append(os.path.join(PAGES_DIR, name))

    if not targets:
        print('[INFO] Aucune cible à traiter')
        return

    for target in targets:
        try:
            process_target(target)
        except Exception as e:
            print(f"[ERROR] Échec pour {target}: {e}")


if __name__ == '__main__':
    main() 