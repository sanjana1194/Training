const tableBody = document.getElementById("tableBody");
const saveBtn = document.getElementById("saveBtn");

saveBtn.onclick = () => {
	const item = {
		itemId: document.getElementById("itemId").value.trim(),
		description: document.getElementById("description").value.trim(),
		unitPrice: document.getElementById("unitPrice").value,
		stockQty: document.getElementById("stockQty").value,
		supplierId: document.getElementById("supplierId").value.trim(),
		reorderLevel: document.getElementById("reorderLevel").value,
		orderQty: document.getElementById("orderQty").value,
		orderStatus: 0
	};

	addRow(item);
	clearFields();
};

function addRow(item) {
	const tr = document.createElement("tr");

	tr.innerHTML = `
		<td>${item.itemId}</td>
		<td>${item.description}</td>
		<td>${item.unitPrice}</td>
		<td>${item.stockQty}</td>
		<td>${item.supplierId}</td>
		<td>${item.reorderLevel}</td>
		<td>${item.orderQty}</td>
		<td>${item.orderStatus}</td>
		<td>
			<button class="editBtn">✏️</button>
		</td>
		<td>
			<button class="deleteBtn">🗑️</button>
		</td>
	`;

	tr.querySelector(".deleteBtn").onclick = () => tr.remove();

	tr.querySelector(".editBtn").onclick = () => loadToForm(tr);

	tableBody.appendChild(tr);
}

function loadToForm(row) {
	const cells = row.children;
	document.getElementById("itemId").value = cells[0].innerText;
	document.getElementById("description").value = cells[1].innerText;
	document.getElementById("unitPrice").value = cells[2].innerText;
	document.getElementById("stockQty").value = cells[3].innerText;
	document.getElementById("supplierId").value = cells[4].innerText;
	document.getElementById("reorderLevel").value = cells[5].innerText;
	document.getElementById("orderQty").value = cells[6].innerText;
	row.remove();
}

function clearFields() {
	document.querySelectorAll("input").forEach(i => i.value = "");
}
