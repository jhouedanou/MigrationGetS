// Fonction pour charger les includes
function loadIncludes() {
    // Détecter le chemin de base selon la localisation de la page
    // Si on est dans un sous-dossier (pages/, missions/, contact/, etc.), il faut remonter d'un niveau
    var currentPath = window.location.pathname;
    var isInSubfolder = currentPath.split('/').length > 2 && !currentPath.endsWith('/index.html') || 
                       currentPath.includes('/pages/') || currentPath.includes('/missions/') || 
                       currentPath.includes('/contact/') || currentPath.includes('/author/') ||
                       currentPath.includes('/category/') || currentPath.includes('/elementor-hf/') ||
                       currentPath.match(/\/[^\/]+\/index\.html$/);
    var basePath = isInSubfolder ? '../' : '';
    
    // Ajouter le lien vers styles.css si pas déjà présent
    if (!document.querySelector('link[href*="styles.css"]')) {
        var stylesLink = document.createElement('link');
        stylesLink.rel = 'stylesheet';
        stylesLink.type = 'text/css';
        stylesLink.href = basePath + 'styles.css';
        document.head.appendChild(stylesLink);
    }
    
    // Charger le header
    $('#header-placeholder').load(basePath + 'includes/header.html', function() {
        console.log('Header loaded successfully');
        // Corriger les chemins des images si on est dans /pages/
        if (basePath) {
            fixImagePaths('#header-placeholder', basePath);
        }
        // Re-initialiser les scripts Google CSE après le chargement
        if (typeof google !== 'undefined' && google.search && google.search.cse) {
            google.search.cse.element.render('searchresults-only');
        }
    });

    // Charger le menu de navigation
    $('#nav-placeholder').load(basePath + 'includes/nav.html', function() {
        console.log('Navigation loaded successfully');
        // Corriger les chemins des images si on est dans /pages/
        if (basePath) {
            fixImagePaths('#nav-placeholder', basePath);
        }
    });

    // Charger le footer
    $('#footer-placeholder').load(basePath + 'includes/footer.html', function() {
        console.log('Footer loaded successfully');
        // Corriger les chemins des images si on est dans /pages/
        if (basePath) {
            fixImagePaths('#footer-placeholder', basePath);
        }
    });
}

// Fonction pour corriger les chemins des images et des liens
function fixImagePaths(container, basePath) {
    $(container).find('img').each(function() {
        var src = $(this).attr('src');
        if (src && !src.startsWith('http') && !src.startsWith('../')) {
            $(this).attr('src', basePath + src);
        }
    });
    
    // Corriger aussi les liens de navigation
    $(container).find('a').each(function() {
        var href = $(this).attr('href');
        if (href && !href.startsWith('http') && !href.startsWith('#') && !href.startsWith('../') && !href.startsWith('mailto:') && !href.startsWith('tel:')) {
            // Si le lien ne commence pas par ../, l'ajouter
            if (!href.startsWith('../')) {
                $(this).attr('href', basePath + href);
            }
        }
    });
}

// Alternative avec JavaScript vanilla (sans jQuery)
function loadIncludesVanilla() {
    // Détecter le chemin de base selon la localisation de la page
    // Si on est dans un sous-dossier (pages/, missions/, contact/, etc.), il faut remonter d'un niveau
    var currentPath = window.location.pathname;
    var isInSubfolder = currentPath.split('/').length > 2 && !currentPath.endsWith('/index.html') || 
                       currentPath.includes('/pages/') || currentPath.includes('/missions/') || 
                       currentPath.includes('/contact/') || currentPath.includes('/author/') ||
                       currentPath.includes('/category/') || currentPath.includes('/elementor-hf/') ||
                       currentPath.match(/\/[^\/]+\/index\.html$/);
    var basePath = isInSubfolder ? '../' : '';
    
    // Ajouter le lien vers styles.css si pas déjà présent
    if (!document.querySelector('link[href*="styles.css"]')) {
        var stylesLink = document.createElement('link');
        stylesLink.rel = 'stylesheet';
        stylesLink.type = 'text/css';
        stylesLink.href = basePath + 'styles.css';
        document.head.appendChild(stylesLink);
    }
    
    loadInclude('header-placeholder', basePath + 'includes/header.html', basePath);
    loadInclude('nav-placeholder', basePath + 'includes/nav.html', basePath);
    loadInclude('footer-placeholder', basePath + 'includes/footer.html', basePath);
}

function loadInclude(elementId, filePath, basePath) {
    fetch(filePath)
        .then(response => response.text())
        .then(data => {
            document.getElementById(elementId).innerHTML = data;
            // Corriger les chemins des images si on est dans /pages/
            if (basePath) {
                fixImagePathsVanilla(elementId, basePath);
            }
        })
        .catch(error => {
            console.error('Erreur lors du chargement de', filePath, ':', error);
        });
}

// Fonction pour corriger les chemins des images et des liens (version vanilla)
function fixImagePathsVanilla(containerId, basePath) {
    var container = document.getElementById(containerId);
    if (container) {
        // Corriger les images
        var images = container.querySelectorAll('img');
        images.forEach(function(img) {
            var src = img.getAttribute('src');
            if (src && !src.startsWith('http') && !src.startsWith('../')) {
                img.setAttribute('src', basePath + src);
            }
        });
        
        // Corriger les liens
        var links = container.querySelectorAll('a');
        links.forEach(function(link) {
            var href = link.getAttribute('href');
            if (href && !href.startsWith('http') && !href.startsWith('#') && !href.startsWith('../') && !href.startsWith('mailto:') && !href.startsWith('tel:')) {
                if (!href.startsWith('../')) {
                    link.setAttribute('href', basePath + href);
                }
            }
        });
    }
}

// Charger les includes quand le DOM est prêt
$(document).ready(function() {
    loadIncludes();
});

// Alternative sans jQuery
// document.addEventListener('DOMContentLoaded', function() {
//     loadIncludesVanilla();
// });