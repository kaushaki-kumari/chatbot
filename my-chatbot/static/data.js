async function loadTable() {
  const res = await fetch("/list");
  const data = await res.json();

  const tableBody = document.getElementById("tableBody");
  tableBody.innerHTML = "";

  data.forEach((item) => {
    const row = `
      <tr>
        <td><textarea class="edit-box" id="edit_${item.id}" disabled>${item.details}</textarea></td>
        <td>
          <button id="btn_${item.id}" onclick="enableEdit('${item.id}')">Update</button>
          <button onclick="deleteItem('${item.id}')">Delete</button>
        </td>
      </tr>
    `;
    tableBody.innerHTML += row;
  });
}

async function saveDetails() {
  const input = document.getElementById("detailsInput");
  const errorMsg = document.getElementById("errorMsg");
  const value = input.value.trim();

  if (!value) {
    errorMsg.style.display = "block";
    input.style.border = "1px solid red";
    return;
  }

  errorMsg.style.display = "none";

  await fetch("/save", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ details: value }),
  });

  input.value = "";
  loadTable();
}

document.getElementById("detailsInput").addEventListener("input", () => {
  document.getElementById("errorMsg").style.display = "none";
  document.getElementById("detailsInput").style.border = "1px solid #ccc";
});

function cancelDetails() {
  document.getElementById("detailsInput").value = "";
}

async function deleteItem(id) {
  await fetch(`/delete/${id}`, { method: "DELETE" });
  loadTable();
}

function enableEdit(id) {
  const textarea = document.getElementById(`edit_${id}`);
  const btn = document.getElementById(`btn_${id}`);

  if (btn.innerText === "Save") {
    updateItem(id);
    return;
  }

  textarea.disabled = false;
  textarea.focus();
  btn.innerText = "Save";
}

async function updateItem(id) {
  const textarea = document.getElementById(`edit_${id}`);
  const btn = document.getElementById(`btn_${id}`);
  const newValue = textarea.value;

  await fetch(`/update/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ details: newValue }),
  });
  textarea.disabled = true;
  btn.innerText = "Edit";
  loadTable();
}

loadTable();
