function show() {
    var tag = document.getElementById("txt");

    var datastring = tag.innerText;

    var firstChar = datastring[0];
    var otherString = datastring.substring(1, datastring.length);
    var newText = otherString + firstChar;

    tag.innerText = newText;
}

setInterval(show, 1000);