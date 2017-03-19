var outside = "";
var open1 = "";
var count = 0; //will return the number of clicks
var found = 0;
var timewait = 3000;
var source = "#boxcontainer";

var ImageList = ["texas.png", "google.png", "facebook.png", "nike.png", "honda.png", "nba.png", "microsoft.png", "apple.png"];

function random_val(max, min) {
		return Math.round(Math.random() * (max - min) + min); //returns a random number between 0 and the length of the list - 1
	}
	
function Shuffle() { //shuffles the images
	var imgTotal = $(source).children();
	var Cur_img = $(source + " div:first-child");
	var imgList = new Array();

	for (var i = 0; i < imgTotal.length; i++) {
		imgList[i] = $("#" + Cur_img.attr("id") + " img").attr("src");
		Cur_img = Cur_img.next();
	}
	Cur_img = $(source + " div:first-child");
	for (var z = 0; z < imgTotal.length; z++) {
	var rand1 = random_val(0, imgList.length - 1);

	$("#" + Cur_img.attr("id") + " img").attr("src", imgList[rand1]);
	imgList.splice(rand1, 1);
	Cur_img = Cur_img.next();
	}
}

function opened() { //called whenever a box is clicked
	var id = $(this).attr("id");

	if ($("#" + id + " img").is(":hidden")) {
		$(source + " div").unbind("click", opened);	
		$("#" + id + " img").fadeIn('fast');
		
		if (open1 == "") { 
			outside = id;
			open1 = $("#" + id + " img").attr("src");
			setTimeout(function() {
				$(source + " div").bind("click", opened)
			}, 0);
		} 
		else {
			open2 = $("#" + id + " img").attr("src");
			if (open1 != open2) { //if the images do not match, wait 3 seconds
				setTimeout(function() {
					$("#" + id + " img").fadeOut('fast');
					$("#" + outside + " img").fadeOut('fast');
					outside = "";
					open1 = "";
				}, timewait);
				
			setTimeout(function() {
				$(source + " div").bind("click", opened)
			}, timewait);
			} else { //the images match, so found is increased and the images stay visible
				found++;
				outside = "";
				open1 = "";
				
			setTimeout(function() { //you should be able to immediately click another box after finding a match
				$(source + " div").bind("click", opened)
			}, 50);
			}
		}
		count++;
		if (found == ImageList.length) { //when all the images are found the alert will pop up
			window.alert("Finished the game in "+count+" clicks.");
		}
	}
}

$(function() { //appends the images into the boxes

for (var y = 1; y < 3 ; y++) {
	$.each(ImageList, function(i, val) {
		$(source).append("<div id=b" + y + i + "><img src=" + val + " />");
	});
}
	$(source + " div").click(opened);
	Shuffle();
});