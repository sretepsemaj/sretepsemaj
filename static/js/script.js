window.onload = function() {
    console.log("Welcome to the website!");

    // Fetch the text file and display its content in the div
    fetch('/static/whtpaper.txt')
        .then(response => response.text())  // Convert the response to text
        .then(data => {
            // Insert the text content into the #text-box div
            document.getElementById('text-box').textContent = data;
        })
        .catch(error => console.error('Error fetching the text file:', error));
};

// Function to handle query submission
function submitQuery() {
    const userQuery = document.getElementById('user-query').value;

    // Send the query to the server
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
            // Display the response from the server
            document.getElementById('api-response').textContent = JSON.stringify(data.response, null, 2);
        }
    })
    .catch(error => {
        document.getElementById('api-response').textContent = 'Error: ' + error;
    });
}
