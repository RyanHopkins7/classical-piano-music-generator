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
    // Get midi file generated from specified order markov chain and prevent file from being cached
    let order = document.getElementById('order').value;
    MIDIjs.play('/serve-midi?t=' + Date.now() + '&order=' + order);
})

document.getElementById('stopMIDI').addEventListener('click', function () {
    MIDIjs.stop();
})