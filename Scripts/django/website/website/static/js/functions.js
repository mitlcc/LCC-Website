$(function(){
	$.each($(".facebook"), function(index, element){
		var text = $(element).html();
		text = text.replace(/\&lt;/g, "<");
		text = text.replace(/\&gt;/g, ">");
		text = text.replace(/\&amp;#039;/g, "'");
		$(element).html(text);
	});
});
