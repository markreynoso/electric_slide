
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
                borderColor: 'rgb(227, 27, 38)',
                borderWidth: 2,
                pointBorderWidth: 1
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
        allMoves = rawData[c]['tree']['time']
        if (c == '0') {
            data.push({x:c, y:allMoves[0].toFixed(3)})
            data.push({x:c, y:allMoves[0].toFixed(3)})
            data.push({x:c, y:allMoves[0].toFixed(3)})
            data.push({x:c, y:NaN})
        } else {
            data.push({x:c, y:mean(allMoves).toFixed(3)})
            data.push({x:c, y:topQuartile(allMoves).toFixed(3)})
            data.push({x:c, y:bottomQuartile(allMoves).toFixed(3)})
            data.push({x:c, y:NaN})
        }
        return data
    }, [])
    treeDataPoints = complexities.reduce((points, c) => {
        points.push('star')
        points.push('line')
        points.push('line')
        points.push('line')
        return points
    }, [])

    aStarData = complexities.reduce((data, c) => {
        allMoves = rawData[c]['a_star']['time']
        if (c == '0') {
            data.push({x:c, y:allMoves[0].toFixed(3)})
            data.push({x:c, y:allMoves[0].toFixed(3)})
            data.push({x:c, y:allMoves[0].toFixed(3)})
            data.push({x:c, y:NaN})
        } else {
            data.push({x:c, y:mean(allMoves).toFixed(3)})
            data.push({x:c, y:topQuartile(allMoves).toFixed(3)})
            data.push({x:c, y:bottomQuartile(allMoves).toFixed(3)})
            data.push({x:c, y:NaN})
        }
        return data
    }, [])
    aStarDataPoints = complexities.reduce((points, c) => {
        points.push('circle')
        points.push('line')
        points.push('line')
        points.push('line')
        return points
    }, [])

    greedyData = complexities.reduce((data, c) => {
        allMoves = rawData[c]['greedy']['time']
        if (c == '0') {
            data.push({x:c, y:allMoves[0].toFixed(3)})
            data.push({x:c, y:allMoves[0].toFixed(3)})
            data.push({x:c, y:allMoves[0].toFixed(3)})
            data.push({x:c, y:NaN})
        } else {
            data.push({x:c, y:mean(allMoves).toFixed(3)})
            data.push({x:c, y:topQuartile(allMoves).toFixed(3)})
            data.push({x:c, y:bottomQuartile(allMoves).toFixed(3)})
            data.push({x:c, y:NaN})
        }
        return data
    }, [])
    greedyDataPoints = complexities.reduce((points, c) => {
        points.push('rectRot')
        points.push('line')
        points.push('line')
        points.push('line')
        return points
    }, [])

    let ctx = document.getElementById('timeChart').getContext('2d');

    let chart = new Chart(ctx, {
        type: 'scatter',

        data: {
            datasets: [{
                label: 'Greedy Algoritm',
                fill: false,
                borderWidth: 1,
                borderColor: 'rgb(0, 0, 0)',
                backgroundColor: 'rgb(0, 0, 0)',
                pointStyle: greedyDataPoints,
                radius: 4,
                data: greedyData,
                spanGaps: false
            }, {
                label: 'A* Algoritm',
                fill: false,
                borderWidth: 1,
                borderColor: 'rgb(227, 27, 38)',
                pointStyle: aStarDataPoints,
                radius: 4,
                data: aStarData,
                spanGaps: false
            }, {
                label: 'Decision Tree',
                fill: false,
                borderWidth: 1,
                borderColor: 'rgb(227, 27, 38)',
                backgroundColor: 'rgb(227, 27, 38)',
                pointStyle: treeDataPoints,
                radius: 4,
                data: treeData,
                spanGaps: false
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
            },
            elements: {
                line: {
                    tension: 0,
                }
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
        avg = mean(allMoves)
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
                borderWidth: 1,
                borderColor: 'rgb(0, 0, 0)',
                backgroundColor: 'rgb(0, 0, 0)',
                pointStyle: greedyDataPoints,
                radius: 4,
                data: greedyData,
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
            },
            elements: {
                line: {
                    tension: 0,
                }
            }
        }

    });
}

function mean(values) {
    return values.reduce((sum, n) => sum + n) / values.length
}

function topQuartile(values) {
    middle = mean(values)
    topHalf = values.filter(n => n > middle)
    return mean(topHalf)
}

function bottomQuartile(values) {
    middle = mean(values)
    bottomHalf = values.filter(n => n < middle)
    return mean(bottomHalf)
}