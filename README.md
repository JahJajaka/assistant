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

implementation:

Step 1. Personality   
Chatting with LLM through Telegram bot interface. 
Conversation history saved in NoSQL db. Static data viewed and edited by user through /person command.
Person data saved in NoSQL db with versions and timestamps.
Person data enriched and revaluated by  LLM through conversations.  LLM is prompted to make conclusions about personality.

Step 2. Events   
Dynamic data added through /event command. This is diary like functionality which used by user to describe current events.
Dynamic saved  in NoSQL db with timestamp
Dynamic data pass through LLM, but not necessarily causes the response. There should be some chain of thoughts and maybe Internet search.

Step 3. Integration   
Setup polling email mechanism.
When a new email is detected, upload it.
Check existing dynamic data about the topic.
Gather all context, initiate thoughts and Internet search.
Save thoughts into dynamic storage. 
Send message to user if needed. 
Save conversation history.
Update static personality data if needed.


Miro board: https://miro.com/app/board/uXjVKLxkLAU=/
