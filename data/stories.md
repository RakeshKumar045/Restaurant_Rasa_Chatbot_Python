## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export
	


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye



## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - verify_location
    - slot{"location": "Delhi"}
    - slot{"location_ok": true}
    - utter_ask_budget_for_two
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* affirm
    - utter_ask_email
* send_email{"email": "trishla.singh35@gmail.com"}
    - slot{"email": "trishla.singh35@gmail.com"}
    - action_validate_email
    - slot{"email": "trishla.singh35@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Other_cities"}
    - slot{"location": "Other_cities"}

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - verify_location
    - slot{"location": "Agra"}
    - slot{"location_ok": true}
    - utter_ask_budget_for_two
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - utter_people
* people
    - utter_ask_email
* send_email{"email": "trishsin03@gmail.com"}
    - slot{"email": "trishsin03@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "ahemdabad"}
    - slot{"location": "ahemdabad"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - verify_location
    - slot{"location": "Ahmedabad"}
    - slot{"location_ok": true}
    - utter_people
* people
    - utter_ask_budget_for_two
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - utter_ask_cuisine
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "Ahmedabad"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* affirm
    - utter_ask_email
* send_email{"email": "trishla.singh35@gmail.com"}
    - slot{"email": "trishla.singh35@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* affirm{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - verify_location
    - slot{"location": "Bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
    - utter_ask_budget_for_two
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* send_email{"email": "trishla.singh35@gmail.com"}
    - slot{"email": "trishla.singh35@gmail.com"}
    - action_send_mail
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget_for_two
* budget{"budgetmin": "700"}
    - slot{"budgetmin": "700"}
    - verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - utter_ask_location
    - utter_ask_location
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* affirm
    - utter_goodbye
* goodbye
