document.getElementById("skinTypeForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const skinType = document.getElementById("skinTypeSelect").value;
    
    if (!skinType) {
        alert("Please select your skin type.");
        return;
    }

    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ skin_type: skinType })
    })
    .then(response => response.json())
    .then(data => {
        const recommendations = data.recommendations;
        const resultsContainer = document.getElementById("resultsContainer");
        const resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = ""; // Clear previous results
        recommendations.forEach(product => {
            const productLink = document.createElement("a");
            productLink.href = product.url;
            productLink.textContent = product.name;
            productLink.target = "_blank"; // Open in new tab
            resultsDiv.appendChild(productLink);
            resultsDiv.appendChild(document.createElement("br")); // Add line break between links
        });

        // Show the results container and hide the skin type form
        document.getElementById("skinTypeForm").style.display = "none";
        resultsContainer.style.display = "block";
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById("restartButton").addEventListener("click", function() {
    // Reset the page to its initial state
    document.getElementById("skinTypeForm").reset();
    document.getElementById("skinTypeForm").style.display = "block";
    document.getElementById("resultsContainer").style.display = "none";
});
