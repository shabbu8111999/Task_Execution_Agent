from flask import Blueprint, jsonify, request
from taskExecutor.agent_controller import run_task_agent

task_routes = Blueprint("task_routes", __name__)


@task_routes.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Task Execution Agent is running."})

@task_routes.route("/run-agent", methods = ["POST"])
def run_agent():
    data = request.get_json()
    task = data.get("task")


    if not task:
        return jsonify({"error" : "Task Description required"}), 400
    

    try:
        result = run_task_agent(task)
        return jsonify({'result' : result}), 200
    
    except Exception as e:
        return jsonify({"error" : str(e)}), 500