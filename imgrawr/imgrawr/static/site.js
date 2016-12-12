jQuery(document).ready(function($){
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    
    var csrftoken = getCookie('csrftoken');
    
    $('.upvote').on('click', function(){
        var tag = $(this).attr('data-tag');
        var img = $(this).attr('data-img').toString();
        var vote = $(this).parent().children('.vote');
        
        /*img = img.replace(".jpg", "");*/
        
        $.post('/upvote/' + tag + '/' + img, function(data){
            vote.text(data.vote_count);
        });
        
        
    });
    //$.post( "test.php", { name: "John", time: "2pm" } );
});