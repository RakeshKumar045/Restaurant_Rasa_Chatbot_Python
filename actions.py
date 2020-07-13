from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import json
import urllib3
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

urllib3.disable_warnings()

import smtplib
import os
import re
import requests
import json
import pandas as pd
from threading import Thread
from flask import Flask
from flask_mail import Mail, Message
from time import sleep
import zomatopy
from concurrent.futures import ThreadPoolExecutor

top_10_restaurant_details = []


# Action search
class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "f4924dc9ad672ee8c4f8c84743301af5"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget_min_price = int(tracker.get_slot('budgetmin'))
        budget_max_price = int(tracker.get_slot('budgetmax'))
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]

        results = len(d1["location_suggestions"])
        d_rest = self.get_restaurants(lat, lon, cuisine)

        restaurant_exist = False
        response = ""
        if results == 0:
            dispatcher.utter_message("Sorry, no results found :(" + "\n")
            restaurant_exist = False
        else:

            zomato_response_df = restaurant_result(d_rest)
            restaurant_df = restaurant_budget_price(zomato_response_df.copy(), budget_min_price, budget_max_price)

            if len(restaurant_df) == 0:
                dispatcher.utter_message("Sorry, no results found :(" + "\n")
                restaurant_exist = False
                return [SlotSet('location', loc), SlotSet('restaurant_exist', restaurant_exist)]

            df = restaurant_df.head(5)
            for ind, val in df.iterrows():
                response = response + "Restaurant Name : " + df['Restaurant Name'][ind] + " & Address : " + \
                           df['Address'][ind] \
                           + " & Rating : " + df["Rating"][ind] + " & Total Riews : " + str(
                    df["Total Reviews"][ind]) + "\n"

            dispatcher.utter_message("Top 5 Restaurant : " + "\n" + response)

            global top_10_restaurant_details
            top_10_restaurant_details = restaurant_df[:10]
            if len(top_10_restaurant_details) > 0:
                restaurant_exist = True

        return [SlotSet('location', loc), SlotSet('restaurant_exist', restaurant_exist)]

    def get_restaurants(self, lat, lon, cuisine):
        cuisines_dict = {'american': 1, 'chinese': 25, 'italian': 55, 'mexican': 73, 'north indian': 50, 'thai': 95,
                         'south indian': 85}
        d_rest = []
        executor = ThreadPoolExecutor(max_workers=5)
        for res_key in range(0, 101, 20):
            executor.submit(retrieve_restaurant, lat, lon, cuisines_dict, cuisine, res_key, d_rest)
        executor.shutdown()
        return d_rest


def restaurant_result(responses):
    df = pd.DataFrame()
    for r in responses:
        df1 = pd.DataFrame([{'Restaurant Name': r['restaurant']['name'],
                             "Address": r['restaurant']['location']['address'],
                             "Phone": r['restaurant']["phone_numbers"],
                             "Timing": r['restaurant']["timings"],
                             "Cuisines": r['restaurant']["cuisines"],
                             "Rating": r['restaurant']["user_rating"]["aggregate_rating"],
                             "Total Reviews": r['restaurant']["all_reviews_count"],
                             "Avg_Cost_for_Two": r['restaurant']["average_cost_for_two"],
                             "Comment": r['restaurant']["user_rating"]["rating_text"],
                             "Featured_Image": r['restaurant']["featured_image"],
                             "URL": r['restaurant']["url"]
                             }])

        df = df.append(df1)
    df = df.reset_index()
    df = df.drop(["index"], axis=1)
    return df


def restaurant_budget_price(dataset, min_value, max_value):
    dataset = dataset[(dataset.Avg_Cost_for_Two > min_value) & (dataset.Avg_Cost_for_Two < max_value)]
    dataset = dataset.sort_values(by=['Rating'], ascending=False)
    return dataset


def retrieve_restaurant(lat, lon, cuisines_dict, cuisine, res_key, d_rest):
    base_url = "https://developers.zomato.com/api/v2.1/"

    headers = {'Accept': 'application/json',
               'user-key': 'f4924dc9ad672ee8c4f8c84743301af5'}
    try:
        results = (requests.get(base_url + "search?" + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" +
                                str(cuisines_dict.get(cuisine)) + "&start=" + str(res_key) + "&count=20",
                                headers=headers).content).decode("utf-8")
    except:
        return
    d = json.loads(results)
    d_rest.extend(d['restaurants'])


