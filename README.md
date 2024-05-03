# assistant
The idea is to build a helpful and proactive AI assistant which acts, based on static and dynamic personal data. 
Static data: personality, social connections and family, hobbies and interests.

Dynamic data: location, events, personal sensors data.

The Assistant is able to use static information together with dynamic data. As a result it should be able to enrich static information overtime. 

This is not a game like experience in the virtual world (Replica)

This is not just a chat engine as tons of existing apps

Possible integrations.
 1. Create reminders based on emails and calendar events, location or sensor data.
 2. Build recommendations based on static and dynamic data: events around, sales and deals.
  
Overal behavior of an assistant should be defined in static memory. With major introspective questions:

Can I help a human, based on my knowledge about him + latest incoming information?

If answer is yes, then it should act.

If answer is no, then it should decide: to store incoming information for further processing when more data coming, or make an internal conclusion and store it in static memory.

For POC:

Telegram bot with access to email. By analyzing email content it makes suggestions. Static data can be added and edited by user through interactions with the bot. 

