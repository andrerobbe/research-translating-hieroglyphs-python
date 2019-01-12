var areaEN = document.getElementById('textarea-en');
var areaHG = document.getElementById('textarea-hg');

function changeTxtToHG(){ 
	areaHG.value = areaEN.value;
}

function changeTxtToEN(){ 
	areaEN.value = areaHG.value;
}