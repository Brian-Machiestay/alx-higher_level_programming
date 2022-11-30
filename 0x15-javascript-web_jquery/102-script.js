$(function(){
    $('INPUT#btn_translate').on('click', function(){
        let urll = 'https://stefanbohacek.com/hellosalut/?lang=';
        urll = urll + $('INPUT#language_code').val();
        $.get(urll, function(data, stat){
            $('DIV#hello').text(data.hello);
        });
    });
});