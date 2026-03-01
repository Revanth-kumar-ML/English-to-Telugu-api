function translateTextToTelugu() {
    const sentence_english = document.getElementById("englishTextForTelugu").value;

    if (!sentence_english) {
        alert("Please enter text");
        return;
    }

    fetch("/english-to-telugu", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ sentence: sentence_english })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerText = data.translated_text;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}