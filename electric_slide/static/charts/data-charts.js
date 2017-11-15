
function getStateDistributionData(callback) {
    $.get('/api/state-distribution').then(callback)
}


function buildStateDistributionChart(rawData) {

    let ctx = document.getElementById('statesChart').getContext('2d');

    let chart = new Chart(ctx, {
        type: 'line',

        data: {
            labels: Object.keys(rawData),
            datasets: [{
                data: Object.values(rawData), 
                borderColor: 'rgb(227, 27, 38)'
            }]
        },

        options: {
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    type: 'linear',
                    gridLines: {
                        drawOnChartArea: false,
                        color: 'rgb(251, 136, 131)'
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'States',
                        fontFamily: "'Josefin Slab', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
                        fontSize: 20
                    }
                }],
                xAxes: [{
                    gridLines: {
                        drawOnChartArea: false,
                        color: 'rgb(251, 136, 131)'
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Number of Moves from Solution',
                        fontFamily: "'Josefin Slab', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
                        fontSize: 20
                    }
                }]
            }
        }

    });

}