class VerifyBudget(Action):
    def name(self):
        return 'verify_budget'

    def run(self, dispatcher, tracker, domain):
        error_msg = "Sorry!! price range not supported, please re-enter."
        try:
            budgetmin = int(tracker.get_slot('budgetmin'))
            budgetmax = int(tracker.get_slot('budgetmax'))
        except ValueError:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budgetmin', None), SlotSet('budgetmax', None), SlotSet('budget_ok', False)]
        min_dict = [0, 300, 700]
        max_dict = [300, 700]
        if budgetmin in min_dict and (budgetmax in max_dict or budgetmax > 700):
            return [SlotSet('budgetmin', budgetmin), SlotSet('budgetmax', budgetmax), SlotSet('budget_ok', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budgetmin', 0), SlotSet('budgetmax', 10000), SlotSet('budget_ok', False)]


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
        if loc == "Other_cities":
            dispatcher.utter_template("utter_other_cities", tracker)
            loc = tracker.get_slot('location')
            return [SlotSet('location', loc), SlotSet("location_ok", False)]

        # loc = None

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
        return [Restarted()]


class ActionSlotReset(Action):
    def name(self):
        return 'action_slot_reset'

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


class ActionValidateEmail(Action):
    def name(self):
        return 'action_validate_email'

    def run(self, dispatcher, tracker, domain):
        pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        email_check = tracker.get_slot('email')
        if email_check is not None:
            if re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_check):
                return [SlotSet('email_ok', True)]
            else:
                dispatcher.utter_message("Sorry this is not a valid email. please check for typing errors")
                return [SlotSet('email', None),SlotSet("email_ok", False)]
        else:
            dispatcher.utter_message("Sorry I could'nt understand the email address you provided? Please provide again")
            return [SlotSet('email', None)]


def config():
    gmail_user = "foodeebotraka@gmail.com"
    gmail_pwd = "QAZX@100"  # Gmail Password
    gmail_config = (gmail_user, gmail_pwd)
    return gmail_config


def mail_config(gmail_credential_detail):
    mail_settings = {

        "MAIL_SERVER": 'smtp.gmail.com',
        "MAIL_PORT": 465,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
        "MAIL_USERNAME": gmail_credential_detail[0],
        "MAIL_PASSWORD": gmail_credential_detail[1],

    }
    return mail_settings

gmail_credentials = config()

app = Flask(__name__)
app.config.update(mail_config(gmail_credentials))
mail = Mail(app)


def send_async_email(flask_app, msg):
    with flask_app.app_context():
        # block only for testing parallel thread
        for i in range(10, -1, -1):
            sleep(2)
        mail.send(msg)


def send_email(recipient, top_10_restaurant_df):
    msg = Message(subject="Restaurant Details", sender=gmail_credentials[0], recipients=[recipient])
    msg.html = u'<h2>Foodie has found few restaurants for you:</h2>'

    for ind, val in top_10_restaurant_df.iterrows():
        name = top_10_restaurant_df['Restaurant Name'][ind]
        location = top_10_restaurant_df['Address'][ind]
        budget = top_10_restaurant_df['Avg_Cost_for_Two'][ind]
        rating = top_10_restaurant_df['Rating'][ind]
        image = top_10_restaurant_df['Featured_Image'][ind]
        url = top_10_restaurant_df['URL'][ind]

        msg.html += u'<h3>{name} (Rating: {rating})</h3>'.format(name=name, rating=rating)
        msg.html += u'<h4>Address: {locality}</h4>'.format(locality=location)
        msg.html += u'<h4>Average Budget for 2 people: Rs{budget}</h4>'.format(budget=str(budget))
        msg.html += u'<div dir="ltr">''<a href={url}><img height = "325", width = "450", src={image}></a><br></div>'.format(
            url=url, image=image)

    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()


class SendMail(Action):
    def name(self):
        return 'action_send_mail'

    def run(self, dispatcher, tracker, domain):
        recipient = tracker.get_slot('email')

        try:
            restaurant_top_10_details = top_10_restaurant_details.copy()
            send_email(recipient, restaurant_top_10_details)
            dispatcher.utter_message("Have a great day! Mail is sent")
        except:
            dispatcher.utter_message("Email address is not valid")
