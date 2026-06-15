// Gender Distribution

new Chart(document.getElementById("genderChart"), {

    type: "doughnut",

    data: {
        labels: ["Male", "Female"],
        datasets: [{
            data: [48, 52],

            backgroundColor: [
                "#7b2cbf",
                "#ff4d9d"
            ],

            borderWidth: 0
        }]
    },

    options: {
        responsive: true,
        plugins: {
            legend: {
                labels: {
                    color: "white"
                }
            }
        }
    }

});


// Subject Performance

new Chart(document.getElementById("subjectChart"), {

    type: "bar",

    data: {
        labels: ["Math", "Reading", "Writing"],

        datasets: [{
            label: "Average Score",

            data: [78, 82, 80],

            backgroundColor: [
                "#7b2cbf",
                "#c77dff",
                "#ff4d9d"
            ]
        }]
    },

    options: {
        scales: {
            y: {
                ticks: {
                    color: "white"
                },
                grid: {
                    color: "#1f4e79"
                }
            },
            x: {
                ticks: {
                    color: "white"
                },
                grid: {
                    color: "#1f4e79"
                }
            }
        },

        plugins: {
            legend: {
                labels: {
                    color: "white"
                }
            }
        }
    }

});


// Attendance Trend

new Chart(document.getElementById("attendanceChart"), {

    type: "line",

    data: {
        labels: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ],

        datasets: [{
            label: "Attendance %",

            data: [
                75,
                80,
                78,
                85,
                88,
                90
            ],

            borderColor: "#00abf0",

            backgroundColor: "#00abf0",

            tension: 0.4,

            fill: false
        }]
    },

    options: {
        scales: {
            y: {
                ticks: {
                    color: "white"
                },
                grid: {
                    color: "#1f4e79"
                }
            },
            x: {
                ticks: {
                    color: "white"
                },
                grid: {
                    color: "#1f4e79"
                }
            }
        },

        plugins: {
            legend: {
                labels: {
                    color: "white"
                }
            }
        }
    }

});


// Parent Education

new Chart(document.getElementById("educationChart"), {

    type: "pie",

    data: {

        labels: [
            "High School",
            "Bachelor",
            "Master",
            "PhD"
        ],

        datasets: [{

            data: [
                35,
                30,
                20,
                15
            ],

            backgroundColor: [
                "#7b2cbf",
                "#9d4edd",
                "#ff4d9d",
                "#00abf0"
            ]
        }]
    },

    options: {

        plugins: {
            legend: {
                labels: {
                    color: "white"
                }
            }
        }

    }

});
