#!/usr/bin/env python
"""Simple script to run the Flask server for runtime testing."""

from ivr_phone_tree_python import app

if __name__ == "__main__":
    print("Starting Flask server on http://0.0.0.0:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
