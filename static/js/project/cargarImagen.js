function load() {
	console.log("loading");
	loading = document.getElementById("loading");
	loading.style.visibility = "visible";
}

$(document).ready(function () {
	$("#nombreImagen").on("change", function () {
		//get the file name
		var fileName = $(this).val();
		fileName = fileName.replace("C:\\fakepath\\", "");
		// var ruta = "C:-Users-Darwin-Documents-PROYECTOS-Integradora-DeteccionPark-Papaya-images-"
		// fileName = ruta + fileName
		//replace the "Choose a file" label
		$(this).next(".custom-file-label").html(fileName);
	});
});

var container = 0;
function loadMRI() {
	file = document.getElementById("nombreImagen").files[0];
	var params = {
		files: [file],
	};
	console.log(container);
	papaya.Container.resetViewer(0, params);
}
