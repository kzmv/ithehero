$(document).ready(function(){
    $('#reader').html5_qrcode(function(data){
 		 var params = data.split(" ");
 		    window.location.href = "http://"+window.location.host + "/exhibit/" + params[0] +"/" + params[1] +"/";
 	},
 	function(error){
		//show read errors
	}, function(videoError){
		//the video stream could be opened
	}
);
});
