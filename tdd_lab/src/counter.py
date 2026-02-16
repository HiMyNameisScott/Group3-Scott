"""
Counter API Implementation
"""
from flask import Flask, jsonify
from . import status

app = Flask(__name__)

COUNTERS = {}

@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    if counter_exists(name):
        return jsonify({"error": f"Counter {name} already exists"}), status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return jsonify({name: COUNTERS[name]}), status.HTTP_201_CREATED

def counter_exists(name):
    return name in COUNTERS


# Failing Test

def test_prevent_duplicate_counters(self, client):
    """It should not allow creating a duplicate counter"""
    # Create it once
    result1 = client.post("/counters/foo")
    assert result1.status_code == status.HTTP_201_CREATED

    # Create it again (should fail)
    result2 = client.post("/counters/foo")
    assert result2.status_code == status.HTTP_409_CONFLICT

def prevent_dupe_counter(name):
    if counter_exists(name):
        return jsonify({"error": f"Counter {name} already exists"}), status.HTTP_409_CONFLICT
    return None