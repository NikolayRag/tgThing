##Идея, лежащая в основе этого метабота.

tgThing - Симбиотический информационный спутник человека, как носителя сознания, *персонаж* с адаптирующимся профилем личного контакта.  
Он существует в *изменяющемся* контекстном пространстве *диалогов* с носителем.  

Технически это эволюционирующий набор бизнеслогики, оперирующей тремя потоками информации - **родительской** (запросы человека и ответ ему), **сгенерированной** (сервис ИИ, аналитические инструменты), и **хранимого контекста** (долгосрочная структурированная память).

Базовая логика складывается из явного обмена информацией (**диалог**, flow) и фонового рекурсивного структурирования памяти (**инфобиота**).  

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

###Structure

* kThing - API entrance
  * ktMessage - Message instance
    * ktMMetric - Message metrics
  * ktFlow - Message transport (dispatcher)
    * ktBotAgent - Telegram API connection
    * ktAIAgent - AI connection
    * ktChar - Character logic
      * ktMemAgent - Contextual memory
    * ktRobot - Local message proccessing

  * ktUser - User account
  * ktDB - Storage


--

###Workflow

* There're 3 logical interfaces: with Telegram (`ktBotAgent`), with GPT (`ktAIAgent`),
  and with Memory (`ktMemAgent`).

* Flow transport (`ktFlow`) is procceeding messages using `ktChar` logic:
  
  * Messages are parsed and long-term context is retreived which describe Character personality.
  * Message is composed using Character rules, and sent to GPT.
  * GPT response is decomposed into things to be memorized and explicit conversation answer.
