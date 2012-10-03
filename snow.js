/*
A dumb JS script that will add falling snowflakes to a page
Requires a browser with decent HTML5 support
*/
count = 100;
var docHeight = Math.max(Math.max(document.body.scrollHeight, document.documentElement.scrollHeight), Math.max(document.body.offsetHeight, document.documentElement.offsetHeight), Math.max(document.body.clientHeight, document.documentElement.clientHeight));
var docWidth = Math.max(Math.max(document.body.scrollWidth, document.documentElement.scrollWidth), Math.max(document.body.offsetWidth, document.documentElement.offsetWidth), Math.max(document.body.clientWidth, document.documentElement.clientWidth));

function snowflakes()
{
	
	for (var i = 0; i < count; i++)
	{
		document.write("<div id=\"snowflake" + i + "\" style=\"position:absolute;z-index:1001; top:" + (-docHeight * 2 * Math.random()-50) + "px; left:" + (Math.random()*(docWidth-10)) + "px;background-color:white;width:10px;height:10px;border-radius:10px;transition:all 1s linear;-webkit-transition:all 1s linear;-o-transition:all 1s linear;-moz-transition:all 1s linear;\"> </div>"); 
	}
	setInterval("move()", 500);
}

function move()
{
	for (var i = 0; i < count; i++)
	{
		var top = parseInt(document.getElementById("snowflake" + i).style.top.replace("px", "")) + 5 + (Math.random()*10);
		if (top < docHeight - 10) document.getElementById("snowflake" + i).style.top = top + "px";
		else document.getElementById("snowflake" + i).style.opacity = "0";
	}
}