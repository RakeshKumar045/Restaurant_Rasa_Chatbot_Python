# Assignment : Foodie Restaurant You’ll be evaluated on the following submission:

Submit the entire folder of your chatbot code as a zip file: It should have all the data files, python files with codes, your saved models etc. The model should run on our CLI without any modifications. Your model will be evaluated on some test cases, similar to the ones shared with you.

Note:  Your chatbot will be evaluated through Command Prompt Line, not through Slack or any other channel. Also, ensure that you are mentioning all the updated versions used for your Chatbot project in a Read Me Text File as part of the Final Submission Folder.nt Search
## @Rakesh Kumar and @ Trishala Singh

#### Email ID : rakesh.sit045@gmail.com
#### Linkedin ID : https://www.linkedin.com/in/rakesh-kumar-gupta-52b77ab4/

#### Email ID : trishla.singh35@gmail.com
#### Linkedin ID : https://www.linkedin.com/in/trishala-singh-1255522a/ 



# Library Installation :

### Create New Environment Variable :
check no of env : conda env list or conda info --envs

create : conda create -n RasaEnv python=3.7 anaconda

conda activate RasaEnv

conda deactivate

conda env remove --name ENVIRONMENT

### Required Libraries :
pip install rasa 

pip install rasa[spacy]

python -m spacy download en_core_web_md
##### OR
python -m spacy link en_core_web_md en

### NLU : 

##### Rasa NLU Run :
rasa train nlu # train nlu model

rasa shell nlu # test nlu model

rasa test nlu # Evaluate nlu model

rasa run actions # expose the nlu model 

##### Rasa Core Run :

rasa train core # train core model

##### OR
rasa train -vv -dump-stories --force 

rasa run actions # expose the core model

rasa shell  # test core model

rasa test core # Evaluate core model

##### Note : actions server run in terminal 1 and test model in terminal 2



# Run Chatbot :
### Terminal 1 :
rasa init --no-prompt #note : do not run this command

### Start directly from here :
rasa run -m models --enable-api --cors "*" --debug

### Terminal 2 :
./ngrok http 5005 #linux

ngrok http 5005 #windows
 
##### Expose URL : http://a1becb115fae.ngrok.io  # check url in googel browser(copy and paste in  google chrome) : Hello from Rasa: 1.10.3
 
# Deployment :
### Slack :
End url : /webhooks/slack/webhook

Link 1: https://api.slack.com/

Link 2: https://app.slack.com/client/T016GCA0T5K/D016XJ4Q75X

Reference video Link : https://www.youtube.com/watch?v=YsOcE8pCXsk&t=192s

### Facebook :
End url : /webhooks/facebook/webhook

Reference video Link : https://www.youtube.com/watch?v=tFYS6JVYNTI

### Telegram :
End url : /webhooks/telegram/webhook

Reference video Link: https://www.youtube.com/watch?v=eDDZ8IsH7Es

Final url : http://a1becb115fae.ngrok.io/webhooks/slack/webhook
