#!/bin/bash

echo "🔧 Mise à jour de toutes les pages avec Bootstrap CDN..."

# Template Bootstrap pour pages "en cours de construction"
create_construction_page() {
    local filename="$1"
    local title="$2"
    
    cat > "pages/$filename" << 'EOF'
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="keywords" content="Gouvernance & Structures">
    <title>PAGETITLE - G-ET-S</title>
    
    <!-- Bootstrap CSS CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    
    <!-- Font Awesome CDN for icons -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    
    <!-- Custom theme CSS -->
    <link href="../css/theme.css" rel="stylesheet" type="text/css">
    
    <!-- jQuery for includes -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    
    <!-- Bootstrap JS CDN -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
    
    <!-- Custom includes script -->
    <script src="../js/includes.js"></script>
    
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        .container main-container bg-white shadow-sm rounded mt-4 mb-4 p-4 {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            margin-top: 50px;
            margin-bottom: 50px;
            padding: 50px 30px;
            text-align: center;
        }
        
        .logo-section {
            margin-bottom: 40px;
        }
        
        .logo {
            max-width: 300px;
            height: auto;
            filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.1));
        }
        
        .construction-title {
            color: #1e73be;
            font-size: 2.5em;
            margin-bottom: 20px;
            font-weight: 600;
        }
        
        .construction-subtitle {
            color: #6c757d;
            font-size: 1.3em;
            margin-bottom: 30px;
            font-weight: 300;
        }
        
        .construction-description {
            color: #495057;
            font-size: 1.1em;
            margin-bottom: 40px;
            line-height: 1.6;
        }
        
        .spinner-container {
            margin: 30px 0;
        }
        
        .construction-spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #1e73be;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            animation: spin 2s linear infinite;
            margin: 0 auto;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .btn-primary-custom {
            background: linear-gradient(45deg, #1e73be, #4dabf7);
            border: none;
            padding: 12px 30px;
            font-weight: 500;
            border-radius: 25px;
            transition: all 0.3s ease;
            color: white;
            text-decoration: none;
            display: inline-block;
            margin: 10px;
        }
        
        .btn-primary-custom:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 16px rgba(30, 115, 190, 0.3);
            color: white;
            text-decoration: none;
        }
        
        .contact-info {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 25px;
            margin-top: 30px;
            border-left: 4px solid #1e73be;
        }
        
        @media (max-width: 768px) {
            .construction-title {
                font-size: 2em;
            }
            .container main-container bg-white shadow-sm rounded mt-4 mb-4 p-4 {
                margin: 20px 10px;
                padding: 30px 20px;
            }
        }
    </style>
</head>
<body>
    <!-- Header include -->
    <div id="header-placeholder"></div>
    
    <!-- Navigation include -->
    <div id="nav-placeholder"></div>
    
    <!-- Main content -->
    <main class="container-fluid">
        <div class="container">
            <div class="container main-container bg-white shadow-sm rounded mt-4 mb-4 p-4">
                <div class="logo-section">
                    <img src="../images/logo-gs.png" alt="Logo G-ET-S" class="logo" onerror="this.style.display='none'">
                </div>
                
                <h1 class="construction-title">
                    <i class="fas fa-tools text-primary me-3"></i>
                    PAGETITLE
                </h1>
                
                <p class="construction-subtitle">
                    Page en cours de développement
                </p>
                
                <div class="spinner-container">
                    <div class="construction-spinner"></div>
                </div>
                
                <div class="construction-description">
                    <p><i class="fas fa-info-circle text-info me-2"></i> Cette page est actuellement en cours de construction.</p>
                    <p>Notre équipe travaille activement sur ce contenu pour vous offrir la meilleure expérience possible.</p>
                    <p><strong>Contenu à venir :</strong> Informations détaillées, ressources et outils relatifs à ce sujet.</p>
                </div>
                
                <div class="contact-info">
                    <h4><i class="fas fa-envelope text-primary me-2"></i>Nous contacter</h4>
                    <p class="mb-2">Pour plus d'informations sur ce sujet, n'hésitez pas à nous contacter :</p>
                    <p class="mb-0">
                        <i class="fas fa-at text-primary me-2"></i>
                        <strong>Email :</strong> contact@g-et-s.com
                    </p>
                </div>
                
                <div class="mt-4">
                    <a href="../index.html" class="btn-primary-custom">
                        <i class="fas fa-home me-2"></i>
                        Retour à l'accueil
                    </a>
                    <a href="../contact/index.html" class="btn-primary-custom">
                        <i class="fas fa-envelope me-2"></i>
                        Nous contacter
                    </a>
                </div>
            </div>
        </div>
    </main>
    
    <!-- Footer include -->
    <div id="footer-placeholder"></div>
</body>
</html>
EOF

    # Remplacer le titre dans le fichier
    sed -i '' "s/PAGETITLE/$title/g" "pages/$filename"
}

# Liste des pages à créer (format: fichier:titre)
declare -A pages_list=(
    ["articles-presse.html"]="Articles de presse"
    ["catalogue-documents.html"]="Catalogue de documents"
    ["certificat-centrale.html"]="Certificat Centrale"
    ["conseils-numerique.html"]="Les conseils d'administration et le numérique"
    ["cours-inseec.html"]="Cours INSEEC Les Instances de Gouvernance"
    ["couverture-harmattan.html"]="Couverture L'Harmattan"
    ["diagnostics-ca.html"]="Diagnostics CA"
    ["directive-europeenne.html"]="Directive européenne"
    ["entreprise-liberee.html"]="Entreprise libérée (Préface)"
    ["etude-juin-2025.html"]="Etude fin juin 2025"
    ["generalites-corporate-governance.html"]="Généralités Corporate Governance"
    ["ia-compliance.html"]="IA et la Compliance (Avant-Propos)"
    ["information-administrateurs.html"]="L'information des administrateurs"
    ["intelligence-collective.html"]="Intelligence collective (Webinar XMPC)"
    ["livre-gouvernance-ca.html"]="Livre Gouvernance CA"
    ["missions-conseil.html"]="Missions conseil"
    ["monde-numerique.html"]="Le monde numérique et la relation client (Vidéo)"
    ["observatoire-genres.html"]="Observatoire des genres"
    ["ouvrage-collectif-ca.html"]="Ouvrage collectif CA"
    ["plateforme-formation.html"]="Plateforme de formation"
    ["recherche-administrateur.html"]="Recherche administrateur"
    ["shadow-conseil.html"]="Shadow Conseil d'Administration de jeunes (Article)"
    ["soiree-lancement.html"]="Soirée de lancement"
    ["video-glp-vl.html"]="Video GLP VL"
    ["webinaires-passes.html"]="Webinaires passés"
)

echo "📄 Mise à jour des pages de construction..."
for filename in "${!pages_list[@]}"; do
    title="${pages_list[$filename]}"
    echo "  ✅ $filename -> $title"
    create_construction_page "$filename" "$title"
done

echo ""
echo "🎉 Mise à jour terminée !"
echo "📊 $(echo ${!pages_list[@]} | wc -w | xargs) pages mises à jour avec Bootstrap"
echo "✨ Style uniforme appliqué à toutes les pages"