console.log("hello")

window.onload = function() {
	for (var i = 1099; i < 1165; i++) {
		if (i != 1103) {
			$('body').append("<a href='pdf/HKMagazine_" + i + ".pdf'><img class='img' src='images/HKMagazine_" + i + "-0.png' /></a>");
		}
	}
};