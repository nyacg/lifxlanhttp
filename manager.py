from lifxlan import *
from pprint import pprint

MAX = 65535

def listtocolor(hsbklist):
	return {'hue': hsbklist[0], 'saturation': hsbklist[1], 'kelvin': hsbklist[3]}

lifx = LifxLAN()
bulbs = {}

def refresh_bulbs(lifx, bulbs):
	lifxlanlights = None

	print "Finding bulbs"

	try:
		lifxlanlights = lifx.get_lights()

		for bulb in lifxlanlights:
			#print("Found {}".format(bulb.get_label()))

			id = bulb.get_mac_addr().replace(":", "")
			label = bulb.get_label()
			power = "on" if bulb.get_power() > 0 else "off"
			lifxlancolor = bulb.get_color()

			bulbs[id] = {
			'bulb': bulb,
				'id': id,
				'uuid': None,
				'label': label,
				'connected': True,
				'power': power,
				'color': listtocolor(lifxlancolor),
				'brightness': lifxlancolor[2]/MAX,
				'group': {'id': None, 'name': None},
				'location': {'id': None, 'name': None},
				'product': {'name': None, 'identifier': None, 'company': None, 'capabilities': {'has_color': None, 'has_variable_color_temp': None}},
				'last_seen': None,
				'seconds_since_seen': 0.0
			}

			pprint(bulbs[id])
	except:
		print "Unexpected error:", sys.exc_info()[0], sys.exc_info()[1]


refresh_bulbs(lifx, bulbs)

print "{} bulbs found".format(len(bulbs))
print ""



