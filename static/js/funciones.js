function get_comment(author,user_logged){
  $('.chat-box').show();
}

function sendMessage(){
  chatSocket.send(JSON.stringify({
      'message': $('#id_comentario').val()
  }));
}