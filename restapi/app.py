from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data with unique IDs
data = [
    {"id": 1, "name": "Alice", "age": 30, "city": "New York"},
    {"id": 2, "name": "Bob", "age": 25, "city": "Los Angeles"},
    {"id": 3, "name": "Charlie", "age": 35, "city": "Chicago"}
]

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')  # This will serve the HTML file

# Route to return column-oriented JSON data with IDs
@app.route('/json', methods=['GET'])
def get_json_data():
    # Transforming the data into column-oriented format
    column_oriented_data = {
        "id": [row['id'] for row in data],
        "name": [row['name'] for row in data],
        "age": [row['age'] for row in data],
        "city": [row['city'] for row in data]
    }
    return jsonify(column_oriented_data)

# Second API that takes an ID and returns more details for that person
@app.route('/details/<int:id>', methods=['GET'])
def get_details(id):
    # Dummy detailed data
    detailed_data = next((item for item in data if item["id"] == id), None)
    if detailed_data:
        return jsonify(detailed_data)
    else:
        return jsonify({"error": "Data not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

