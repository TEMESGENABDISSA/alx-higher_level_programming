$(document).ready(function () {
    const url = 'https://stefanbohacek.com/hellosalut/?';
    $('INPUT#btn_translate').click(function () {
      $.get(url, { lang: $('INPUT#language_code').val() }, function (data) {
        $('DIV#hello').html(data.hello);
      });
    });
  });
