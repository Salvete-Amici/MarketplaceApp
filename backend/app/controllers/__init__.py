from flask import jsonify

def success_helper(data, code):
  return jsonify(data), code

def failure_helper(message, code):
  return jsonify({"Error": message}), code