$(document).ready(function(){

    $('input#form-field-nname').attr('maxlength','40');
    $('input#form-field-vname').attr('maxlength','40');
    $('input#form-field-zielfahrt').attr('maxlength','80');

    $('input#form-field-unfalltag').attr('placeholder', 'TT.MM.JJJJ').mask('99.99.9999');
    $('input#form-field-geburtsdatum').attr('placeholder', 'TT.MM.JJJJ').mask('99.99.9999');
    $('input#form-field-tagfahrt').attr('placeholder', 'TT.MM.JJJJ').mask('99.99.9999');

});

