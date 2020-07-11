from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import json
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

import zomatopy


# Action search
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		config = {"user_key": "f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')

		print("Type 1 : ", loc)
		print("Type 2 : ", cuisine)

		location_detail = zomato.get_location(loc, 1)

		print("Type 3 : ", location_detail)

		d1 = json.loads(location_detail)

		print("Type 4 : ", d1)

		lat = d1["location_suggestions"][0]["latitude"]
		lon = d1["location_suggestions"][0]["longitude"]
		cuisines_dict = {'bakery': 5, 'chinese': 25, 'cafe': 30, 'italian': 55, 'biryani': 7, 'north indian': 50,
						 'south indian': 85}
		results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)

		print("Type 5 : ", results)

		d = json.loads(results)

		print("Type    6 : ", d)

		response = ""
		if d['results_found'] == 0:
			response = "no results"
		else:
			for restaurant in d['restaurants']:
				response = response + "Found " + restaurant['restaurant']['name'] + " in " + \
						   restaurant['restaurant']['location']['address'] + "\n"

		dispatcher.utter_message("-----" + response)

		print("Type 7   : ", response)
		print("Type 8 : ", [SlotSet('location', loc)])

		return [SlotSet('location', loc)]


class VerifyLocation(Action):
	TIER_1 = []
	TIER_2 = []

	def __init__(self):
		self.TIER_1 = ['ahmedabad', 'bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune']
		self.TIER_2 = ['agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly',
					   'belgaum',
					   'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro steel city',
					   'chandigarh',
					   'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'erode', 'faridabad',
					   'firozabad',
					   'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hamirpur',
					   'hubli–dharwad',
					   'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi',
					   'jodhpur',
					   'kakinada', 'kannur', 'kanpur', 'kochi', 'kolhapur', 'kollam', 'kozhikode', 'kurnool',
					   'ludhiana', 'lucknow',
					   'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore',
					   'nagpur', 'nanded',
					   'nashik', 'nellore', 'noida', 'patna', 'pondicherry', 'purulia', 'prayagraj', 'raipur', 'rajkot',
					   'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur',
					   'srinagar', 'surat',
					   'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tiruppur', 'ujjain', 'bijapur', 'vadodara',
					   'varanasi',
					   'vasai-virar city', 'vijayawada', 'visakhapatnam', 'vellore', 'warangal']

	def name(self):
		return "verify_location"

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')

		if not (self.verify_location(loc)):
			dispatcher.utter_message("Sorry, we do not operate in " + loc + " yet. Please try some other city.")
			return [SlotSet('location', None), SlotSet("location_ok", False)]
		else:
			return [SlotSet('location', loc), SlotSet("location_ok", True)]

	def verify_location(self, loc):
		return loc.lower() in self.TIER_1 or loc.lower() in self.TIER_2
