const API_URL = 'http://127.0.0.1:8000';
const display = document.getElementById('display');
let chartInstance = null;

function appendValue(val) {
    if (display.value === 'Error') display.value = '';
    display.value += val;
}

function clearDisplay() {
    display.value = '';
}

async function calculate() {
    const expr = display.value;
    if (!expr) return;
    
    try {
        const response = await fetch(`${API_URL}/calculate`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ expression: expr })
        });
        
        const data = await response.json();
        if (response.ok) {
            display.value = data.result;
        } else {
            display.value = 'Error';
            console.error(data.detail);
        }
    } catch (e) {
        display.value = 'Error';
        console.error('Failed to connect to backend', e);
    }
}

async function plotGraph() {
    const eq = document.getElementById('graph-eq').value;
    if (!eq) return;

    try {
        const response = await fetch(`${API_URL}/graph`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ equation: eq })
        });
        
        const data = await response.json();
        if (response.ok) {
            renderChart(eq, data.x, data.y);
        } else {
            alert('Error generating graph: ' + data.detail);
        }
    } catch (e) {
        alert('Failed to connect to backend');
        console.error(e);
    }
}

function renderChart(label, xData, yData) {
    const ctx = document.getElementById('graphCanvas').getContext('2d');
    
    if (chartInstance) {
        chartInstance.destroy();
    }
    
    chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
            labels: xData.map(x => x.toFixed(2)),
            datasets: [{
                label: `y = ${label}`,
                data: yData,
                borderColor: '#007bff',
                borderWidth: 2,
                pointRadius: 0,
                fill: false,
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: { display: true, text: 'x' },
                    ticks: { maxTicksLimit: 10 }
                },
                y: {
                    title: { display: true, text: 'y' }
                }
            }
        }
    });
}
