from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')  # This will serve the HTML file

# Route to return column-oriented JSON data
@app.route('/json', methods=['GET'])
def get_json_data():
    # Transforming the data into column-oriented format
    column_oriented_data = {
        "name": [row['name'] for row in data],
        "age": [row['age'] for row in data],
        "city": [row['city'] for row in data]
    }
    return jsonify(column_oriented_data)

if __name__ == '__main__':
    app.run(debug=True)
