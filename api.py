
# api.py
# from flask import Flask, request, jsonify
# from db import aims_db

# app = Flask(__name__)

# @app.route("/data/", methods=["POST"])
# def get_data():
#     try:
#         data = request.get_json()
#         query_type = data.get("query_type", "about_aims")

#         # About AIMS Information
#         if query_type == "about_aims":
#             return jsonify({"status": "success", "data": aims_db["about_aims"]})
        
#         elif query_type == "mission":
#             return jsonify({"status": "success", "data": {
#                 "mission": aims_db["about_aims"]["mission"],
#                 "vision": aims_db["about_aims"]["vision"]
#             }})
        
#         elif query_type == "values":
#             return jsonify({"status": "success", "data": aims_db["about_aims"]["values"]})
        
#         elif query_type == "campus_info":
#             return jsonify({"status": "success", "data": aims_db["about_aims"]["campus_info"]})
        
#         elif query_type == "achievements":
#             return jsonify({"status": "success", "data": aims_db["about_aims"]["key_achievements"]})

#         # Leadership Information
#         elif query_type == "leadership":
#             return jsonify({"status": "success", "data": aims_db["leadership"]})
        
#         elif query_type == "president":
#             return jsonify({"status": "success", "data": aims_db["leadership"]["centre_president"]})
        
#         elif query_type == "research_president":
#             return jsonify({"status": "success", "data": aims_db["leadership"]["research_and_innovation_president"]})
        
#         elif query_type == "academic_director":
#             return jsonify({"status": "success", "data": aims_db["leadership"]["academic_director"]})

#         # Faculty and Staff Information
#         elif query_type == "faculty":
#             return jsonify({"status": "success", "data": aims_db["faculty_and_staff"]})
        
#         elif query_type == "senior_faculty":
#             return jsonify({"status": "success", "data": aims_db["faculty_and_staff"]["senior_faculty"]})
        
#         elif query_type == "academic_staff":
#             return jsonify({"status": "success", "data": aims_db["faculty_and_staff"]["academic_staff"]})
        
#         elif query_type == "industry_initiative":
#             return jsonify({"status": "success", "data": aims_db["faculty_and_staff"]["industry_initiative"]})

#         # Programs Information
#         elif query_type == "programs":
#             return jsonify({"status": "success", "data": aims_db["programs"]})
        
#         elif query_type == "program_id":
#             program_id = data.get("program_id")
#             if not program_id:
#                 return jsonify({"status": "error", "message": "Missing 'program_id'"}), 400
#             program = next((p for p in aims_db["programs"] if p["program_id"] == program_id), None)
#             if program:
#                 return jsonify({"status": "success", "data": program})
#             else:
#                 return jsonify({"status": "error", "message": "Program not found"}), 404

#         # Research Information
#         elif query_type == "research":
#             return jsonify({"status": "success", "data": aims_db["research"]})
        
#         elif query_type == "research_focus":
#             return jsonify({"status": "success", "data": aims_db["research"]["research_focus"]})
        
#         elif query_type == "research_entities":
#             return jsonify({"status": "success", "data": aims_db["research"]["research_entities"]})
        
#         elif query_type == "specialized_research":
#             return jsonify({"status": "success", "data": aims_db["research"]["specialized_research_areas"]})

#         # Initiatives Information
#         elif query_type == "initiatives":
#             return jsonify({"status": "success", "data": aims_db["initiatives"]})
        
#         elif query_type == "eureka_mu_rugo":
#             return jsonify({"status": "success", "data": aims_db["initiatives"]["eureka_mu_rugo"]})
        
#         elif query_type == "next_einstein_forum":
#             return jsonify({"status": "success", "data": aims_db["initiatives"]["next_einstein_forum"]})
        
#         elif query_type == "quantum_leap_africa":
#             return jsonify({"status": "success", "data": aims_db["initiatives"]["quantum_leap_africa"]})
        
#         elif query_type == "teacher_training":
#             return jsonify({"status": "success", "data": aims_db["initiatives"]["teacher_training_program"]})

#         # Students and Alumni Information
#         elif query_type == "students":
#             return jsonify({"status": "success", "data": aims_db["students"]})
        
