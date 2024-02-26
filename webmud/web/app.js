function sendMessage(ws, id) {
    return function () {
        let inputEl = document.getElementById('input');
        let inputText = inputEl.value;

        inputEl.value = '';
        let history = document.createElement('p');
        history.textContent = inputText;
        document.getElementById('label_input').before(history);
        

        ws.send(JSON.stringify({'id': id, 'command': inputText}));
    } 
}

function receiveMessage({ data }) {
    let history = document.createElement('p');
    history.textContent = data;
    document.getElementById('label_input').before(history);
}

function main() {
    const id = Math.floor(Math.random() * 10_000_000);
    const ws = new WebSocket(`ws://${location.hostname}:8080/`);
    let submitButton = document.getElementById('enter');

    submitButton.addEventListener('click', sendMessage(ws, id));

    ws.addEventListener('message', receiveMessage);



}

document.addEventListener('DOMContentLoaded', main);
