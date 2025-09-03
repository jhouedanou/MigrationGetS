// Fonction pour charger les includes
function loadIncludes() {
    // Charger le header
    $('#header-placeholder').load('includes/header.html', function() {
        console.log('Header loaded successfully');
        // Re-initialiser les scripts Google CSE après le chargement
        if (typeof google !== 'undefined' && google.search && google.search.cse) {
            google.search.cse.element.render('searchresults-only');
        }
    });

    // Charger le menu de navigation
    $('#nav-placeholder').load('includes/nav.html', function() {
        console.log('Navigation loaded successfully');
    });

    // Charger le footer
    $('#footer-placeholder').load('includes/footer.html', function() {
        console.log('Footer loaded successfully');
    });
}

// Alternative avec JavaScript vanilla (sans jQuery)
function loadIncludesVanilla() {
    loadInclude('header-placeholder', 'includes/header.html');
    loadInclude('nav-placeholder', 'includes/nav.html');
    loadInclude('footer-placeholder', 'includes/footer.html');
}

function loadInclude(elementId, filePath) {
    fetch(filePath)
        .then(response => response.text())
        .then(data => {
            document.getElementById(elementId).innerHTML = data;
        })
        .catch(error => {
            console.error('Erreur lors du chargement de', filePath, ':', error);
        });
}

// Charger les includes quand le DOM est prêt
$(document).ready(function() {
    loadIncludes();
});

// Alternative sans jQuery
// document.addEventListener('DOMContentLoaded', function() {
//     loadIncludesVanilla();
// });