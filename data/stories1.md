
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* number_of_person{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - verify_location

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* number_of_person{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - verify_location
    - slot{"location": "Bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_goodbye
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - action_stop_bot
