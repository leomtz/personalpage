// Right side loader

function updateData(section){

    document.getElementById("data").style.display = "none";
    document.getElementById("ldr").style.display = "block";
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (xhttp.readyState === 4) {
            if (xhttp.status === 200){
                document.getElementById("data").innerHTML = xhttp.responseText;
                document.getElementById("ldr").style.display = "none";
                document.getElementById("data").style.display = "block";
                window.history.pushState("wow data", "Title", "/"+section);
                MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        }
        }
        }
        xhttp.open("GET", "/request/" + section, true);
        xhttp.send();
        $('html,body').animate({
        scrollTop: $("#ldr").offset().top
}, 800);
}

function gosection() {
    if (window.location.pathname != "/"){
    $('html,body').animate({
        scrollTop: $("#data").offset().top
    }, 800);
    }
}