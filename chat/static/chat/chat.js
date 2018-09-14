




// function insertMessage() {
//     console.log('insert msg..')
//     msg = $('.message-input').val();
//     if ($.trim(msg) == '') {
//         return false;
//     }
//     $('<div class="message message-personal">' + msg + '</div>').appendTo(
//         $('.mCSB_container')
//     ).addClass('new');

//     setDate();
//     $('.message-input').val(null);
//     updateScrollbar();
//     setTimeout(function () {
//         fakeMessage();
//     }, 1000 + (Math.random() * 20) * 100);
// }

// $('.message-submit').click(function () {
//     insertMessage();
// });

// $(window).on('keydown', function (e) {
//     if (e.which == 13) {
//         insertMessage();
//         return false;
//     }
// })

    var chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/');

    //append change log
    chatSocket.onmessage = function(e) {
        console.log('on-message event.')
        var data = JSON.parse(e.data);
        var message = data['message'];
        $('#chat-log').text += (message + '\n');
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    var input_id = '.message-input';
    var submit_id = '#message-submit';
    
    //focus on textarea
    $(input_id).focus();
    //keyboard submit
    $(input_id).onkeyup = function(e) {
        // enter, return
        if (e.keyCode === 13) {  
            $(submit_id).click();
        }
    };
    //mouse click submit
    $(submit_id).click(function(e){
        console.log('client sending....');

        var messageInputDom = $(input_id);
        chatSocket.send(JSON.stringify({
            'message': messageInputDom.value
        }));
        //reset input area
        messageInputDom.value = '';
    });
