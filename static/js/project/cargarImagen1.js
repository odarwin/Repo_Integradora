$(document).ready(function () {

    $("#btnDiagnosticar").click(function (e) {
        var filename = $("#rutaImagen").val().replace(/C:\\fakepath\\/i, '')
        var rutaCompleta = 'C:-Users-Darwin-Documents-PROYECTOS-Integradora-DeteccionPark-Papaya-Papaya-images-' + filename;
        var CSRFtoken = $('input[name=csrfmiddlewaretoken]').val();

        $.post("cargarImagenRuta", {
            rutaImagen: rutaCompleta,
            titulo: filename,
            csrfmiddlewaretoken: CSRFtoken

        });
    });

});