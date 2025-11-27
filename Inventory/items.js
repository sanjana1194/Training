window.onload = function() {
	loadItems();
};

function loadItems() {
	fetch("getItems.jsp")
		.then(res => res.json())
		.then(data => {
			const body = document.getElementById("tableBody");
			body.innerHTML = "";

			data.forEach(item => {
				const row = document.createElement("tr");

				row.innerHTML = `
					<td>${item.ItemID}</td>
					<td>${item.Description}</td>
					<td>${item.UnitPrice}</td>
					<td>${item.StockQty}</td>
				`;

				body.appendChild(row);
			});
		})
		.catch(err => console.error("Error:", err));
}
