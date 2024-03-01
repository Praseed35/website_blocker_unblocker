function performAction(action) {
    var resultElement = document.getElementById('result');
    var websitesElement = action === 'block' ? document.getElementById('block-websites') : document.getElementById('unblock-websites');
    var websites = websitesElement.value;

    resultElement.innerHTML = ''; // Clear previous results

    fetch(`/${action}_websites`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `websites=${websites}`,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            resultElement.innerHTML = `Websites ${action}ed successfully!`;
        } else {
            resultElement.innerHTML = `Error ${action}ing websites.`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        resultElement.innerHTML = `Error ${action}ing websites.`;
    });
}