#         elif query_type == "alumni":
#             return jsonify({"status": "success", "data": aims_db["alumni"]})
        
#         elif query_type == "staff":
#             return jsonify({"status": "success", "data": aims_db["staff"]})

#         # Partnerships and Governance
#         elif query_type == "partners":
#             return jsonify({"status": "success", "data": aims_db["partners"]})
        
#         elif query_type == "governance":
#             return jsonify({"status": "success", "data": aims_db["governance"]})

#         # Calendar and Events
#         elif query_type == "calendar":
#             return jsonify({"status": "success", "data": aims_db["calendar"]})
        
#         elif query_type == "events":
#             return jsonify({"status": "success", "data": aims_db["calendar"]["events"]})

#         # Contact Information
#         elif query_type == "contact":
#             return jsonify({"status": "success", "data": aims_db["contact"]})

#         # Statistics
#         elif query_type == "statistics":
#             stats = {
#                 "total_students_trained": aims_db["students"]["total_trained"],
#                 "women_participation": aims_db["students"]["women_participation_rate"],
#                 "total_graduates_network": aims_db["alumni"]["total_graduates"],
#                 "established_year": aims_db["about_aims"]["established"],
#                 "total_programs": len(aims_db["programs"]),
#                 "research_areas": len(aims_db["research"]["research_focus"]),
#                 "initiatives_count": len(aims_db["initiatives"]),
#                 "partners_count": len(aims_db["partners"])
#             }
#             return jsonify({"status": "success", "data": stats})

#         # Search functionality
#         elif query_type == "search":
#             search_query = data.get("search_query", "").lower()
#             if not search_query:
#                 return jsonify({"status": "error", "message": "Missing 'search_query'"}), 400
            
#             results = []
            
#             # Search in programs
#             for program in aims_db["programs"]:
#                 if (search_query in program["name"].lower() or 
#                     search_query in program["description"].lower() or
#                     any(search_query in fa.lower() for fa in program["focus_areas"])):
#                     results.append({"type": "program", "data": program})
            
#             # Search in research areas
#             for area in aims_db["research"]["research_focus"]:
#                 if search_query in area.lower():
#                     results.append({"type": "research_area", "data": area})
            
#             # Search in initiatives
#             for key, initiative in aims_db["initiatives"].items():
#                 if (search_query in initiative["name"].lower() or 
#                     search_query in initiative.get("philosophy", "").lower()):
#                     results.append({"type": "initiative", "data": initiative})
            
#             return jsonify({"status": "success", "data": results, "total_results": len(results)})

#         # Faculty search by name
#         elif query_type == "faculty_search":
#             faculty_name = data.get("faculty_name", "").lower()
#             if not faculty_name:
#                 return jsonify({"status": "error", "message": "Missing 'faculty_name'"}), 400
            
#             # Search in leadership
#             for key, leader in aims_db["leadership"].items():
#                 if faculty_name in leader["name"].lower():
#                     return jsonify({"status": "success", "data": leader})
            
#             # Search in faculty and staff
#             for faculty_type in aims_db["faculty_and_staff"].values():
#                 if isinstance(faculty_type, list):
#                     for member in faculty_type:
#                         if faculty_name in member["name"].lower():
#                             return jsonify({"status": "success", "data": member})
            
#             return jsonify({"status": "error", "message": "Faculty member not found"}), 404

#         # Program search by focus area
#         elif query_type == "programs_by_focus":
#             focus_area = data.get("focus_area", "").lower()
#             if not focus_area:
#                 return jsonify({"status": "error", "message": "Missing 'focus_area'"}), 400
            
#             matching_programs = []
#             for program in aims_db["programs"]:
#                 if any(focus_area in fa.lower() for fa in program["focus_areas"]):
#                     matching_programs.append(program)
            
#             return jsonify({"status": "success", "data": matching_programs, "total_programs": len(matching_programs)})

#         # All data (use with caution)
#         elif query_type == "all_data":
#             return jsonify({"status": "success", "data": aims_db})

#         else:
#             return jsonify({"status": "error", "message": "Unknown query_type"}), 400

#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, jsonify, request
from flask_cors import CORS
from db import aims_db

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
    app.run(debug=True)