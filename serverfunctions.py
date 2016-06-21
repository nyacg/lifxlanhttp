from pprint import pprint
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