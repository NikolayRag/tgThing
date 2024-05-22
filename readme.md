###TG-OPENAI bot core engine.


* Handles user interaction with openai GPT api within telegram.

* tgThing passes messages to-from while handling GPT's system state.
* GPT's system state describes the implicit rules of GPT, and so
  tgThing manages and deliver implicit operational character to user.

* tgThing operation without any rules is an instant GPT connector.


---
###Structure

- kiThing API entrance
  - kiTMessage  Message instance
  - kiTFlow Conversation logic
    - kiTChar Virtual character
    - kiTTeleAgent  Telegram API connection
    - kiTAIAgent GPT API connection
  - kiTRobot  Local message proccessing

  - kiTUser User account
  - kiTDB Storage
  - kiTMetrics  Metrics operational class and fabric


---
###Workflow

* There're 3 logical interfaces: with Telegram (kiTTeleAgent), with GPT (kiTAIEntry),
  and with Character (kiTChar) which is technically a GPT Behavior Tuner.

* Logic manager (kiTFlow) is procceeding User message:
  
  - Messages are parsed and long-term context is retreived which describe user's
    virtual Character.
  - Then message is composed with semantic description of Character rules
    and tgThing's technical control protocol for GPT, and sent to GPT.
  - GPT responce is technically split into User and Metrics. User part is sent
    to TG back, Metrics contains requested GPT metrics to adjust virtual Character.

