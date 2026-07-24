from flask import Flask, request, make_response, jsonify, render_template
from pip._internal.resolution.resolvelib import provider

from datetime import datetime
from posudba_service import add_posudba, patch_posudba
from knjiga_service import  get_knjige, add_knjiga


app = Flask(__name__)


@app.route("/")
def home():
  response = get_knjige()
  return render_template('index.html', knjige=response['data'])

@app.route("/knjige", methods=["GET"])
def vrati_knjige():
  response = get_knjige()

  if response["status"] == "Success":
    return make_response(jsonify(response), 200)

  return make_response(jsonify(response), 400)

@app.route("/knjiga", methods=["POST"])
def create_knjiga():
  try:
    json_request = request.json
  except Exception as e:
    response = {"response": str(e)}
    return make_response(jsonify(response), 400)

  response = add_knjiga(json_request)

  if response['status'] == "Success":
    return make_response(jsonify(response), 200)

  return make_response(jsonify(response), 400)


@app.route("/posudba", methods=["POST"])
def create_posudba():
  try:
    json_request = request.json
  except Exception as e:
    response = {"response": str(e)}
    return make_response(jsonify(response), 400)

  response = add_posudba(json_request)

  if response["response"] == "Success":
    return make_response(jsonify(response), 200)
  return make_response(jsonify(response), 400)

@app.route("/posudba", methods=["PATCH"])
def update_posudba():
  try:
    json_request = request.json
  except Exception as e:
    response = {"response": str(e)}
    return make_response(jsonify(response), 400)

  if request.args:
    posudba_id = int(request.args.get("id"))
    response = patch_posudba(posudba_id, json_request)

    if response["response"] == "Success":
      return make_response(jsonify(response), 200)

    return make_response(jsonify(response), 400)

  response = {"response": "Query string missing"}
  return make_response(jsonify(response), 400)

  

if __name__ == "__main__":
  app.run(port=8080)