// Homepage functionality with Isotope.js, search, and AJAX navigation
$(document).ready(function() {
    let $grid;
    let isIsotopeInitialized = false;

    // Initialize Isotope
    function initIsotope() {
        if (isIsotopeInitialized) return;
        
        $grid = $('.content-grid').isotope({
            itemSelector: '.grid-item',
            layoutMode: 'fitRows',
            getSortData: {
                name: '.card-title',
                category: '[data-category]'
            },
            transitionDuration: '0.8s'
        });
        
        isIsotopeInitialized = true;
    }

    // Initialize Isotope after a short delay to ensure DOM is ready
    setTimeout(initIsotope, 100);

    // Category filter functionality
    $('#category-filter').on('change', function() {
        const filterValue = this.value;
        if ($grid && isIsotopeInitialized) {
            $grid.isotope({ filter: filterValue });
        }
        
        // Update search to work with filtered items
        performSearch();
    });

    // Search functionality
    $('#search-input').on('keyup', debounce(function() {
        performSearch();
    }, 300));

    // Debounce function to limit search frequency
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // Perform search based on text content
    function performSearch() {
        const searchTerm = $('#search-input').val().toLowerCase().trim();
        const categoryFilter = $('#category-filter').val();
        
        if (!searchTerm) {
            // If no search term, use only category filter
            if ($grid && isIsotopeInitialized) {
                $grid.isotope({ filter: categoryFilter });
            }
            return;
        }

        // Search through grid items
        $('.grid-item').each(function() {
            const $item = $(this);
            const title = $item.find('.card-title').text().toLowerCase();
            const content = $item.find('.card-text').text().toLowerCase();
            const category = $item.data('category');
            
            // Check if item matches search term
            const matchesSearch = title.includes(searchTerm) || content.includes(searchTerm);
            
            // Check if item matches category filter
            const matchesCategory = categoryFilter === '*' || $item.hasClass(categoryFilter.replace('.', ''));
            
            // Show/hide item based on both search and category
            if (matchesSearch && matchesCategory) {
                $item.removeClass('hidden');
            } else {
                $item.addClass('hidden');
            }
        });

        // Update Isotope layout after search
        if ($grid && isIsotopeInitialized) {
            $grid.isotope('layout');
        }
    }

    // AJAX Navigation functionality
    $(document).on('click', '.page-link', function(e) {
        e.preventDefault();
        
        const targetPage = $(this).data('page');
        if (!targetPage) return;
        
        loadPage(targetPage);
    });

    // Load page via AJAX
    function loadPage(pageName) {
        showLoading();
        
        // Simulate AJAX page loading (replace with actual AJAX call)
        setTimeout(() => {
            // This would normally be an AJAX call to load page content
            // $.ajax({
            //     url: `pages/${pageName}.html`,
            //     type: 'GET',
            //     success: function(data) {
            //         $('#main-content').html(data);
            //         hideLoading();
            //         updateURL(pageName);
            //     },
            //     error: function() {
            //         showError('Erreur lors du chargement de la page');
            //         hideLoading();
            //     }
            // });
            
            // For demo purposes, just show a message
            const content = generatePageContent(pageName);
            updateMainContent(content);
            hideLoading();
            updateURL(pageName);
        }, 800);
    }

    // Generate demo page content
    function generatePageContent(pageName) {
        const pageContents = {
            gouvernance: {
                title: 'Gouvernance d\'Entreprise',
                content: `
                    <div class="page-content">
                        <h2>Gouvernance d'Entreprise</h2>
                        <p>La gouvernance d'entreprise désigne l'ensemble des processus, réglementations, lois et institutions destinés à cadrer la manière dont une entreprise est dirigée, administrée et contrôlée.</p>
                        <h3>Principes clés</h3>
                        <ul>
                            <li>Transparence dans la gestion</li>
                            <li>Responsabilité des dirigeants</li>
                            <li>Protection des actionnaires</li>
                            <li>Éthique des affaires</li>
                        </ul>
                        <button class="btn btn-secondary back-home">Retour à l'accueil</button>
                    </div>
                `
            },
            structures: {
                title: 'Structures Organisationnelles',
                content: `
                    <div class="page-content">
                        <h2>Structures Organisationnelles</h2>
                        <p>L'organisation structurelle définit comment les activités sont réparties, coordonnées et contrôlées dans une entreprise.</p>
                        <h3>Types de structures</h3>
                        <ul>
                            <li>Structure hiérarchique</li>
                            <li>Structure matricielle</li>
                            <li>Structure en réseau</li>
                            <li>Structure plate</li>
                        </ul>
                        <button class="btn btn-secondary back-home">Retour à l'accueil</button>
                    </div>
                `
            },
            processus: {
                title: 'Processus Métier',
                content: `
                    <div class="page-content">
                        <h2>Processus Métier</h2>
                        <p>Les processus métier sont des séquences d'activités qui transforment des entrées en sorties pour créer de la valeur.</p>
                        <h3>Étapes de gestion</h3>
                        <ul>
                            <li>Cartographie des processus</li>
                            <li>Analyse et optimisation</li>
                            <li>Implémentation</li>
                            <li>Suivi et amélioration continue</li>
                        </ul>
                        <button class="btn btn-secondary back-home">Retour à l'accueil</button>
                    </div>
                `
            },
            outils: {
                title: 'Outils et Technologies',
                content: `
                    <div class="page-content">
                        <h2>Outils et Technologies</h2>
                        <p>Les outils technologiques supportent et automatisent les processus organisationnels.</p>
                        <h3>Catégories d'outils</h3>
                        <ul>
                            <li>Systèmes d'information</li>
                            <li>Outils de collaboration</li>
                            <li>Solutions de gestion</li>
                            <li>Plateformes d'analyse</li>
                        </ul>
                        <button class="btn btn-secondary back-home">Retour à l'accueil</button>
                    </div>
                `
            }
        };

        return pageContents[pageName] || {
            title: 'Page non trouvée',
            content: `
                <div class="page-content">
                    <h2>Page non trouvée</h2>
                    <p>La page demandée n'existe pas.</p>
                    <button class="btn btn-secondary back-home">Retour à l'accueil</button>
                </div>
            `
        };
    }

    // Update main content
    function updateMainContent(pageData) {
        $('.main-container').html(pageData.content);
        document.title = `${pageData.title} - G-ET-S`;
    }

    // Handle back to home
    $(document).on('click', '.back-home', function() {
        location.reload(); // Simple way to return to homepage
    });

    // Show/hide loading indicator
    function showLoading() {
        $('#loading-indicator').addClass('show');
    }

    function hideLoading() {
        $('#loading-indicator').removeClass('show');
    }

    // Update URL without page reload
    function updateURL(pageName) {
        if (history.pushState) {
            history.pushState({ page: pageName }, '', `#${pageName}`);
        }
    }

    // Handle browser back/forward buttons
    window.addEventListener('popstate', function(e) {
        if (e.state && e.state.page) {
            loadPage(e.state.page);
        } else {
            location.reload(); // Return to homepage
        }
    });

    // Clear search functionality
    function clearSearch() {
        $('#search-input').val('');
        $('#category-filter').val('*');
        $('.grid-item').removeClass('hidden');
        if ($grid && isIsotopeInitialized) {
            $grid.isotope({ filter: '*' });
        }
    }

    // Add clear search button functionality if needed
    $(document).on('click', '.clear-search', function() {
        clearSearch();
    });

    // Handle initial page load with hash
    const hash = window.location.hash.slice(1);
    if (hash && hash !== '') {
        setTimeout(() => {
            loadPage(hash);
        }, 500);
    }
});