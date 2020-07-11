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
			for restaurant in d['resturants']:
				response = response + "Found " + restaurant['restaurant']['name'] + " in " + \
						   restaurant['restaurant']['location']['address'] + "\n"

		dispatcher.utter_message("-----" + response)

		print("Type 7   : ", response)
		print("Type 8 : ", [SlotSet('location', loc)])

		response = "We will add later response result"
		try:
			file = open("body.txt", "w")
			counter = 1
			for restaurant in d['resturants']:
				response = response + "Found " + restaurant['restaurant']['name'] + " in " + \
						   restaurant['restaurant']['location']['address'] + "\n"


			for restaurant in d['resturants']:
				file.write("{}. Restaurant Name: {}\n Restaurant locality address: {}\n Average budget for two people: {}\n Zomato user rating: {}\n\n".format(
						counter,restaurant['restaurant']['name'], restaurant['restaurant']['location']['address'], "2 people ", "4.6"))
				counter += 1
			file.close()
		except:
			response = "no results"

			dispatcher.utter_message("Foodie Rasa Chatbot Assig : ", response)

		return [SlotSet('location', loc)]

# ## ****
# 	for restaurant in restaurant_final_list:
# 				file.write(
# 					"{}. Restaurant Name: {}\n Restaurant locality address: {}\n Average budget for two people: {}\n Zomato user rating: {}\n\n".format(
# 						counter, restaurant[0], restaurant[1], restaurant[2], restaurant[3]))
# 				counter += 1
# 			file.close()
# ##********




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

class ActionRestarted(Action):
	def name(self):
		return 'action_restart'

	def run(self, dispatcher, tracker, domain):
		return[Restarted()]

class ActionSlotReset(Action):
	def name(self):
		return 'action_slot_reset'

	def run(self, dispatcher, tracker, domain):
		return[AllSlotsReset()]

class ActionValidateEmail(Action):
	def name(self):
		return 'action_validate_email'

	def run(self, dispatcher, tracker, domain):
		pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
		email_check = tracker.get_slot('email')
		if email_check is not None:
			if re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_check):
				return [SlotSet('email', email_check)]
			else:
				dispatcher.utter_message("Sorry this is not a valid email. please check for typing errors")
				return [SlotSet('email', None)]
		else:
			dispatcher.utter_message(
				"Sorry I could not understand the email address which you provided? Please provide again")
			return [SlotSet('email', None)]



class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):

		body = ""
		file = open('body.txt', 'r')

		for line in file.readlines():
			body += line
		file.close()

		# Credential Detail
		mail_user_name = "rakesh.sit045@gmail.com"
		mail_password = "Rakeshkumar@06184"

		# Reciever
		receiver_rakesh_mail = "27002rakesh@gmail.com"
		receiver_trishala_mail = "trishla.singh035@gmail.com"
		receiver_raka_mail = "raka006184@gmail.com"

		gmail_user = mail_user_name
		gmail_password = mail_password

		sent_from = gmail_user
		to = tracker.get_slot('email_id')
		subject = " Restaurant recommendations in " + tracker.get_slot("location").title()

		email_text = """\  
		From: %s  
		To: %s  
		Subject: %s
		%s
		""" % (sent_from, to, subject, body)

		try:
			server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			server.ehlo()
			server.login(gmail_user, gmail_password)
			server.sendmail(sent_from, to, email_text)
			server.close()
			dispatcher.utter_template("utter_email_Sent", tracker)

		except:

			dispatcher.utter_template("utter_email_error", tracker)

		return [SlotSet('email_id', to)]
