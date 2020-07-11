# a = [3, 2, 1]
#
# b = sorted(a)
# print("a : ", a)
# a.insert(0, 1)
# print(b[1])
# print(a)
# print(b)


class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		# Get user's email id
		to_email = tracker.get_slot('emailid')

		# Get location and cuisines to put in the email
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		global d_email_rest
		email_rest_count = len(d_email_rest)
		# Construct the email 'subject' and the contents.
		d_email_subj = "Top " + str(email_rest_count) + " " + cuisine.capitalize() + " restaurants in " + str(
			loc).capitalize()
		d_email_msg = "Hi there! Here are the " + d_email_subj + "." + "\n" + "\n" + "\n"
		for restaurant in d_email_rest:
			d_email_msg = d_email_msg + restaurant['restaurant']['name'] + " in " + \
						  restaurant['restaurant']['location']['address'] + " has been rated " + \
						  restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" + "\n"

		# Open SMTP connection to our email id.
		s = smtplib.SMTP("smtp.gmail.com", 587)
		s.starttls()
		s.login("asaupgrad.chatbot@gmail.com", "pgdmlaiupgrad")

		# Create the msg object
		msg = EmailMessage()

		# Fill in the message properties
		msg['Subject'] = d_email_subj
		msg['From'] = "asaupgrad.chatbot@gmail.com"

		# Fill in the message content
		msg.set_content(d_email_msg)
		msg['To'] = to_email

		s.send_message(msg)
		s.quit()
		dispatcher.utter_message("** EMAIL SENT! HAPPY DINING :) **")
		return []
