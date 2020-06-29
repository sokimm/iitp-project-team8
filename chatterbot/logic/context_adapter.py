from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from chatterbot import languages
import datetime


class ContextAdapter(LogicAdapter):
    """
    Context Adapter helps to control the context.
    
    If the most recent user input is same as current input,
    sample response is "You kist ask me that." + "originam response".
    
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.language = kwargs.get('language', languages.ENG)
        self.cache = {}
        self._input_history = ['BEGIN']
        self._max_history = 10

    def can_process(self, statement):
        response = self.process(statement)
        self.cache[statement.text] = response
        return response.confidence == 0.9

    def process(self, statement, additional_response_selection_parameters=None):
        input_text = statement.text
        
        if input_text in self.cache:
            response = Statement(text='You just ask me that.')
            response.confidence = 0.9
            self.cache = {}
            return response
        
        if input_text == self._input_history[-1]:
            response = Statement(text='You just ask me that.')
            response.confidence = 0.9

        else:
            self._input_history.append(input_text)
            while len(self._input_history) > self._max_history:
                self._input_history.pop(0)
            response = Statement(text='')
            response.confidence = 0

        return response
