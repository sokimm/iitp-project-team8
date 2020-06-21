from datetime import datetime
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement


class TimeLogicAdapter(LogicAdapter):
    """
    The TimeLogicAdapter returns the current time.

    :kwargs:
        * *positive* (``list``) --
          The time-related questions used to identify time questions.
          Defaults to a list of English sentences.
        * *negative* (``list``) --
          The non-time-related questions used to identify time questions.
          Defaults to a list of English sentences.
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        from nltk import NaiveBayesClassifier

        self.positive = kwargs.get('positive', [
            'what time is it',
            'what time is it now',
            'hey what time is it',
            'do you have the time',
            'do you know the time',
            'do you know what time it is',
            'could you tell me the time, please?',
            'could you tell me what time it is, please?',
            'what is the time',
            'what\'s the time',
            'tell me the time',
        ])

        self.negative = kwargs.get('negative', [
            'it is time to go to sleep',
            #'what is your favorite color',
            'i had a great time',
            #'thyme is my favorite herb',
            'do you have time to look at my essay',
            #'how do you have the time to do all this'
            #'what is it'
            'do you have time',
            'i had time',
            'nice time',
            'do you have time to look at my essay',
            'many times',
            'no time',
            'how many times',
            'there is no time',
            'the phone rang ten times before lisa gave up'
        ])

        labeled_data = (
            [
                (name, 0) for name in self.negative
            ] + [
                (name, 1) for name in self.positive
            ]
        )

        train_set = [
            (self.time_question_features(text), n) for (text, n) in labeled_data
        ]

        self.classifier = NaiveBayesClassifier.train(train_set)

    def can_process(self, statement):


        if 'time' in statement.text.lower():
            response = self.process(statement)
            set_preps = set(["in", "at", "of", "for"])
            if set(statement.text.lower().split(" ")) & set_preps != set():
                return response.confidence == 0
        else:
            return False
        return response.confidence == 1



    def time_question_features(self, text):
        """
        Provide an analysis of significant features in the string.
        """
        features = {}

        # A list of all words from the known sentences
        all_words = " ".join(self.positive + self.negative).split()

        # A list of the first word in each of the known sentence
        all_first_words = []
        for sentence in self.positive + self.negative:
            all_first_words.append(
                sentence.split(' ', 1)[0]
            )

        for word in text.split():
            features['first_word({})'.format(word)] = (word in all_first_words)

        for word in text.split():
            features['contains({})'.format(word)] = (word in all_words)

        for letter in 'abcdefghijklmnopqrstuvwxyz':
            features['count({})'.format(letter)] = text.lower().count(letter)
            features['has({})'.format(letter)] = (letter in text.lower())

        return features

    def process(self, statement, additional_response_selection_parameters=None):
        now = datetime.now()

        time_features = self.time_question_features(statement.text.lower())

        if 'time' in statement.text.lower():
            confidence = self.classifier.classify(time_features)
            response = Statement(text='The current time is ' + now.strftime('%I:%M %p'))
            response.confidence = confidence
            return response
        confidence = 0
        return Statement(text='There is no \'time\' in the user input')
