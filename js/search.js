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
        
        if (!term) {
            // Show all links if search is empty
            $('.nav-link-item').show();
            $('.nav-sub-section').show();
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
    
    // Add search input to the page if it doesn't exist
    function addSearchInput() {
        if ($('#nav-search-input').length === 0) {
            const searchHtml = `
                <div class="nav-search-container" style="margin: 20px 0; text-align: center;">
                    <input type="text" id="nav-search-input" 
                           placeholder="Rechercher dans la navigation..." 
                           class="form-control" 
                           style="max-width: 400px; margin: 0 auto;">
                    <button type="button" id="clear-search" 
                            class="btn btn-sm btn-outline-secondary mt-2"
                            style="display: none;">
                        Effacer la recherche
                    </button>
                </div>
            `;
            
            $('.navigation-tabs-section').prepend(searchHtml);
        }
    }
    
    // Initialize search functionality
    initializeSearch();
    addSearchInput();
    
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
    
    // Clear search button handler
    $(document).on('click', '#clear-search', function() {
        $('#nav-search-input').val('');
        clearHighlights();
        filterNavigation('');
        $('#clear-search').hide();
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
        }
    });
    
    // Export functions for use by other scripts
    window.G_ET_S_Search = {
        filterNavigation: filterNavigation,
        highlightResults: highlightSearchResults,
        clearHighlights: clearHighlights
    };
});