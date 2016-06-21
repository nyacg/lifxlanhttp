from flask import Flask, request, jsonify
from serverfunctions import *
from manager import *

app = Flask(__name__)

lifx = LifxLAN()
bulbs = {}
refresh_bulbs(lifx, bulbs)

print "{} bulbs found".format(len(bulbs))


@app.route("/")
def index():
	return "LIFX Local HTTP Server is Running"

@app.route("/v1/lights/<selector>")
def listlights(selector):
	ids = parse_selector(selector, bulbs)
	if ids is not None:
		return_list = []
		for id in ids:
			bulb_object = dict(bulbs[id])
			del bulb_object['bulb']
			del bulb_object['finished']
			return_list.append(bulb_object)

		return jsonify(return_list)
	else:
		return "Invalid Selector"

@app.route("/v1/lights/<selector>/state", methods=['PUT'])
def setstate():
	return "todo"

@app.route("/v1/lights/states", methods=['PUT'])
def setstates():
	return "todo"

@app.route("/v1/lights/<selector>/toggle", methods=['POST'])
def togglelights():
	return "todo"

@app.route("/v1/lights/<selector>/effects/breathe", methods=['POST'])
def breathelights():
	return "todo"

@app.route("/v1/lights/<selector>/effects/pulse", methods=['POST'])
def pulselights():
	return "todo"

@app.route("/v1/lights/<selector>/cycle", methods=['POST'])
def cyclelights():
	return "todo"

@app.route("/v1/scenes")
def listscenes():
	return "todo"

@app.route("/v1/scenes/<scene_id>/activate", methods=['PUT'])
def setscene():
	return "todo"

@app.route("/v1/color")
def validatecolor():
	return "todo"

if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)