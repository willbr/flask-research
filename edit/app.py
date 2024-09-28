
from flask import Flask, jsonify, request, render_template

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
    return render_template('index.html')

# Route to return column-oriented JSON data with IDs
@app.route('/json', methods=['GET'])
def get_json_data():
    column_oriented_data = {
        "id": [row['id'] for row in data],
        "name": [row['name'] for row in data],
        "age": [row['age'] for row in data],
        "city": [row['city'] for row in data]
    }
    return jsonify(column_oriented_data)

# Route to update the age of a user
@app.route('/update/<int:id>', methods=['PUT'])
def update_age(id):
    # Find the user by id
    user = next((item for item in data if item["id"] == id), None)
    if user:
        # Get the new age from the request data
        new_age = request.json.get('age', user['age'])
        user['age'] = new_age
        return jsonify({"message": "Age updated successfully", "user": user}), 200
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
