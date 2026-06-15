// Monthly Sales

new Chart(document.getElementById("salesChart"), {
type: "line",
data: {
labels: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
datasets: [{
label: "Sales",
data: [12000,15000,18000,17000,22000,25000,27000,30000,35000,40000,45000,50000],
borderWidth: 3
}]
}
});

// Category Sales

new Chart(document.getElementById("categoryChart"), {
type: "bar",
data: {
labels: ["Furniture","Office Supplies","Technology"],
datasets: [{
label: "Sales",
data: [45000,65000,85000]
}]
}
});

// Region Sales

new Chart(document.getElementById("regionChart"), {
type: "pie",
data: {
labels: ["West","East","South","Central"],
datasets: [{
data: [35,30,20,15]
}]
}
});

// Profit

new Chart(document.getElementById("profitChart"), {
type: "bar",
data: {
labels: ["Furniture","Office Supplies","Technology"],
datasets: [{
label: "Profit",
data: [12000,18000,28000]
}]
}
});
