$(document).ready(function () {
    $('#nombreImagen').on('change', function () {

        //get the file name
        var fileName = $(this).val();
        fileName = fileName.replace("C:\\fakepath\\", "");
        // var ruta = "C:-Users-Darwin-Documents-PROYECTOS-Integradora-DeteccionPark-Papaya-images-"
        // fileName = ruta + fileName
        //replace the "Choose a file" label
        $(this).next('.custom-file-label').html(fileName);
    })

});