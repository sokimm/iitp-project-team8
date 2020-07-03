# 20spring-iitp-project-team8-chatbot
2020 Spring IITP Project Team8. Each team will build a general purpose Chatbot that is able to conduct dialoguewith a humanuser.


## chatterbot
This is from https://github.com/gunthercox/ChatterBot

We make some modification of 
- chatterbot/chatterbot.py
- chatterbot/logic/mathematical_evaluation.py
- chatterbot/logic/time_adapter.py

and we add our own files
- chatterbot/postprocessors.py
- chatterbot/logic/retrieval_custon.py
- chatterbot/logic/parlai_adapter.py
- chatterbot/logic/context_adapter.py


## mathparse
This is from https://github.com/gunthercox/mathparse/tree/master/mathparse

We make some modification of
- mathparse/mathparse.py

## aiml
This is from https://github.com/paulovn/python-aiml

We make some modification of
- std-starup.xml
- aiml/Kernel.py
- aiml/Utils.py

and we add our own files
- aiml/botdata/std-custom/std-*.aiml

## parlai
This is from https://github.com/facebookresearch/ParlAI

We make some modification of
- parlai/tasks/interative/worlds.py
- parlai/tasks/blended_skill_talk/worlds.py
- parlai/agents/safe_local_human.py

and we add our own files
- parlai/scripts/safe_interactive_custom.py

## ui
This is from https://github.com/chamkank/flask-chatterbot

We make some modification of
- ui/static/style.css
- ui/templates/index.html
