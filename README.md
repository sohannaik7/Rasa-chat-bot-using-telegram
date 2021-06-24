# Rasa-chat-bot-using-telegram
rasa chatbot using telegram, this project is on Domain based, where we have built for learning python bot.

hello viewer, how you doin,
I suggest you to go through the installation and set of rasa 

once you have set up the platform, you can see the rasa folder which contains----
1. .idea file
2. actions
3. data 
4. models
5. test 
and mainly you'll find the congig, credentials, domain and endpoint are files out side the those above file.


I have given core zip file, don't unzip it, just add it in the models folder

and in credential there is something called as 

telegram:
  access_token: "1827830380:AAGtXsvjKJHNADKHDHJ36h5qdDv9sKHQRW1Bot0"
  verify: "pipsohanbot"-------------------------------->(YOUR BOT NAME GIVEN IN TELEGRAM) 
  webhook_url: "https://ce0225ed0369.ngrok.io/webhooks/telegram/webhook" -------------->
  ------------>DOWNLOAD THE NGROK FROM NGROK.COM AND ONCE YOU UNZIP IT, YOU'LL GET ONE CMD KIND OF FILE OPEN IT AND THEN TYPE NGROK HTTP 5005
  THIS WILL PROVIDE YOU THE SERVER https://ce0225ed0369.ngrok.io LIKE THIS....
  YOU'LL GET HTTP AND HTTPS, CHOOSE HTTPS....
  AND ADD IT IN WEBHOOK
  
  
  FOR SETTING UP THE TELEGRAM WATCH YOUTUBE.
  
  RUNNING---->  
    1. conda activate <your environment anme>----> set up anaconda
    2. and make same on other terminal
    3. once both terminal are on same ENV
    4. in terminal 1-->first train--->rasa train
    5. then once traing is done, the run--->rasa run
    6. if you have not set up telegram just run ----> rasa shell
    7. once the rasa runs on other terminal --terminal 2 ----rasa run actions
    8. your all set 
  
  


