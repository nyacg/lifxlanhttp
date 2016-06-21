from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "LIFX Local HTTP Server is Running"

@app.route("/v1/lights/<selector>")
def listlights():
	return "todo"

@app.route("/v1/lights/<selector>/state", methods=['PUT'])
def setstate():
	return "todo"

@app.route("/v1/lights/states", methods=['PUT'])
def setstates():
	return "todo"

@app.route("/v1/lights/<selector>/toggle", method=['POST'])
def togglelights():
	return "todo"

@app.route("/v1/lights/<selector>/effects/breathe", method=['POST'])
def breathelights():
	return "todo"

@app.route("/v1/lights/<selector>/effects/pulse", method=['POST'])
def pulselights():
	return "todo"

@app.route("/v1/lights/<selector>/cycle", method=['POST'])
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