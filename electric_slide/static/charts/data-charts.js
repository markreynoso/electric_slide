
function populateCharts() {
    axisSettings = {
        gridLines: {
            drawOnChartArea: false,
            color: 'rgb(251, 136, 131)'
        },
        scaleLabel: {
            display: true,
            fontFamily: "'Josefin Slab', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
            fontSize: 20
        },
        ticks: {
            fontFamily: "'Open Sans', 'Helvetica', 'Arial', sans-serif"
        }
    }
    Chart.scaleService.updateScaleDefaults('linear', axisSettings)
    Chart.scaleService.updateScaleDefaults('category', axisSettings)
    getStateDistributionData(buildStateDistributionChart)
    buildScatterChart({},'timeChart', 'Time (ms)')
}


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
                    scaleLabel: {
                        labelString: 'States',
                    }
                }],
                xAxes: [{
                    scaleLabel: {
                        labelString: 'Number of Moves from Solution',
                    }
                }]
            }
        }

    });

}

function buildScatterChart(rawData, chartId, yAxisLabel) {

    let ctx = document.getElementById(chartId).getContext('2d');

    let chart = new Chart(ctx, {
        type: 'scatter',

        data: {
            datasets: [{
                label: 'Greedy Algoritm',
                fill: false,
                showLine: false,
                borderColor: 'rgb(0, 0, 0)',
                backgroundColor: 'rgb(0, 0, 0)',
                pointStyle: 'rect',
                radius: 4,
                data: [{
                    x: 10, y: 2
                },{
                    x: 4, y: 3
                },{
                    x: 5, y: 9
                },{
                    x: 2, y: 1
                }]
            }, {
                label: 'A* Algoritm',
                fill: false,
                showLine: false,
                borderColor: 'rgb(227, 27, 38)',
                pointStyle: 'circle',
                radius: 4,
                data: [{
                    x: 1, y: 3
                },{
                    x: 4, y: 4
                },{
                    x: 5, y: 2
                },{
                    x: 2, y: 0
                }]
            }, {
                label: 'Machine Learning',
                fill: false,
                showLine: false,
                borderColor: 'rgb(227, 27, 38)',
                backgroundColor: 'rgb(227, 27, 38)',
                pointStyle: 'star',
                radius: 4,
                data: [{
                    x: 10, y: 3
                },{
                    x: 4, y: 9
                },{
                    x: 5, y: 2
                },{
                    x: 2, y: 10
                }]
            }]
        },

        options: {
            legend: {
                position: 'bottom',
                labels: {
                    fontFamily: "'Open Sans', 'Helvetica', 'Arial', sans-serif",
                    fontSize: 15,
                    usePointStyle: true,
                    padding: 30
                }
            },
            scales: {
                yAxes: [{
                    type: 'linear',
                    scaleLabel: {
                        labelString: yAxisLabel,
                    }
                }],
                xAxes: [{
                    type: 'linear',
                    display: 'bottom',
                    scaleLabel: {
                        labelString: 'Number of Moves from Solution',
                    }
                }]
            }
        }

    });
}