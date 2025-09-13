#!/usr/bin/env python3
import os

# Liste des pages à générer
pages = [
    "articles-presse",
    "assises-parite", 
    "catalogue-documents",
    "certificat-centrale",
    "conseils-numerique",
    "cours-inseec",
    "couverture-harmattan",
    "diagnostics-ca",
    "directive-europeenne",
    "entreprise-liberee",
    "etude-juin-2025",
    "generalites-corporate-governance",
    "historique",
    "ia-compliance",
    "information-administrateurs",
    "informatique",
    "intelligence-collective",
    "livre-eti",
    "loi-rixain",
    "loi-zimmerman",
    "monde-numerique",
    "organisation-gs",
    "questionnaire-rixain-societes",
    "questionnaire-rixain",
    "shadow-conseil",
    "soiree-lancement",
    "video-glp-vl"
]

# Template de page en construction
template = '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="keywords" content="Gouvernance & Structures">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} - G-ET-S</title>
        <!-- Bootstrap CSS CDN -->
        <link href="../css/theme.css" rel="stylesheet" type="text/css">
        <link href="../styles.css" rel="stylesheet" type="text/css">
        <link rel="stylesheet" href="../bootstrap/css/bootstrap.min.css" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <!-- Font Awesome CDN for icons -->
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
        <script src="../bootstrap/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
        <!-- jQuery for includes -->
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <!-- Custom includes script -->
        <script src="../js/includes.js"></script>
        <!-- Isotope JS for filtering -->
        <script src="https://unpkg.com/isotope-layout@3/dist/isotope.pkgd.js"></script>
        <!-- Font Awesome CDN for icons -->
    </head>
    <body>
        <!-- Header include -->
        <div id="header-placeholder"></div>
        <!-- Navigation include -->
        <div id="nav-placeholder"></div>
        <!-- Main content goes here -->
        <main class="container-full pt-4 pb-4">
            <div class="container main-container bg-white">
                <!-- Page en construction -->
                <div class="construction-page text-center" style="padding: 80px 20px;">
                    <div class="construction-content">
                        <img src="../wp-content/uploads/2020/02/logo-gets-3C.png" alt="G-ET-S Logo" style="max-width: 300px; height: auto; margin-bottom: 30px;">
                        <h1 style="color: #1e73be; font-size: 2.5rem; margin-bottom: 20px; font-weight: 300;">Page en construction</h1>
                        <p style="font-size: 1.2rem; color: #666; margin-bottom: 30px;">Cette page est actuellement en cours de développement.</p>
                        <p style="color: #888; margin-bottom: 40px;">Merci de votre patience. Le contenu sera bientôt disponible.</p>
                        <a href="../index.html" class="btn btn-primary" style="background-color: #1e73be; border-color: #1e73be; padding: 12px 30px; font-size: 1.1rem; text-decoration: none; border-radius: 5px;">Retour à l'accueil</a>
                    </div>
                </div>
            </div>
        </main>
        <!-- Footer include -->
        <div id="footer-placeholder"></div>
        <!-- Homepage functionality script -->
        <script src="../js/homepage.js"></script>
        <script src="../assets/js/popper.min.js"></script>
    </body>
</html>'''

# Titres des pages
titles = {
    "articles-presse": "Articles de presse",
    "assises-parite": "Les assises de la Parité", 
    "catalogue-documents": "Catalogue des documents pour l'administrateur",
    "certificat-centrale": "Certificat Centrale-Supelec Comex Codir",
    "conseils-numerique": "Les conseils d'administration et le numérique",
    "cours-inseec": "Cours INSEEC Les Instances de Gouvernance",
    "couverture-harmattan": "Couverture L'Harmattan",
    "diagnostics-ca": "Diagnostics pour CA",
    "directive-europeenne": "Directive Européenne (Novembre 2024)",
    "entreprise-liberee": "Entreprise libérée (Préface)",
    "etude-juin-2025": "Etude fin juin 2025",
    "generalites-corporate-governance": "Généralités Corporate Governance",
    "historique": "Historique",
    "ia-compliance": "IA et la Compliance (Avant-Propos)",
    "information-administrateurs": "L'information des administrateurs",
    "informatique": "Informatique",
    "intelligence-collective": "Intelligence collective (Webinar XMPC)",
    "livre-eti": "Livre ETI",
    "loi-rixain": "La Loi Rixain Décembre 2021",
    "loi-zimmerman": "La loi Zimmerman Janvier 2011",
    "monde-numerique": "Le monde numérique et la relation client (Vidéo)",
    "organisation-gs": "Organisation G & S",
    "questionnaire-rixain-societes": "Questionnaire Enquête Rixain pour les sociétés",
    "questionnaire-rixain": "Questionnaire Enquête Rixain",
    "shadow-conseil": "Shadow Conseil d'Administration de jeunes (Article)",
    "soiree-lancement": "Soirée de lancement",
    "video-glp-vl": "Video GLP VL"
}

# Générer toutes les pages
for page in pages:
    title = titles.get(page, page.replace('-', ' ').title())
    content = template.format(title=title)
    
    filename = f"pages/{page}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Généré: {filename}")

print("Toutes les pages ont été générées avec le template 'en construction'.")