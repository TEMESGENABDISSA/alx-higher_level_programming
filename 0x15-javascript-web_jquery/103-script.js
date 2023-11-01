$(document).ready(function () {
    const url = 'https://stefanbohacek.com/hellosalut/?';
    const translate =()=>{
        $.get(url, { lang: $('input#language_code').val() }, function (data) {
            $('div#hello').html(data.hello);
            });
    }

    $('input#btn_translate').on('click', translate);
    $('input#language_code').on('focus', function(){
        $(this).keypress(function(e){
            if(e.which === 13){
                translate();
            }
        })
    })
});
