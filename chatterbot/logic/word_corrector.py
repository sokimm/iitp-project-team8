from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from chatterbot import languages
from symspellpy import SymSpell, Verbosity
import pkg_resources


class WordCorrector(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.language = kwargs.get('language', languages.ENG)
        self.sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
        self.dictionary_path = pkg_resources.resource_filename("symspellpy", "frequency_dictionary_en_82_765.txt")
        # TODO : 숫자 없음. dictionary modifying 필요
        self.bigram_path = pkg_resources.resource_filename("symspellpy", "frequency_bigramdictionary_en_243_342.txt")
        self.sym_spell.load_dictionary(self.dictionary_path, term_index=0, count_index=1)
        self.sym_spell.load_bigram_dictionary(self.bigram_path, term_index=0, count_index=2)

    def can_process(self, statement):
        try:
            if " " in statement.text.lower():
                return False
            else:
                response = self.process(statement)
                return response.confidence == 1
        except:
            return False


    def process(self, statement, additional_response_selection_parameters=None):
        input_text = statement.text
        input_text = (input_text)
        suggestions = self.sym_spell.lookup_compound(input_text, max_edit_distance=2)

        for suggestion in suggestions:
            #print(suggestion)
            #print(type(suggestion))
            expression = "Do you mean \""+ str(suggestion).split(",")[0] +"\""

            if input_text == str(suggestion).split(",")[0]:
                expression = ""
            response = Statement(text=expression)
            response.confidence = 1
            #TODO: corrector 돌렸을 때 같을 땐 confidence 0, 다를 땐 confidence 1로 줬었는데 모 딴 거하다 이걸로 냅둠
        return response
