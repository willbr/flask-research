from flask import Flask, render_template, jsonify, make_response
import csv
import io

app = Flask(__name__)

# Sample data for CSV
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')  # This will serve the HTML file

# Route to serve CSV data
@app.route('/csv', methods=['GET'])
def get_csv_data():
    # Create an in-memory CSV file
    csv_file = io.StringIO()
    csv_writer = csv.DictWriter(csv_file, fieldnames=["name", "age", "city"])
    csv_writer.writeheader()
    csv_writer.writerows(data)
    
    # Create a response and set the correct headers for a CSV file download
    response = make_response(csv_file.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    response.headers['Content-Type'] = 'text/csv'
    return response

if __name__ == '__main__':
    app.run(debug=True)

