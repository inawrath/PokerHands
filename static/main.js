window.token_poker = '';
$(document).ready(function() {
    function showData(data){
        if(data.status && !data.end){
            token_poker = data.token;
            $('#next_hands, #result').show();
            console.log('@data.end', data.end);
            console.log('@data.status', data.status);
            var div = $('<div></div>');
            var img = $('<img />');
            for(var i = 0; i < data.hand1.hand.length; i++) {
                var card = div.clone();
                $('#hand1 .cards').append(card.addClass('card').append(img.clone().attr('src', data.hand1.hand[i].image)));
            }
            for(var i = 0; i < data.hand2.hand.length; i++) {
                var card = div.clone();
                $('#hand2 .cards').append(card.addClass('card').append(img.clone().attr('src', data.hand2.hand[i].image)));
            }
            $('#result1').append(data.hand1.ranking);
            $('#result2').append(data.hand2.ranking);
            var message = '';
            if (data.win_hand == 0) {
                message = 'Tie';
            } else {
                message = 'Hand ' + data.win_hand;
            }
            $('#result p').html('Win: <span></span>');
            $('#result p span').text(message);
        } else {
            if (data.end) {
                $('#new_game').show();
                $('#result p').html('<span></span>');
                $('#result p span').text('Game Over');
            }
        }
    }
    $('#new_game').on('click', function() {
        $('#hand1 .cards, #hand2 .cards, #result1, #result2').html('');
        $('#result p').html('');
        $(this).hide();
        $.ajax({
            url: '/new',
            type: 'POST',
            dataType: 'json'
        }).done(function(data) {
            console.log(data);
            showData(data);
        });
    });
    $('#next_hands').on('click', function() {
        $('#hand1 .cards, #hand2 .cards, #result1, #result2').html('');
        $('#result p').html('');
        $(this).hide();
        $.ajax({
            url: '/newHand',
            type: 'POST',
            dataType: 'json',
            data: {
                token: token_poker
            }
        }).done(function(data) {
            console.log(data);
            showData(data);
        });
    });

});