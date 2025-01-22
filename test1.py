import json

# Create some data
data = {
    "labels": ["January", "February", "March", "April", "May"],
    "datasets": [
        {
            "label": "Sales",
            "data": [30, 40, 55, 70, 60],
            "backgroundColor": "rgba(75, 192, 192, 0.2)",
            "borderColor": "rgba(75, 192, 192, 1)",
            "borderWidth": 1
        }
    ]
}

# Convert data to JSON format
data_json = json.dumps(data)

# Create the HTML with Chart.js code
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chart.js Example</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <canvas id="myChart" width="400" height="200"></canvas>
    <script>
        const ctx = document.getElementById('myChart').getContext('2d');
        const data = {data_json};
        new Chart(ctx, {{
            type: 'bar',
            data: data,
            options: {{
                scales: {{
                    y: {{
                        beginAtZero: true
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""

# Write the HTML content to a file
with open("chart_example.html", "w") as f:
    f.write(html_content)

print("HTML file created successfully with Chart.js visualization.")
