document.getElementById('generateMidi').addEventListener('click', function () {
    let http = new XMLHttpRequest();
    http.open('POST', '/generate-midi', true);
    http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    document.getElementById('loading').classList.remove('hidden');
    
    http.onreadystatechange = function () {
        if (http.readyState == 4 && http.status == 200) {
            document.getElementById('loading').classList.add('hidden');
            alert(http.responseText);
        }
    }

    let order = document.getElementById('order').value;
    http.send('order=' + order);
})

document.getElementById('playMIDI').addEventListener('click', function () {
    MIDIjs.play('static/generated.mid');
})

document.getElementById('stopMIDI').addEventListener('click', function () {
    MIDIjs.stop();
})