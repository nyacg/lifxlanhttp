from pprint import pprint
from manager import *
import colorsys

colors = {'white': WHITE, 'red': RED, 'orange': ORANGE, 'yellow': YELLOW, 'cyan': CYAN, 'green': GREEN, 'blue': BLUE, 'purple': PURPLE, 'pink': PINK}

from multiprocessing import Pool
def parse_selector(selector, bulbs):
	"""Takes selector and returns a list of ids that match, an empty array if valid selector but no match
	 or None if invalid selector"""
	ids = []

	if selector == "all":
		ids = bulbs.keys()

	elif selector.startswith("label:"):
		label = selector.split("label:", 1)[1]
		print label
		for id, bulb in bulbs.iteritems():
			pprint(bulb)
			if bulb['label'] == label:
				ids.append(id)

	elif selector.startswith("id:"):
		ids.append(selector.split("id:",1)[1])

	elif selector.startswith("group_id:"):
		group_id = selector.split("group_id:", 1)[1]
		for id, bulb in bulbs.iteritems():
			if bulb['group']['id'] == group_id:
				ids.append(id)

	elif selector.startswith("group:"):
		group = selector.split("group:", 1)[1]
		for id, bulb in bulbs.iteritems():
			if bulb['group']['name'] == group:
				ids.append(id)

	elif selector.startswith("location_id:"):
		location_id = selector.split("location_id:", 1)[1]
		for id, bulb in bulbs.iteritems():
			if bulb['location']['id'] == location_id:
				ids.append(id)

	elif selector.startswith("location:"):
		location = selector.split("location:", 1)[1]
		ids = []
		for id, bulb in bulbs.iteritems():
			if bulb['location']['name'] == location:
				ids.append(id)

	elif selector.startswith("scene_id:"):
		scene_id = selector.split("scene_id:", 1)[1]
		#TODO
		ids = None
	else:
		ids = None

	return ids

def parse_color(color_string, brightness):
	parsed_color = [None, None, None, None]

	# [name]
	if color_string.lower() in colors:
		parsed_color = colors[color_string.lower()]
	# rgb:[0-255], [0-255], [0-255]
	elif color_string.startswith("rgb:"):
		rgb = color_string.split("rgb:", 1)[1]
		rgb = rgb.split(", ")
		try:
			rgb = [int(value) for value in rgb]
		except ValueError:
			return None

		for value in rgb:
			if value < 0 or value > 255:
				return None

		hsb = colorsys.rgb_to_hsv(*rgb)
		parsed_color[0:3] = hsb

	# #RRGGBB
	elif color_string.startswith("#"):
		if len(color_string) == 7:
			try:
				rgb = [int(color_string[i:i+2], 16) for i in range(1, len(color_string), 2)]
			except:
				return None
			for value in rgb:
				if value < 0 or value > 255:
					return None
			hsb = colorsys.rgb_to_hsv(*rgb)
			parsed_color[0:3] = hsb
		else:
			return None
	# some collection of hue:[0-360] saturation:[0.0-1.0] brightness:[0.0-1.0] kelvin:[2500-9000]
	else:
		hsbk_components = color_string.split(" ")
		for component in hsbk_components:
			if component.startswith("hue:"):
				hue = component.split("hue:", 1)[1]
				try:
					hue = int(hue)
				except ValueError:
					return None
				if hue >= 0 and hue <= 360:
					parsed_color[0] = hue
				else:
					return None

			elif component.startswith("saturation:"):
				sat = component.split("saturation:", 1)[1]
				try:
					sat = float(sat)
				except ValueError:
					return None
				if sat >= 0 and sat <= 1.0:
					parsed_color[1] = sat
				else:
					return None

			elif component.startswith("brightness:"):
				sat = component.split("brightness:", 1)[1]
				try:
					brightness = float(brightness)
				except ValueError:
					return None
				if brightness >= 0 and brightness <= 1.0:
					parsed_color[2] = brightness
				else:
					return None

			elif component.startswith("kelvin:"):
				sat = component.split("kelvin:", 1)[1]
				try:
					kelvin = int(kelvin)
				except ValueError:
					return None
				if kelvin >= 2500 and kelvin <= 9000:
					parsed_color[3] = kelvin
				else:
					return None

			else:
				return None

	return parsed_color


def set_light(bulb, bulb_id, power, hsbk, duration):
	'''Assumes recieving a valid and connect bulb id
	bulb should be a lifxlan bulb object'''
	#-- check connected, turn on if not on and check if finished
	# update bulbs with new settings

	bulb.set_power(power, duration, True)
	bulb.set_color(hsbk, duration, True)


def finished_callback(arg):#bulbs, bulb_ids):
	# set finished to true
	print "Finished {}".format(arg)
	pass


def set_lights(bulbs, settings):
	'''
	:param bulbs: bulbs dict
	:param settings: settings dict, (id: setting dict)
	:return: hmmm
	'''
	for id, setting in settings:
		hsbk = parse_color(settings.color_string, settings.brightness)
		set_light(bulbs[id]['bulb'], id, setting.power, hsbk, setting.duration)

	# do a set light on each light in a new thread
	# handle the 'finished' and timeout
	#

		# make finished false
		# call set lights in a task like thing

	#

