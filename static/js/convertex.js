// ConverTex Scripts

function buildElement(obj) {
    if (obj['tagName'] === 'text') {
        return document.createTextNode(obj['text']);
    } else {
        // Create element
        var parentNode = document.createElement(obj['tagName'].toUpperCase());
        var index;

        // Set attributes
        for (index in obj) {
            if (index !== 'tagName' && index !== 'text' && index !== 'children') {
                parentNode.setAttribute(index, obj[index]);
            }
        }

        // Add children
        if ('children' in obj) {
            for (index in obj['children']) {
                parentNode.appendChild(buildElement(obj['children'][index]));
            }
        } else if ('text' in obj) {
            parentNode.appendChild(document.createTextNode(obj['text']));
        }

        return parentNode;
    }
}

function newcard() {
    newcard = document.getElementById("newcard");
    value = document.getElementById("newinput").value.substring(0, 750);
    newcard.innerHTML = '';
    childElement = buildElement({
        tagName: 'span',
        text: value
    })
    newcard.appendChild(childElement);
    document.getElementById("createcard").style.display = "block";

    $('html,body').animate({
        scrollTop: $("#createcard").offset().top
    }, 800);
    MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
}

function dls(a) {
    var cursorPos = $('#newinput').prop('selectionStart');
    var v = $('#newinput').val();
    var textBefore = v.substring(0,cursorPos);
    var textAfter = v.substring(cursorPos,v.length);
    $('#newinput').val(textBefore+a+textAfter);
    $('#newinput').focus();
    $('#newinput')[0].selectionStart = $('#newinput')[0].selectionEnd = cursorPos+1
    count();
}

function save() {
    content = document.getElementById("newinput").value.substring(0, 750);
    // Hashear
    var XHR = new XMLHttpRequest();
    var urlEncodedData = "";
    urlEncodedData = encodeURIComponent("content") + '=' + encodeURIComponent(content);
    urlEncodedData = urlEncodedData + "&path=" + window.location.pathname;
    XHR.addEventListener('load', function (event) {
        link = "http://www.nekomath.com" + XHR.responseText;
        document.getElementById("linktex").value = link;
        document.getElementById("linktex").select();
    })
    XHR.open('POST', '/cts');
    XHR.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    XHR.send(urlEncodedData);
}

function count() {
    k = String(750 - document.getElementById("newinput").value.length)
    document.getElementById("charcount").innerHTML = k;
    if (k < 0) {
        document.getElementById("charcount").style.color = "rgb(200,55,113)";
    }
    if (k >= 0) {
        document.getElementById("charcount").style.color = "rgb(0,0,43)";
    }
}