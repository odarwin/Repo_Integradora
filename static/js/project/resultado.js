$(document).ready(function () {
    $("#aceptaP").click(function (e) {
        $.ajax({
            type: "POST",
            url: "{% url 'Prediccion:guardarPrediccion' %}",
            data: {
                "titulo": $("#imagenPaciente").val(),
                "id_imagen": $("#id_imagen").val(),
                "description": $("#description").val()
            },
            success: function (data) {
                console.log("success");
                console.log(data);
            },
            failure: function (data) {
                console.log("failure");
                console.log(data);
            },
        });

    });

});