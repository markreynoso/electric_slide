
function getStateDistributionData(callback) {
    $.get('/api/state-distribution').then(callback)
}


function buildStateDistributionChart(rawData) {

    let ctx = document.getElementById('statesChart').getContext('2d');

    let chart = new Chart(ctx, {
        type: 'line',

        data: {
            labels: [1,2,3,4,5,6,7,8,9,10],
            datasets: [{
                data: [0,3,6,2,1,7,8,2,12,4], 
                borderColor: 'rgb(227, 27, 38)'
            }]
        },

        options: {
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
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