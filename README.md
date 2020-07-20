## Follow Me:

 [<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/rakesh-kumar-gupta-52b77ab4/) [<img src = "https://img.shields.io/badge/kaggle-%3390FF.svg?&style=for-the-badge&logo=kaglle&logoColor=white">](https://www.kaggle.com/rakesh6184) [<img src = "https://img.shields.io/badge/twitter-3336FF.svg?&style=for-the-badge&logo=twitter&logoColor=white">](https://twitter.com/2702rakesh) [<img src="https://img.shields.io/badge/medium-%2312100E.svg?&style=for-the-badge&logo=medium&logoColor=white" />](https://medium.com/@2702rakesh)


## Hi there 👋

![Rakesh's github stats](https://github-readme-stats.vercel.app/api?username=RakeshKumar045&show_icons=true)
<img src="https://i.giphy.com/media/LMt9638dO8dftAjtco/200.webp" width="100"><img src="https://i.giphy.com/media/KzJkzjggfGN5Py6nkT/200.webp" width="100"><img src="https://i.giphy.com/media/IdyAQJVN2kVPNUrojM/200.webp" width="100">


# Assignment : Foodie Restaurant Search Case Study:

#### Restaurant Bot :

A restaurant chatbot using open source chat framework RASA : https://rasa.com/. Integrates with Zomato : https://developers.zomato.com/?lang=tr API to fetch restaurant information.

Problem Statement An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. You have been hired as the lead data scientist for creating this product.

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. The project brief provided to you is as follows.

The bot takes the following inputs from the user:

City: Take the input from the customer as a text field. For example:

Bot: In which city are you looking for restaurants?

User: anywhere in Delhi

Important Notes:

Assume that Foodie works only in Tier-1 and Tier-2 cities. You can use the current HRA classification of the cities from here. Under the section 'current classification' on this page, the table categorizes cities as X, Y and Z. Consider 'X ' cities as tier-1 and 'Y' as tier-2. The bot should be able to identify common synonyms of city names, such as Bangalore/Bengaluru, Mumbai/Bombay etc.

Your chatbot should provide results for tier-1 and tier-2 cities only, while for tier-3 cities, it should reply back with something like "We do not operate in that area yet".

Cuisine Preference: Take the cuisine preference from the customer. The bot should list out the following six cuisine categories (Chinese, Mexican, Italian, American, South Indian & North Indian) and the customer can select any one out of that. Following is an example for the same:

Bot: What kind of cuisine would you prefer?

Chinese Mexican Italian American South Indian North Indian User: I’ll prefer Italian!

Average budget for two people: Segment the price range (average budget for two people) into three price categories: lesser than 300, 300 to 700 and more than 700. The bot should ask the user to select one of the three price categories. For example:

Bot: What price range are you looking at?

Lesser than Rs. 300 Rs. 300 to 700 More than 700 User: in range of 300 to 700

* NLU training: One can use rasa-nlu-trainer to create more training examples for entities and intents. Try using regex features and synonyms for extracting entities.

* Build actions for the bot: Read through the Zomato API documentation to extract the features such as the average price for two people and restaurant’s user rating. One can also build an ‘action’ for sending emails from Python.

* Creating more stories: Use train_online.py file to create more stories. Refer to the sample conversational stories provided above.


Note:  Your chatbot will be evaluated through Command Prompt Line, not through Slack or any other channel. Also, ensure that you are mentioning all the updated versions used for your Chatbot project in a Read Me Text File as part of the Final Submission Folder.nt Search
## @Rakesh Kumar and @ Trishala Singh

#### Email ID : rakesh.sit045@gmail.com
#### Linkedin ID : https://www.linkedin.com/in/rakesh-kumar-gupta-52b77ab4/

#### Email ID : trishla.singh35@gmail.com
#### Linkedin ID : https://www.linkedin.com/in/trishala-singh-1255522a/ 

## The Architecture of chatbot:
![](https://camo.githubusercontent.com/00b24c2d647e91fbc26418626fa1804ef61e770e/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f6d61782f313037382f312a425642512d7569414f5942394c746862536f695555412e706e67)

## Rasa Architecture :

![](https://camo.githubusercontent.com/b93c48620cf63fae2b970f70ae5f6e5cc4610520/68747470733a2f2f6c68342e676f6f676c6575736572636f6e74656e742e636f6d2f76676c4475732d544e55616443502d4a4a7643484f4777556b6e344e6454443662616c737562744f2d5139434f366e6c5231753178386567445f64575a534e536d6639384172716a4359566843785a41665a5f52724a4f4d2d447831636e35364e356f4169576f504d6333354c5959324453307556797a315735447349517a6b6655323342636f62)

Here Interpreter is part of NLU and Tracker, policy and action are part of Core.

* The message is passed to an Interpreter, which converts it into a dictionary including the original text, the intent, and any entities that were found.

* The Tracker is the object which keeps track of the conversation state. It receives the info that a new message has come in. Know more about it here: https://rasa.com/docs/rasa/api/tracker-stores/

* The policy receives the current state of the tracker, chooses the next action which is logged by the tracker and response is sent to the user. There are different policies to choose from.
You will get more information here: https://rasa.com/docs/rasa/core/policies/#policies
Along with policy “slots” which act as bot’s memory(context). It also influences how the dialogue progresses. Read more about slots here: https://rasa.com/docs/rasa/core/slots/



# Library Installation :

## Pre-requisites :
* python 3.7.0
* rasa 1.1.4
* spacy 2.1.4
* en_core_web_md 2.1.0

### Create New Environment Variable :
- check no of env : conda env list or conda info --envs
- create : conda create -n RasaEnv python=3.7 anaconda
- conda activate RasaEnv
- conda deactivate
- conda env remove --name ENVIRONMENT

### Required Libraries :
- pip install rasa 
- pip install rasa[spacy]
- python -m spacy download en_core_web_md

##### OR
- python -m spacy link en_core_web_md en

# RASA
- Refer to official installation guide : https://rasa.com/docs/rasa/user-guide/installation/ to install RASA

### NLU : 

##### Rasa NLU Run :
- rasa train nlu # train nlu model
- rasa shell nlu # test nlu model
- rasa test nlu # Evaluate nlu model
- rasa run actions # expose the nlu model 

##### Rasa Core Run :
- rasa train core # train core model
##### OR
- rasa train -vv -dump-stories --force 

#### Equivalent RASA CLI command: 
- rasa run actions # expose the core model

#### Run RASA action server ( mandatory step to interact with chatbot) on port 5055
- python actions_server.py

#### Train RASA NLU and Core model
- python rasa_train.py

#### Equivalent RASA CLI command
- rasa train
- rasa train -vv -dump-stories --force 


#### Starts an interactive session with restaurant chatbot
- python rasa_train.py --shell

#### Equivalent RASA CLI command
- rasa shell

#### Run RASA server to connect slack channel
rasa run -m models -p 5004 --connctor slack --credentials credentials.yml







- rasa shell  # test core model
- rasa test core # Evaluate core model

##### Note : actions server run in terminal 1 and test model in terminal 2

# Run Chatbot :
### Terminal 1 :
rasa init --no-prompt #note : do not run this command

### Start directly from here :
- rasa run -m models --enable-api --cors "*" --debug

### Terminal 2 :
- ./ngrok http 5005 #linux
- ngrok http 5005 #windows
 
##### Expose URL : http://a1becb115fae.ngrok.io  # check url in googel browser(copy and paste in  google chrome) : Hello from Rasa: 1.10.3
 
# Repo Information:
This repo contains training data and script files necessary to compile and execute this restaurant chatbot. It comprises of the following files:

### Data Files :
* data/nlu.md : contains training examples for the NLU model
* data/stories.md : contains training stories for the Core model

## Script Files :
* zomato : contains Zomato API integration code
* zomato.py : contains functions to consume common Zomato APIs like fetch location details, type of cuisines, search for restaurants, etc
* actions.py : contains the following custom actions (insert ZOMATO API key in this script file before starting RASA server)

- search restaurant
- action_restart
- action_search_restaurants
- action_send_mail
- action_slot_reset
- action_validate_email
- validate location
- validate cuisine
- restart conversation
- reset slots

## Config Files : 
* config.yml contains model configuration and custom policy

* credentials.yml contains authentication token to connect with channels like slack

* domain.yml defines chatbot domain like entities, actions, templates, slots

* endpoints.yml contains the webhook configuration for custom action
 
 
 
# Rasa Reference video :
* https://www.youtube.com/watch?v=xu6D_vLP5vY
 
 
# Deployment :
### Slack :
* End url : /webhooks/slack/webhook

* Link 1: https://api.slack.com/

* Link 2: https://app.slack.com/client/T016GCA0T5K/D016XJ4Q75X

* Reference video Link : https://www.youtube.com/watch?v=YsOcE8pCXsk&t=192s

### Facebook :
* End url : /webhooks/facebook/webhook

* Reference video Link : https://www.youtube.com/watch?v=tFYS6JVYNTI

### Telegram :
* End url : /webhooks/telegram/webhook

* Reference video Link: https://www.youtube.com/watch?v=eDDZ8IsH7Es

* Final url : http://a1becb115fae.ngrok.io/webhooks/slack/webhook
