var $ = jQuery.noConflict();
$(document).ready(function () {
    $('#aceptaR').on('click', function (e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: "guardarPrediccion/nameButton=aceptaR",
            data: $('form').serialize(),
            success: function () {
                console.log("Exito");
            }
        })
    });

    $('#rechazaR').on('click', function (e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: "guardarPrediccion/nameButton=rechazaR",
            data: $('form').serialize(),
            success: function () {
                console.log("Exito");
            }
        })
    })



});