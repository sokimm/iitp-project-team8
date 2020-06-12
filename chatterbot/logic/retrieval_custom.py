from datetime import datetime
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from chatterbot import languages
from aiml import Kernel


class RetrievalCustom(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.language = kwargs.get('language', languages.ENG)
        self.cache = {}
        k = Kernel()
        k.learn("std-startup.xml")
        k.respond("load aiml b")
        self.kernel = k

    def can_process(self, statement):
        response = self.process(statement)
        self.cache[statement.text] = response
        return response.confidence == 1


    def process(self, statement, additional_response_selection_parameters=None):
        input_text = statement.text

        if input_text in self.cache:
            cached_result = self.cache[input_text]
            self.cache = {}
            return cached_result

        k = self.kernel
        response_aiml = k.respond(input_text)
        # TODO: kernel.py 안에서 respond()에 없는 대답 input으로 넣으면 원래는 I don't know 등을 내뱉지만, 우리는 그걸 없앨거라서
        # response 가 ""로 나오는 경우가 있음.
        # 그럴 때 _respond 에서 "Warning: No match" 어쩌고가 error로서 프린트 되는데 그거 지워야함


        if response_aiml == "": #retrieval 안에 없을 때
            txt = "No match aiml"
            response = Statement(text=txt)
            response.confidence = 0
        else:
            response = Statement(text=response_aiml)
            response.confidence = 1

        return response
