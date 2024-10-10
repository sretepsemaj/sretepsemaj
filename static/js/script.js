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
