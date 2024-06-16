import logging
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# Routes and other Flask configurations


# CORS(app, resources={r"/*": {"origins": "*"}}) 
# allows requests from any origin (*). 
# This is suitable for development but should 
# be restricted to specific origins (http://localhost:3000 for your Next.js frontend) 
# in production for security reasons.
CORS(app, resources={r"/*": {"origins": "*"}})

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Counter variable
counter = 0

@app.route('/increment_counter', methods=['POST', 'OPTIONS'])
def increment_counter():
    if request.method == 'OPTIONS':
        # Set CORS headers for the preflight request
        headers = {
            'Access-Control-Allow-Origin': '*',  # Replace with your frontend URL
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
        return '', 200, headers

    global counter
    # app.logger.info('Request data: %s', request.get_data())
    app.logger.info('Request headers: %s', request.headers)
    # app.logger.info('Request JSON data: %s', request.json)
    # Increment the counter
    counter += 1
    # Return the updated count
    response = jsonify({'count': counter})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response, 200

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0') ensures that the Flask server binds to all network interfaces within the Docker container.
    app.run(debug=True, host='0.0.0.0')
