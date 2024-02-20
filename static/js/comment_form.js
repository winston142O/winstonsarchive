window.onload = function() {
    var submit_button = document.getElementById('comment-submit-btn');
    
    submit_button.classList.add('hide-div');

    submit_button.classList.add('fade-in');    

    submit_btn_class = $('.comment-btn');    
}

function setBtnMargin() {
    var comment_column_width = $('.comment-column').width();
    var submit_btn_width = $('.comment-btn').width();

    var magin_left = (comment_column_width - submit_btn_width) - 30;

    submit_btn_class.css('margin-left', magin_left + 'px');
}

document.addEventListener('DOMContentLoaded', function() {
    var submit_button = document.getElementById('comment-submit-btn');
    var comment_text = document.getElementById('comment-txt-box');


    comment_text.addEventListener('focus', function() {
        setBtnMargin();
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

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');    
    
    $('#comment-submit-btn').click(function() {
        var comment_text = $('#comment-txt-box').val();
        var post_id = $('#comment-form').data('post-id');
        var url = $('#comment-form').data('url');
    
        if (comment_text.length > 0) {
            $.ajax({
                url: url,
                type: 'POST',
                data: {
                    'post_id': post_id,
                    'text': comment_text                    
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
                mode: 'same-origin',
                success: function(response) {   
                    $('#comment-txt-box').val('');
                    $('.comments-container').html(response);
                    location.reload();
                },
                fail: function() {
                    alert('An error occurred while posting your comment. Please try again.');
                }
            });
        }
        else {
            alert('Please enter a comment before submitting.');
        }
    });
});