// Detect required margin-bottom for responsive-section 
$(document).ready(function() {
    var responsive_section_class = $('.responsive-section');

    if (responsive_section_class.height() < 500) {
        var html_height = $('html').height();                

        var screen_height = window.innerHeight;  
        var current_margin_bottom = parseInt(responsive_section_class.css('margin-bottom'), 10);                                    
        var remaining_height = screen_height - html_height;

        var new_margin_bottom = current_margin_bottom + remaining_height;

        responsive_section_class.css('margin-bottom', new_margin_bottom + 'px');
    }
});  