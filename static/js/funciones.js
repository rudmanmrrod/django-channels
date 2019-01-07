function get_comment(author,user_logged){
  var datos = {
        "user_recibe":user_logged,
        "user_emite":author,
    }
    $.ajax({
        type: 'GET',
        url: URL_LIST_COMMENT,
        data:{
          'user_reci':author
        },
        success: function(response) {
            var data = JSON.parse(response);
            var html = '';
            $.each(data,function(key,value){
                var send = value.fields.visto ? 'done_all' :'done';
                var comment = value.fields.visible ? value.fields.comentario :'Este mensaje fue eliminado';
                html += '<div class="row" onclick="select_chat(this)" data-comment="'+value.pk+'">';
                if(value.fields.fk_user_emite==author){
                    html += '<div class="recived left">'+comment;
                }
                else{
                    html += '<div class="sended right">'+comment;
                    send = 'done_all';
                }
                if(value.fields.visible){
                    html += '<br/><i class="tiny material-icons prefix">'+send+'</i> | ';
                    html += '<small>'+ value.fields.fecha +'</small>';
                }
                html += '</div></div>';
            });
            $('.chat-box').show();
            $('.chat-log').html(html);
            $('#user_to').val(author);
            // bar posicion final
            $('.chat-log').scrollTop(9999999)   
        }
    });
}

function sendMessage(token,author,user_to,comentario){
  $.ajax({
        type: 'POST',
        url: URL_CREATE_COMMENT,
        data:{
          "csrfmiddlewaretoken":token,
          "user_recibe":user_to,
          "comentario":comentario,
          "user_emite":author,
        },
        success: function(response) {
          var data = JSON.parse(response);
          var fields = data[0].fields;
          $('#id_comentario').val('');
          chatSocket.send(JSON.stringify({
              'comentario':fields.comentario,
              'fecha':fields.fecha,
              'fk_user_emite':fields.fk_user_emite,
              'fk_user_recibe':fields.fk_user_recibe,
              'visto':fields.visto
          }));  
        }
    });
}