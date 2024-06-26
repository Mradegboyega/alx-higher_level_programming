$(document).ready(function(){
    $('#btn_translate').click(fetchTranslation);
    
    $('#language_code').keypress(function(event){
        if (event.which === 13) {
            fetchTranslation();
        }
    });

    function fetchTranslation() {
        var languageCode = $('#language_code').val();
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            type: 'GET',
            data: { lang: languageCode },
            success: function(response) {
                $('#hello').text(response.hello);
            },
            error: function() {
                $('#hello').text('Error fetching translation');
            }
        });
    }
});
