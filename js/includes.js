// Fonction pour charger les includes
function loadIncludes() {
    // Déterminer dynamiquement la profondeur pour remonter au dossier racine du site
    // en se basant sur l'URL du script courant (js/includes.js)
    function computeBasePath() {
        try {
            var scriptEl = document.querySelector('script[src*="js/includes.js"]');
            if (!scriptEl) return '';
            var scriptPath = decodeURIComponent(new URL(scriptEl.src, document.baseURI).pathname);
            // scriptPath se termine par /<siteRoot>/js/includes.js → extraire <siteRoot>/
            var anchor = '/js/includes.js';
            var idx = scriptPath.lastIndexOf(anchor);
            if (idx < 0) return '';
            var siteRootPath = scriptPath.substring(0, idx + 1); // inclut le slash final

            var pagePath = decodeURIComponent(window.location.pathname);
            // Si la page n'est pas sous le siteRootPath, ne pas préfixer
            if (pagePath.indexOf(siteRootPath) !== 0) return '';
            // Reste du chemin après le dossier racine du site
            var remainder = pagePath.substring(siteRootPath.length);
            // Exemple: 'index.html' → depth 0 ; 'pages/x.html' → depth 1 ; 'pages/dir/index.html' → depth 2
            var parts = remainder.split('/').filter(function(p){ return p.length > 0; });
            var depth = Math.max(0, parts.length - 1); // retirer le fichier
            return depth > 0 ? Array(depth + 1).join('../') : '';
        } catch (e) {
            console.warn('computeBasePath fallback (""), cause:', e);
            return '';
        }
    }

    var basePath = computeBasePath();
    
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

        // Activer le menu mobile (toggle)
        var $navRoot = $('#nav-placeholder');
        
        // Debug: Check if elements exist
        console.log('Nav root found:', $navRoot.length);
        console.log('Menu toggle found:', $navRoot.find('.menu-toggle').length);
        console.log('Main nav found:', $navRoot.find('.main-nav').length);
        
        $navRoot.off('click', '.menu-toggle').on('click', '.menu-toggle', function (e) {
            e.preventDefault();
            console.log('Menu toggle clicked');
            
            // Always target the real navigation element by id
            var $navigation = $('#site-navigation');
            var $mainNav = $navigation.find('#menu-main-menu, .main-nav');
            
            if ($mainNav.length === 0) {
                // Fallback: search globally
                $mainNav = $('.main-navigation').find('#menu-main-menu, .main-nav');
                $navigation = $('.main-navigation');
            }
            
            console.log('Main nav found:', $mainNav.length);
            console.log('Navigation found:', $navigation.length);
            
            // Toggle with class only; CSS controls display
            var isOpen = $navigation.hasClass('toggled');
            $navigation.toggleClass('toggled', !isOpen);
            $(this).attr('aria-expanded', String(!isOpen));
        });

        // Ouverture/fermeture des sous-menus au clic en mobile
        $navRoot.off('click', '.menu-item-has-children > a').on('click', '.menu-item-has-children > a', function (e) {
            if (window.matchMedia('(max-width: 768px)').matches) {
                e.preventDefault();
                var $submenu = $(this).siblings('.sub-menu');
                $submenu.slideToggle(150);
            }
        });
        
        // Alternative menu toggle handler (global)
        $(document).off('click.menuGlobal').on('click.menuGlobal', '.menu-toggle', function(e) {
            e.preventDefault();
            console.log('Global menu toggle clicked');
            
            var $this = $(this);
            var $navigation = $('#site-navigation');
            var $mainNav = $navigation.find('#menu-main-menu, .main-nav');
            
            if ($navigation.length === 0) {
                $navigation = $('.main-navigation');
                $mainNav = $navigation.find('#menu-main-menu, .main-nav');
            }
            
            console.log('Global - Navigation found:', $navigation.length);
            console.log('Global - Main nav found:', $mainNav.length);
            
            var isOpen = $navigation.hasClass('toggled');
            $navigation.toggleClass('toggled', !isOpen);
            $this.attr('aria-expanded', String(!isOpen));
        });
    });

    // Charger le footer des contributions (si présent)
    if ($('#contribution-footer-placeholder').length > 0) {
        $('#contribution-footer-placeholder').load(basePath + 'includes/footer-contributions.html', function() {
            console.log('Contribution footer loaded successfully');
            // Corriger les chemins des images si on est dans /pages/
            if (basePath) {
                fixImagePaths('#contribution-footer-placeholder', basePath);
            }
        });
    }

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