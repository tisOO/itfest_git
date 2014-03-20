/*hs.graphicsDir = '/highslide/graphics/';
hs.align = 'center';
hs.transitions = ['expand', 'crossfade'];
hs.outlineType = 'rounded-white';
hs.fadeInOut = true;
hs.dimmingOpacity = 0.75;
hs.showCredits = false;

// Add the controlbar
hs.addSlideshow({
	//slideshowGroup: 'group1',
	interval: 5000,
	repeat: false,
	useControls: true,
	fixedControls: 'fit',
	overlayOptions: {
		opacity: 0.75,
		position: 'bottom center',
		hideOnMouseOut: true
	}
});
*/
function pagetotop(){
	t=document.documentElement.scrollTop || document.body.scrollTop;
	l=document.documentElement.scrollLeft || document.body.scrollLeft;
	if(t>0){
		t=t-100;
	}
	if(t<0){
		t=0;
	}
	scroll(l,t);
	if(t>0){	
		setTimeout("pagetotop()",20);
	}
}
function startTime() {
	var t = $('#t_time').attr("time");
    var Ndate = new Date(t);
	var Nseconds = Math.round(Ndate.getTime()/1000);
	var Odate = new Date();
	var Oseconds = Math.round(Odate.getTime()/1000);
	var Rseconds = Nseconds - Oseconds;
	if (Rseconds<=0) $("#timer").html("<p>Олимпиада<br /> закончена</p>");
	else {
		var hours = Math.floor(Rseconds/3600);
		var strHours = hours.toString();
		var ost = (Rseconds%3600);
		var minutes = Math.floor(ost/60);
		var strMinutes = minutes.toString();
		ost = (ost%60);
		var seconds = ost;
		var strSeconds = seconds.toString();
		if (hours<10) strHours = "0" + strHours[0];
		else strHours = strHours[0] + strHours[1];
		if (minutes<10) strMinutes = "0" + strMinutes[0];
		else strMinutes = strMinutes[0] + strMinutes[1];
		if (seconds<10) strSeconds = "0" + strSeconds[0];
		else strSeconds = strSeconds[0] + strSeconds[1];
		$("#t_time").html(strHours + ":" + strMinutes + ":" + strSeconds);
		setTimeout(startTime, 1000);
	}
}
$(document).ready(function(){
	$('#logo').click(function(){
		document.location.href=document.location.hostname;
	});
	$(window).scroll(function() {
		var page_scroll = $(this).scrollTop();
		if ( page_scroll > 100) {
			$('#up').show();
		} else {
			$('#up').hide();
		}
	});
	$("#load").click(function(){
		loadmark();
	});
	$("#getLoginWindow").click(function(){
		$("#loginWindow").fadeIn();
	});
	$("#closeLoginWindow").click(function(){
		$("#loginWindow").fadeOut();
	});
	startTime();
});
$(document).ready(function(){
	var hl = $('#sideleft').innerHeight();
	var hc = $('#content').innerHeight();
	var hr = $('#sideright').innerHeight();
	var maxH = Math.max(hl,hc,hr) - 40;
	$('#sideleft').css({"height":maxH});
	$('#content').css({"height":maxH});
	$('#sideright').css({"height":maxH});
});
