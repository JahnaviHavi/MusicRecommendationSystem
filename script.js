document.getElementById("musicForm").addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent default form submission

    // Collect user inputs
    const mood = document.getElementById("mood").value;
    const activity = document.getElementById("activity").value;
    const language = document.getElementById("language").value;
    const genre = document.getElementById("genre").value;
    const tempo = document.getElementById("tempo").value;

    // Send inputs to backend
    const response = await fetch("http://127.0.0.1:5000/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mood, activity, language, genre, tempo }),
    });

    // Parse and display the results
    const tracks = await response.json();
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = ""; // Clear previous results

    tracks.forEach(track => {
        const trackDiv = document.createElement("div");
        trackDiv.className = "track";
        trackDiv.innerHTML = `
            <img src="${track.image_url}" alt="Album Cover" width="100" height="100">
            <p>${track.name} by ${track.artist}</p>
            <p>Release Date: ${track.release_date}</p>
            ${track.preview_url ? `<audio controls src="${track.preview_url}"></audio>` : "<p>No preview available</p>"}
        `;
        resultsDiv.appendChild(trackDiv);
    });
    
});
