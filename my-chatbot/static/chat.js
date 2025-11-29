let open = false;

function toggleChat() {
  open = !open;

  const chatBox = document.getElementById("chat-box");
  const chatIcon = document.getElementById("chat-icon");

  if (open) {
    chatBox.style.display = "flex";
    chatIcon.style.display = "none";
  } else {
    chatBox.style.display = "none";
    chatIcon.style.display = "flex";
  }
}

function appendMessage(text, sender) {
  const msg = document.createElement("div");
  msg.className = sender === "user" ? "msg user" : "msg bot";
  msg.innerHTML = text;
  document.getElementById("chat-body").appendChild(msg);
  document.getElementById("chat-body").scrollTop =
    document.getElementById("chat-body").scrollHeight;
}

async function sendMessage() {
  const input = document.getElementById("message");
  const question = input.value.trim();
  if (!question) return;

  appendMessage(question, "user");
  input.value = "";

  const loading = document.createElement("div");
  loading.className = "msg bot";
  loading.innerHTML = `
  <div class="loader">
    <div class="dot"></div>
    <div class="dot"></div>
    <div class="dot"></div>
  </div>
`;

  document.getElementById("chat-body").appendChild(loading);

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });

    const data = await res.json();
    loading.remove();

    appendMessage(data.answer || "No answer", "bot");
  } catch (err) {
    loading.remove();
    appendMessage("⚠️ Error: " + err.message, "bot");
  }
}

document.addEventListener("keypress", (e) => {
  if (e.key === "Enter") sendMessage();
});
