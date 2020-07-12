from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import json
import pandas as pd

import zomatopy

print("hi 1")


def zomaato_api():
    response = ""
    try:
        config = {"user_key": "f4924dc9ad672ee8c4f8c84743301af5"}
        zomato = zomatopy.initialize_app(config)
        loc = "New Delhi"
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)

        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]

        print(lat, "  ", lon)

        # lat = 28.6766166672
        # lon = 77.2252111137
        cuisine = "north indian"
        cuisines_dict = {'american': 1, 'chinese': 25, 'italian': 55, 'mexican': 73, 'north indian': 50,
                         'south indian': 5}
        results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)

        # print(" Result 45 ", results)

        d = json.loads(results)
        # print("json : ", d)

        restaurant_response = ""
        # if d['results_found'] == 0:
        #     response = "no results"
        # else:
        #     # restaurant_response = restaurant_result(d)
        #     for r in d['restaurants']:
        #         response = response + r['restaurant']['name'] + r['restaurant']['location']['address'] + "\n"
    except Exception as e:
        print("Exception : ")

    return response


res = zomaato_api()

print("hi 2")

print("Result : \n ", res)

print("hi 3")


def restaurant_result(responses):
    df = pd.DataFrame()
    for r in responses["restaurants"]:
        df1 = pd.DataFrame([{'Restaurant Name': r['restaurant']['name'],
                             "Address": r['restaurant']['location']['address'],
                             "Phone": r['restaurant']["phone_numbers"],
                             "Timing": r['restaurant']["timings"],
                             "Cuisines": r['restaurant']["cuisines"],
                             "Rating": r['restaurant']["user_rating"]["aggregate_rating"],
                             "Total Reviews": r['restaurant']["all_reviews_count"],
                             "Avg_Cost_for_Two": r['restaurant']["average_cost_for_two"],
                             "Comment": r['restaurant']["user_rating"]["rating_text"],
                             "image": r['restaurant']["featured_image"]
                             }])

        df = df.append(df1)

    df = df.reset_index()
    df = df.drop(["index"], axis=1)
    return df


def budget_group(row):
    if row['Avg_Cost_for_Two'] < 300:
        return 'lesser than 300'
    elif 300 <= row['Avg_Cost_for_Two'] < 700:
        return 'between 300 to 700'
    else:
        return 'more than 700'


def restaurant_budget(dataset, price_budget):
    dataset['Budget'] = dataset.apply(lambda row: budget_group(row), axis=1)
    restaurant_df = dataset[(dataset.Budget == price_budget)]
    restaurant_df = restaurant_df.sort_values(['Rating'], ascending=0)
    restaurant_df = restaurant_df.drop_duplicates()
    return restaurant_df

# restaurant_budget(restaurant_result, 'more than 700')
