import psycopg2
import json

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="chart_data",   # Replace with your database name
    user="postgres",   # Replace with your username
    password="vision",   # Replace with your password
    host="localhost",       # Replace with your host if different
    port="5432"             # Default PostgreSQL port
)

# Create a cursor to interact with the database
cur = conn.cursor()

# Query to fetch sales data
cur.execute("SELECT month, sales FROM sales_data")

# Fetch all rows from the query result
rows = cur.fetchall()

# Close the database connection
cur.close()
conn.close()

# Prepare data for Chart.js
months = [row[0] for row in rows]
sales = [row[1] for row in rows]

# Create the data dictionary for Chart.js
data = {
    "labels": months,
    "datasets": [
        {
            "label": "Sales",
            "data": sales,
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
