from flask import Flask, jsonify, request
from flask_cors import CORS
from db import aims_db
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

@app.route('/data/', methods=['GET', 'POST'])
def get_data():
    """
    Single gateway endpoint to fetch any information from AIMS database
    
    Query Parameter (GET) or JSON Body (POST):
    - path: Dot notation path to specific data (e.g., 'about_aims.mission' or 'faculty_and_staff.senior_faculty.0.name')
    
    Path format:
    - Dictionary keys: separated by dots (e.g., 'about_aims.mission')
    - List indices: numeric values (e.g., 'programs.0.name' for first program's name)
    - Mixed: 'faculty_and_staff.senior_faculty.0.expertise.2' for third expertise of first senior faculty
    """
    try:
        # Get path parameter from query string (GET) or JSON body (POST)
        if request.method == 'POST':
            data = request.get_json() or {}
            path_str = data.get('path')
        else:
            path_str = request.args.get('path')
        
        # If no path provided, return entire database
        if not path_str:
            return jsonify({
                "status": "success",
                "message": "AIMS Rwanda Database - Full Data",
                "data": aims_db,
                "usage": "Add ?path=section_name to get specific data (e.g., ?path=about_aims.mission)"
            })
        
        # Split path and traverse the database
        tokens = path_str.split('.')
        current = aims_db
        
        for token in tokens:
            if isinstance(current, dict):
                if token in current:
                    current = current[token]
                else:
                    return jsonify({
                        "status": "error",
                        "message": f"Key '{token}' not found",
                        "path": path_str,
                        "available_keys": list(current.keys()) if isinstance(current, dict) else None
                    }), 404
            elif isinstance(current, list):
                try:
                    index = int(token)
                    if 0 <= index < len(current):
                        current = current[index]
                    else:
                        return jsonify({
                            "status": "error",
                            "message": f"Index {index} out of range",
                            "path": path_str,
                            "list_length": len(current)
                        }), 404
                except ValueError:
                    return jsonify({
                        "status": "error",
                        "message": f"Expected integer index for list, got '{token}'",
                        "path": path_str,
                        "list_length": len(current)
                    }), 404
            else:
                # Current is a scalar and we have more tokens -> error
                return jsonify({
                    "status": "error",
                    "message": f"Cannot traverse into {type(current).__name__} at token '{token}'",
                    "path": path_str,
                    "current_type": type(current).__name__,
                    "current_value": current
                }), 404
        
        # Successfully traversed, return the result
        return jsonify({
            "status": "success",
            "path": path_str,
            "data": current,
            "type": type(current).__name__
        })
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Server error: {str(e)}",
            "path": path_str if 'path_str' in locals() else None
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Endpoint not found",
        "available_endpoint": "/data/"
    }), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "status": "error",
        "message": "Method not allowed. Use GET or POST",
        "allowed_methods": ["GET", "POST"]
    }), 405

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
