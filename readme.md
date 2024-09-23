##Идея, лежащая в основе этого метабота.

tgThing - Симбиотический информационный спутник человека, как носителя сознания, *персонаж* с эволюционирующим личным контактом.  
Он существует в *изменяющемся* контекстном пространстве *диалогов* с родителем.

Технически это эволюционирующий набор бизнеслогики, оперирующей тремя потоками информации - **родительской** (запросы человека и ответ ему), **сгенерированной** (сервис ИИ, аналитические инструменты), и **хранимого контекста** (долгосрочная структурированная память).

Базовая логика складывается из явного обмена информацией (**диалог**) и фонового рекурсивного структурирования памяти (**инфобиота**).  

**Диалог** - явный обмен информацией:
- прямой запрос пользователя
- семантический разбор и сопоставление с **памятью**
- передача на генератор ответа (ИИ)
- разбор ответа, переформулирование, корректировка памяти
- выдача пользователю

**Инфобиота** - рекурсивное структурирование памяти:
- запрос структуры памяти
- поиск блоков информации с высокой энтропией
- структурирование
- обновление памяти

--

###TG-Character bot core engine.

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

