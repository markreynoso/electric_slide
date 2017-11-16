
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
    getSolvingData([buildTimeScatterChart, buildMovesScatterChart])
}


function getStateDistributionData(callback) {
    $.get('/api/data/states').then(callback)
}

function getSolvingData(callbacks) {
    $.get('/api/data/solve').then(data => callbacks.forEach(c => c(data)))
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

function buildTimeScatterChart(rawData) {
    complexities = Object.keys(rawData)
    treeData = complexities.reduce((data, c) => {
        for (let i = 0; i < rawData[c]['tree']['time'].length; i++) {
            data.push({x:c, y:rawData[c]['tree']['time'][i]})
        }
        return data
    }, [])
    aStarData = complexities.reduce((data, c) => {
        for (let i = 0; i < rawData[c]['a_star']['time'].length; i++) {
            if (rawData[c]['a_star']['time'][i] < 250000) {
                data.push({x:c, y:rawData[c]['a_star']['time'][i]})
            }
        }
        return data
    }, [])
    greedyData = complexities.reduce((data, c) => {
        for (let i = 0; i < rawData[c]['greedy']['time'].length; i++) {
            data.push({x:c, y:rawData[c]['greedy']['time'][i]})
        }
        return data
    }, [])

    let ctx = document.getElementById('timeChart').getContext('2d');

    let chart = new Chart(ctx, {
        type: 'scatter',

        data: {
            datasets: [{
                label: 'Greedy Algoritm',
                fill: false,
                showLine: false,
                borderColor: 'rgb(0, 0, 0)',
                backgroundColor: 'rgb(0, 0, 0)',
                pointStyle: 'rectRot',
                radius: 4,
                data: greedyData
            }, {
                label: 'A* Algoritm',
                fill: false,
                showLine: false,
                borderColor: 'rgb(227, 27, 38)',
                pointStyle: 'circle',
                radius: 4,
                data: aStarData
            }, {
                label: 'Decision Tree',
                fill: false,
                showLine: false,
                borderColor: 'rgb(227, 27, 38)',
                backgroundColor: 'rgb(227, 27, 38)',
                pointStyle: 'star',
                radius: 4,
                data: treeData
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
                        labelString: 'Time (ms)',
                    }
                }],
                xAxes: [{
                    ticks: {
                        max: 31,
                        stepSize: 1
                    },
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

function buildMovesScatterChart(rawData) {
    complexities = Object.keys(rawData)
    treeData = complexities.map(c => {
        return {x:c, y:rawData[c]['tree']['moves'][0]}
    })
    aStarData = complexities.map(c => {
        return {x:c, y:rawData[c]['a_star']['moves'][0]}
    })
    greedyData = complexities.reduce((data, c) => {
        allMoves = rawData[c]['greedy']['moves']
        for (let i = 0; i < allMoves.length; i++) {
            if (allMoves.indexOf(allMoves[i]) == i) {
                data.push({x:c, y:allMoves[i]})
            }
        }
        return data
    }, [])
    greedyDataAvg = complexities.reduce((data, c) => {
        allMoves = rawData[c]['greedy']['moves']
        avg = allMoves.reduce((sum, n) => sum + n) / allMoves.length
        data.push({x:c, y:avg.toFixed(3)})
        data.push({x:c, y:allMoves.reduce((a, b) => Math.min(a, b))})
        data.push({x:c, y:allMoves.reduce((a, b) => Math.max(a, b))})
        data.push({x:c, y:NaN})
        return data
    }, [])
    greedyDataPoints = complexities.reduce((points, c) => {
        points.push('rectRot')
        points.push('line')
        points.push('line')
        points.push('line')
        return points
    }, [])

    let ctx = document.getElementById('movesChart').getContext('2d');

    let chart = new Chart(ctx, {
        type: 'scatter',

        data: {
            datasets: [{
                label: 'Greedy Algoritm',
                fill: false,
                borderWidth: 2,
                borderColor: 'rgb(0, 0, 0)',
                backgroundColor: 'rgb(0, 0, 0)',
                pointStyle: greedyDataPoints,
                radius: 4,
                data: greedyDataAvg,
                spanGaps: false
            }, {
                label: 'A* Algoritm',
                fill: false,
                showLine: false,
                borderColor: 'rgb(227, 27, 38)',
                pointStyle: 'circle',
                radius: 4,
                data: aStarData
            }, {
                label: 'Decision Tree',
                fill: false,
                showLine: false,
                borderColor: 'rgb(227, 27, 38)',
                backgroundColor: 'rgb(227, 27, 38)',
                pointStyle: 'star',
                radius: 4,
                data: treeData
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
                        labelString: 'Number of Moves Taken',
                    }
                }],
                xAxes: [{
                    ticks: {
                        max: 31,
                        stepSize: 1
                    },
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