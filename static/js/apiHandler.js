window.onload = function() {
    console.log("Welcome to the report page!");

    // Load whitepaper text content (if needed for another section)
    fetch('/static/whtpaper.txt')
        .then(response => response.text())
        .then(data => {
            document.getElementById('text-box').textContent = data;
        })
        .catch(error => console.error('Error fetching the text file:', error));
};

function submitQuery() {
    const userQuery = document.getElementById('user-query').value;

    fetch('/api/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userQuery })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('api-response').textContent = data.error;
        } else {
            document.getElementById('api-response').textContent = JSON.stringify(data.response, null, 2);
        }
    })
    .catch(error => {
        document.getElementById('api-response').textContent = 'Error: ' + error;
    });
}
