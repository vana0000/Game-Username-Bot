from flask import Flask, request, jsonify
from flask_cors import CORS
from UsernameLogic.get_profile import get_player_by_ign  # Import the function you created

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from different origins (like React frontend)

# Endpoint for checking username availability
@app.route("/api/check-availability", methods=['POST'])
def check_availability():
    data = request.json
    usernames = data.get('usernames')  # Get the usernames from the request

    if not usernames:
        return jsonify({"error": "Usernames are required"}), 400  # Return error if usernames are missing

    # Split usernames if they are provided as a single string separated by commas
    if isinstance(usernames, str):
        usernames = [username.strip() for username in usernames.split(',')]

    # Prepare a response dictionary to store results for each username
    results = {}
    for username in usernames:
        results[username] = get_player_by_ign(username)

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
