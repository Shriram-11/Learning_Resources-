def get_window_size():
	import json
	with open('config.json') as file:
		data = json.load(file)
		return (data['main-window-width'], data['main-window-height'])

def get_window_title():
	import json
	with open('config.json') as file:
		data = json.load(file)
		return data['main-window-title']