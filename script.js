new Chart(document.getElementById("salesChart"), {
type: "line",
data: {
labels: ["Jan","Feb","Mar","Apr","May","Jun"],
datasets: [{
label: "Sales",
data: [12000,19000,15000,25000,22000,30000]
}]
}
});

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

new Chart(document.getElementById("regionChart"), {
type: "pie",
data: {
labels: ["East","West","South","Central"],
datasets: [{
data: [25,35,20,20]
}]
}
});

new Chart(document.getElementById("profitChart"), {
type: "bar",
data: {
labels: ["Furniture","Office Supplies","Technology"],
datasets: [{
label: "Profit",
data: [5000,12000,18000]
}]
}
});
