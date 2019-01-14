var areaEN = document.getElementById('textarea-en');
var areaHG = document.getElementById('textarea-hg');

function changeTxtToHG(){ 
	areaHG.value = areaEN.value;
}

function changeTxtToEN(){ 
	areaEN.value = areaHG.value;
}


function showLoading(){
	var loading = document.getElementById('loader');
	loading.classList.add('show-loading');

	var btn = document.getElementById('btn-translate');
	btn.innerHTML = "";
}