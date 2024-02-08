window.onload = function() {
    var submit_button = document.getElementById('comment-submit-btn');
    
    submit_button.classList.add('hide-div');

    submit_button.classList.add('fade-in');    

    submit_btn_class = $('.comment-btn');

    var comment_column_width = $('.comment-column').width();
    var submit_btn_width = $('.comment-btn').width();

    var magin_left = (comment_column_width - submit_btn_width) - 26;

    submit_btn_class.css('margin-left', magin_left + 'px');
}

document.addEventListener('DOMContentLoaded', function() {
    var submit_button = document.getElementById('comment-submit-btn');
    var comment_text = document.getElementById('comment-txt-box');


    comment_text.addEventListener('focus', function() {
        submit_button.classList.remove('hide-div');
        setTimeout(function() {
            submit_button.classList.add('visible');
        }, 400);        
    });

    comment_text.addEventListener('blur', function() {
        submit_button.classList.remove('visible');
        setTimeout(function() {
            submit_button.classList.add('hide-div');
        }, 400);        
    });
});
