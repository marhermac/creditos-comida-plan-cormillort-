const input = document.getElementById("searchInput");
const table = document.getElementById("dataTable");
const suggestions = document.getElementById("suggestions");

const modal = document.getElementById("modal");
const modalText = document.getElementById("modalText");
const close = document.getElementById("close");

const words = [];

// Cargar palabras desde la tabla
for (let row of table.tBodies[0].rows) {
  words.push(row.cells[0].textContent);
}

// Autocompletar
input.addEventListener("input", () => {
  suggestions.innerHTML = "";
  const value = input.value.toLowerCase();

  words
    .filter(word => word.toLowerCase().startsWith(value))
    .forEach(word => {
      const option = document.createElement("option");
      option.value = word;
      suggestions.appendChild(option);
    });
});

// Buscar y resaltar
input.addEventListener("change", () => {
  let found = false;

  for (let row of table.tBodies[0].rows) {
    row.classList.remove("highlight");

    if (row.cells[0].textContent.toLowerCase() === input.value.toLowerCase()) {
      row.classList.add("highlight");
      found = true;

      modalText.textContent = `Resultado encontrado: ${row.cells[0].textContent}`;
      modal.style.display = "block";
    }
  }

  if (!found) {
    modalText.textContent = "No se encontró el resultado";
    modal.style.display = "block";
  }
});

// Cerrar modal
close.onclick = () => modal.style.display = "none";
window.onclick = e => {
  if (e.target === modal) modal.style.display = "none";
};
