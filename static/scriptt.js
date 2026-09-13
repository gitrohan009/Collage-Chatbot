alert("JavaScript Connected");

// ---------------- CHATBOT ----------------
async function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    let chatBox = document.getElementById("chat-area");

    if (userInput === "") {
        return;
    }

    chatBox.innerHTML += "<b>You:</b> " + userInput + "<br>";

    let response = await fetch("/chatbot", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
    });

    let data = await response.json();

    chatBox.innerHTML += "<b>Chatbot:</b> " + data.reply + "<br><br>";

    document.getElementById("userInput").value = "";
    

}

// ---------------- LOGIN ----------------
async function login() {
    let roll = document.getElementById("roll").value;
    let password = document.getElementById("password").value;
    let error = document.getElementById("error-msg");

    if (roll === "" || password === "") {
        error.innerHTML = "Please enter Roll Number and Password";
        return;
    }

    let response = await fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            roll: roll,
            password: password
        })
    });

    let data = await response.json();

    if (data.status === "success") {
        window.location.href = "/chat";
    } else {
        error.innerHTML = "Invalid Roll Number or Password";
    }
}
function quickQuestion(question) {
    document.getElementById("userInput").value = question;
    sendMessage();
}