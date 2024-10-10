document.getElementById("apiForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const query = document.getElementById("queryInput").value;

    // Send the API request to the server
    fetch("/api/query", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ query: query })  // Send the query as JSON
    })
    .then(response => response.json())  // Parse the response as JSON
    .then(data => {
        // Update the page with the API response
        document.getElementById("result").innerHTML = `<h3>Response: ${data.response}</h3>`;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerHTML = "An error occurred.";
    });
});
