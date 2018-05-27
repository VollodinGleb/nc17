// $('a:has(img.language-select-icon)').click(function() {
//     var lang_code = $(this).attr('data-lang');
//     window.location = window.location.origin + window.location.pathname.replace('ru', lang_code).replace('uk', lang_code).replace('en', lang_code);
//
//     // $.ajax({
//     //     type: 'POST',
//     //     url: '/i18n/setlang/',
//     //     data: {
//     //         "language": lang_code,
//     //         "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val()
//     //
//     //     },
//     //     success: function(){
//     //         window.location.href = window.location.href.replace('/en', '').replace('/ru', '').replace('/uk', '');
//     //     }
//     // });
// });