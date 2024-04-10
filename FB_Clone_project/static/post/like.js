    // unlike function
    function submitUnLike(post_id){
        $.ajax({
            url: '/post/unlike/'+ post_id +'/',
            type: 'GET',
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success : function(response){
                if (response.success){
                    location.reload();
                }
            } //success close
        })//ajax close
    }// submimtLike close
    
    
    
    //like function
    function submitLike(post_id){
    $.ajax({
        url: '/post/like/'+ post_id +'/',
        type: 'GET',
        data: {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success : function(response){
            if (response.success){
                location.reload();
            }
        } //success close
    })//ajax close
    }// submimtLike close
    