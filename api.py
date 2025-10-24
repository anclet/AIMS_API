# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from db import aims_db
# import os

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all origins

# @app.route('/data/', methods=['GET', 'POST'])
# def get_data():
#     """
#     Single gateway endpoint to fetch any information from AIMS database
    
#     Query Parameter (GET) or JSON Body (POST):
#     - path: Dot notation path to specific data (e.g., 'about_aims.mission' or 'faculty_and_staff.senior_faculty.0.name')
    
#     Path format:
#     - Dictionary keys: separated by dots (e.g., 'about_aims.mission')
#     - List indices: numeric values (e.g., 'programs.0.name' for first program's name)
#     - Mixed: 'faculty_and_staff.senior_faculty.0.expertise.2' for third expertise of first senior faculty
#     """
#     try:
#         # Get path parameter from query string (GET) or JSON body (POST)
#         if request.method == 'POST':
#             data = request.get_json() or {}
#             path_str = data.get('path')
#         else:
#             path_str = request.args.get('path')
        
#         # If no path provided, return entire database
#         if not path_str:
#             return jsonify({
#                 "status": "success",
#                 "message": "AIMS Rwanda Database - Full Data",
#                 "data": aims_db,
#                 "usage": "Add ?path=section_name to get specific data (e.g., ?path=about_aims.mission)"
#             })
        
#         # Split path and traverse the database
#         tokens = path_str.split('.')
#         current = aims_db
        
#         for token in tokens:
#             if isinstance(current, dict):
#                 if token in current:
#                     current = current[token]
#                 else:
#                     return jsonify({
#                         "status": "error",
#                         "message": f"Key '{token}' not found",
#                         "path": path_str,
#                         "available_keys": list(current.keys()) if isinstance(current, dict) else None
#                     }), 404
#             elif isinstance(current, list):
#                 try:
#                     index = int(token)
#                     if 0 <= index < len(current):
#                         current = current[index]
#                     else:
#                         return jsonify({
#                             "status": "error",
#                             "message": f"Index {index} out of range",
#                             "path": path_str,
#                             "list_length": len(current)
#                         }), 404
#                 except ValueError:
#                     return jsonify({
#                         "status": "error",
#                         "message": f"Expected integer index for list, got '{token}'",
#                         "path": path_str,
#                         "list_length": len(current)
#                     }), 404
#             else:
#                 # Current is a scalar and we have more tokens -> error
#                 return jsonify({
#                     "status": "error",
#                     "message": f"Cannot traverse into {type(current).__name__} at token '{token}'",
#                     "path": path_str,
#                     "current_type": type(current).__name__,
#                     "current_value": current
#                 }), 404
        
#         # Successfully traversed, return the result
#         return jsonify({
#             "status": "success",
#             "path": path_str,
#             "data": current,
#             "type": type(current).__name__
#         })
        
#     except Exception as e:
#         return jsonify({
#             "status": "error",
#             "message": f"Server error: {str(e)}",
#             "path": path_str if 'path_str' in locals() else None
#         }), 500

# @app.errorhandler(404)
# def not_found(error):
#     return jsonify({
#         "status": "error",
#         "message": "Endpoint not found",
#         "available_endpoint": "/data/"
#     }), 404

# @app.errorhandler(405)
# def method_not_allowed(error):
#     return jsonify({
#         "status": "error",
#         "message": "Method not allowed. Use GET or POST",
#         "allowed_methods": ["GET", "POST"]
#     }), 405

# @app.errorhandler(500)
# def internal_error(error):
#     return jsonify({
#         "status": "error",
#         "message": "Internal server error"
#     }), 500


# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 10000))
#     app.run(host='0.0.0.0', port=port)

import os
import requests
import threading
import time
from flask import Flask, jsonify, request
from flask_cors import CORS
from db import aims_db

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins


# ---------------------------
# Background Sync (Every 5 min)
# ---------------------------
def background_sync():
    """Runs automatically every 5 minutes to keep service warm and log activity"""
    while True:
        try:
            print("🔄 Starting scheduled synchronization...")

            # Step 1: Ping Render app (keep warm)
            render_url = os.getenv("RENDER_EXTERNAL_URL", "https://your-aims-db-app.onrender.com")
            try:
                response = requests.get(f"{render_url}/health", timeout=10)
                if response.status_code == 200:
                    print("✅ Self-ping successful - service is warm")
                else:
                    print(f"⚠️ Self-ping returned status {response.status_code}")
            except requests.exceptions.RequestException as ping_error:
                print(f"⚠️ Self-ping failed: {ping_error}")

            # Step 2: Log database statistics
            total_sections = len(aims_db.keys())
            print(f"📊 Database contains {total_sections} main sections")

            # Step 3: Optional - Save activity log
            logs_dir = os.path.join(os.getcwd(), "logs")
            os.makedirs(logs_dir, exist_ok=True)
            log_file = os.path.join(logs_dir, "sync_log.txt")

            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"\n[SYNC @ {time.ctime()}]\n")
                f.write(f"• Database sections: {total_sections}\n")
                f.write(f"• Service status: healthy\n")

            print("📝 Activity logged successfully.")

        except Exception as e:
            print(f"⚠️ Sync error: {e}")

        # Wait 5 minutes before next sync
        time.sleep(300)  # 300 seconds = 5 minutes


def start_background_thread():
    """Start sync task in a background thread"""
    thread = threading.Thread(target=background_sync, daemon=True)
    thread.start()
    print("🚀 Background sync thread started (runs every 5 minutes)")


# ---------------------------
# Routes
# ---------------------------
@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "database_sections": len(aims_db.keys()),
        "message": "AIMS DB API is running"
    }), 200


@app.route('/', methods=['GET'])
def home():
    """Root endpoint"""
    return jsonify({
        "message": "🎉 AIMS Rwanda Database API is live!",
        "usage": "Use /data/?path=section_name to get specific data",
        "example": "/data/?path=about_aims.mission",
        "health_check": "/health"
    }), 200


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


# ---------------------------
# Error Handlers
# ---------------------------
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Endpoint not found",
        "available_endpoints": ["/", "/health", "/data/"]
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


# ---------------------------
# Run Flask App
# ---------------------------
if __name__ == '__main__':
    # Start background sync thread
    start_background_thread()
    
    # Start Flask app
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

