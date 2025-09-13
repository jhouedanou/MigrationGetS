// Search functionality for G-ET-S website
$(document).ready(function() {
    // Enhanced search functionality for the homepage
    function initializeSearch() {
        // Add search capability to navigation links
        $('.nav-link-anchor').each(function() {
            const $link = $(this);
            const linkText = $link.text().toLowerCase();
            $link.attr('data-search-keywords', linkText);
        });
    }
    
    // Filter navigation links based on search term
    function filterNavigation(searchTerm) {
        const term = searchTerm.toLowerCase().trim();
        let visibleCount = 0;
        
        if (!term) {
            // Show all links if search is empty
            $('.nav-link-item').show();
            $('.nav-sub-section').show();
            $('#search-results-count').hide();
            return;
        }
        
        $('.nav-link-item').each(function() {
            const $item = $(this);
            const $link = $item.find('.nav-link-anchor');
            const linkText = $link.text().toLowerCase();
            const keywords = $link.attr('data-search-keywords') || '';
            
            // Check if the search term matches
            if (linkText.includes(term) || keywords.includes(term)) {
                $item.show();
                visibleCount++;
                // Also show parent sub-section if this is a sub-item
                $item.closest('.nav-sub-section').show();
            } else {
                $item.hide();
            }
        });
        
        // Hide empty sub-sections
        $('.nav-sub-section').each(function() {
            const $subSection = $(this);
            const visibleItems = $subSection.find('.nav-link-item:visible').length;
            
            if (visibleItems === 0) {
                $subSection.hide();
            }
        });
        
        // Update results count
        const countText = visibleCount === 0 ? 'Aucun résultat trouvé' : 
                         visibleCount === 1 ? '1 résultat trouvé' : 
                         `${visibleCount} résultats trouvés`;
        $('#search-results-count').text(countText).show();
    }
    
    // Highlight search results
    function highlightSearchResults(searchTerm) {
        const term = searchTerm.toLowerCase().trim();
        
        if (!term) return;
        
        $('.nav-link-anchor:visible').each(function() {
            const $link = $(this);
            const originalText = $link.text();
            const highlightedText = originalText.replace(
                new RegExp(`(${term})`, 'gi'),
                '<mark>$1</mark>'
            );
            
            if (originalText.toLowerCase().includes(term)) {
                $link.html(highlightedText);
            }
        });
    }
    
    // Clear highlights
    function clearHighlights() {
        $('.nav-link-anchor mark').each(function() {
            const $mark = $(this);
            $mark.replaceWith($mark.text());
        });
    }
    
    // Initialize search functionality
    initializeSearch();
    
    // Navigate to homepage with AJAX
    function navigateToHomepage() {
        // Check if we're already on homepage
        if (window.location.pathname.endsWith('index.html') || window.location.pathname === '/') {
            return;
        }
        
        // Use AJAX to load homepage content
        $.ajax({
            url: 'index.html',
            type: 'GET',
            success: function(data) {
                // Extract the main content from the response
                const $newContent = $(data).find('main').html();
                if ($newContent) {
                    $('main').html($newContent);
                    
                    // Update URL without page reload
                    if (history.pushState) {
                        history.pushState(null, null, 'index.html');
                    }
                    
                    // Re-initialize search functionality for new content
                    setTimeout(function() {
                        initializeSearch();
                    }, 100);
                    
                    // Show success message
                    const $toast = $('<div class="alert alert-success alert-dismissible fade show position-fixed" style="top: 20px; right: 20px; z-index: 9999;">' +
                        '<i class="fas fa-home me-2"></i>Page d\'accueil chargée' +
                        '<button type="button" class="btn-close" data-bs-dismiss="alert"></button>' +
                        '</div>');
                    $('body').append($toast);
                    
                    // Auto-hide toast after 3 seconds
                    setTimeout(function() {
                        $toast.alert('close');
                    }, 3000);
                }
            },
            error: function() {
                // Fallback to regular navigation
                window.location.href = 'index.html';
            }
        });
    }

    // Search input event handler
    $(document).on('input', '#nav-search-input', function() {
        const searchTerm = $(this).val();
        
        clearHighlights();
        filterNavigation(searchTerm);
        
        if (searchTerm.trim()) {
            highlightSearchResults(searchTerm);
            $('#clear-search').show();
        } else {
            $('#clear-search').hide();
        }
    });

    // Click handler for search input to navigate to homepage
    $(document).on('click', '#nav-search-input', function() {
        navigateToHomepage();
    });

    // Click handler for search container to navigate to homepage
    $(document).on('click', '.nav-search-container', function(e) {
        // Only trigger if clicking on the container itself, not input or button
        if (e.target === this) {
            navigateToHomepage();
        }
    });
    
    // Clear search button handler
    $(document).on('click', '#clear-search', function() {
        $('#nav-search-input').val('');
        clearHighlights();
        filterNavigation('');
        $('#clear-search').hide();
        $('#search-results-count').hide();
    });
    
    // Keyboard shortcuts
    $(document).on('keydown', function(e) {
        // Ctrl+F or Cmd+F for search focus
        if ((e.ctrlKey || e.metaKey) && e.keyCode === 70) {
            e.preventDefault();
            $('#nav-search-input').focus();
        }
        
        // Escape to clear search
        if (e.keyCode === 27) {
            $('#nav-search-input').val('');
            clearHighlights();
            filterNavigation('');
            $('#clear-search').hide();
            $('#search-results-count').hide();
        }
    });
    
    // Export functions for use by other scripts
    window.G_ET_S_Search = {
        filterNavigation: filterNavigation,
        highlightResults: highlightSearchResults,
        clearHighlights: clearHighlights
    };
});