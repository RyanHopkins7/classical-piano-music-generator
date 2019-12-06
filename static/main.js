document.getElementById('generateMidi').addEventListener('click', function () {
    let http = new XMLHttpRequest();
    http.open('POST', '/generate-midi', true);
    http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

    http.onreadystatechange = function () {
        if (http.readyState == 4 && http.status == 200) {
            alert(http.responseText);
        }
    }

    let order = document.getElementById('order').value;
    http.send('order=' + order);
})
