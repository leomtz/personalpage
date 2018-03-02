// Right side loader

function updateData(section){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (xhttp.readyState === 4) {
            if (xhttp.status === 200){
    document.getElementById("data").innerHTML = xhttp.responseText;
window.history.pushState("wow data", "Title", "/"+section);
MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
}
}
}
xhttp.open("GET", "/request/" + section, true);
xhttp.send();
        $('html,body').animate({
        scrollTop: $("#data").offset().top
}, 800);
}

// ConverTex Scripts

function update() {
    document.getElementById("textMJ").innerHTML = document.getElementById("datamj").value.substring(0,750)
    MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
    $('html,body').animate({
        scrollTop: $("#textMJ").offset().top
    }, 800);
}
function dls(a) {
        document.getElementById("datamj").value = document.getElementById("datamj").value + a;
        document.getElementById("datamj").focus();
        count();
    }

function count() {
    k = String(750 - document.getElementById("datamj").value.length)
    document.getElementById("charcount").innerHTML = k;
    if (k < 0){
        document.getElementById("charcount").style.color = "rgb(200,55,113)";
    }
    if (k >= 0) {
        document.getElementById("charcount").style.color = "rgb(0,0,43)";
    }
}