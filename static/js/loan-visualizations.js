const canvas = document.getElementById('myChart')

const chartSelectDropdown = document.getElementById('chartSelect')

chartSelectDropdown.addEventListener('change', function() {
    Chart.getChart(canvas).destroy();
    new Chart(canvas, {
        type: window.chartData[this.value].type,
        data: {
          labels: window.chartData[this.value].labels,
          datasets: [{
            label: window.chartData[this.value].title,
            data: window.chartData[this.value].values,
            borderWidth: 1
          }]
        },
        options: {
            responsive: true,
            scales: window.chartData[this.value].type !== 'pie' ?
                {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            precision: 0
                        }
                    }
                } : {}
        }

    });

});

new Chart(canvas, {
    type: window.chartData[chartSelectDropdown.value].type,
        data: {
          labels: window.chartData[chartSelectDropdown.value].labels,
          datasets: [{
            label: window.chartData[chartSelectDropdown.value].title,
            data: window.chartData[chartSelectDropdown.value].values,
            borderWidth: 1
          }]
        },
    options: {
      responsive: true
    }
});