// Données centralisées des articles pour le site G-ET-S
window.articlesData = {
    'generalites-contrib': [
        { title: "Shadow Conseil d'Administration de jeunes", url: 'pages/shadow-conseil.html', dateCreation: '2025-09-12' },
        { title: 'Administrateur indépendant un vaccin ?', url: 'pages/administrateur-independant.html', dateCreation: '2025-09-30' },
        { title: 'IFA et le Numérique', url: 'pages/travaux-ifa-digital.html', dateCreation: '2025-09-29' },
        { title: 'Comparaison féminisation Boards et Comex', url: 'pages/comparaison-feminisation-boards-comex.html', dateCreation: '2025-09-28' },
        { title: 'Intelligence émotionnelle des administrateurs', url: 'pages/intelligence-emotionnelle-administrateurs.html', dateCreation: '2025-09-27' },
        { title: 'Facilities Management, Les normes Européennes', url: 'pages/facilities-management-normes-europeennes.html', dateCreation: '2025-09-24-4' },
        { title: 'Comment les DSI peuvent impliquer les Conseils d\'Administration', url: 'pages/dsi-conseils-administration.html', dateCreation: '2025-09-24-3' },
        { title: 'Le monde numérique et la relation client', url: 'pages/monde-numerique-relation-client.html', dateCreation: '2025-09-24-2' },
        { title: 'Apports de l\'Intelligence artificielle à la Compliance', url: 'pages/apports-ia-compliance.html', dateCreation: '2025-09-24-1' },
        { title: 'Salariés et Dirigeants en Confiance', url: 'pages/salarie-dirigeants-confiance.html', dateCreation: '2025-09-24-0' },
        { title: 'Le monde et la gouvernance des ETI', url: 'pages/livre-eti.html', dateCreation: '2025-09-20' },
        { title: 'Intelligence collective (Webinar XMPC)', url: 'pages/intelligence-collective.html', dateCreation: '2025-09-14' },
        { title: 'Instances de gouvernance (Cours à l\'INSEEC)', url: 'pages/cours-inseec.html', dateCreation: '2025-09-11' },
        { title: 'Club Européen', url: 'pages/club-europeen.html', construction: true, dateCreation: '2025-09-08' }
    ],
    'generalites-docs': [
        { title: 'Formation aux Comex/Codir', url: 'pages/certificat-centrale.html' },
        { title: "Formations au C.A.", url: 'pages/formations-administrateurs.html' },
        { title: 'Sites intéressants et Amis', url: 'sites-interesssants-4/index.html' },
        { title: 'Bibliographie', url: 'pages/bibliographie.html' }
    ],
    'feminisation-contrib': [
        { title: 'Etudes G & S 2010 à 2025', url: 'pages/etude-juin-2025.html' },
        { title: 'Assises de la parité 2012 et 2023', url: 'pages/assises-parite.html' },
        { title: 'Évènements', url: '#', construction: true },
        { title: 'Article Presse', url: 'la-presse-parle-de-gouvernance-structures/index.html' },
        { title: 'Observatoire des genres', url: 'pages/observatoire-genres.html' }
    ],
    'feminisation-docs': [
        { title: 'Directive Européenne (2024)', url: 'pages/directive-europeenne.html' },
        { title: 'Article 14 Loi Rixain (2021)', url: 'pages/loi-rixain.html' },
        { title: 'Loi Zimmerman (2011)', url: 'pages/loi-zimmerman.html' }
    ],
    'qui': [
        { title: 'Introduction', url: 'pages/organisation-gs.html' },
        { title: 'Gouvernance Advisors', url: 'gouvernance-advisors/index.html' },
        { title: 'Historique', url: 'pages/historique.html' },
        { title: 'Contact', url: 'contact.html' }
    ],
    'pour-mandataires': [
        { title: 'Formation au digital', url: 'pages/informatique.html' },
        { title: 'Candidature comme mandataire', url: 'pages/candidats-mandataires.html' }
    ],
    'pour-societes': [
        { title: 'Candidats mandataires sociaux', url: 'pages/candidats-mandataires-sociaux.html' },
        { title: 'Auto diagnostic Loi Rixain', url: 'pages/questionnaire-rixain-societes.html' },
        { title: 'Diagnostics', url: 'pages/diagnostics-ca.html' },
        { title: "Catalogue de documents pour l'administrateur", url: 'pages/catalogue-documents.html' },
        { title: 'Glossaire des Prestations de conseil', url: 'pages/glossaire-prestations.html' }
    ]
};

// Fonction pour obtenir tous les articles sous forme de tableau simple
window.getAllArticles = function() {
    const allArticles = [];
    for (const category in window.articlesData) {
        const items = window.articlesData[category];
        items.forEach(item => {
            allArticles.push({
                ...item,
                category: category
            });
        });
    }
    return allArticles;
};

// Fonction de recherche (uniquement les pages du dossier /pages/)
window.searchArticles = function(searchTerm) {
    if (!searchTerm || searchTerm.trim() === '') {
        return [];
    }

    const term = searchTerm.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    const allArticles = window.getAllArticles();

    // Filtrer uniquement les articles qui sont dans le dossier pages/
    return allArticles.filter(article => {
        // Vérifier que l'URL commence par 'pages/'
        if (!article.url.startsWith('pages/')) {
            return false;
        }

        const title = article.title.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
        return title.includes(term);
    });
};
