from chatterbot.logic import LogicAdapter
from chatterbot import filters
from chatterbot.conversation import Statement



class ParlAI(LogicAdapter):
    """
    A logic adapter that returns a response based on known responses to
    the closest matches to the input statement.

    :param excluded_words:
        The excluded_words parameter allows a list of words to be set that will
        prevent the logic adapter from returning statements that have text
        containing any of those words. This can be useful for preventing your
        chat bot from saying swears when it is being demonstrated in front of
        an audience.
        Defaults to None
    :type excluded_words: list
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        from parlai.scripts import safe_interactive_custom
        from parlai.tasks.interactive import worlds
        opt = {'init_opt': None, 'show_advanced_args': False, 'task': 'interactive', 
               'download_path': '/Users/soyeon/Downloads/Project/chatbot/iitp-project-team8/ParlAI/downloads', 
               'datatype': 'train', 'image_mode': 'raw', 'numthreads': 1, 'hide_labels': False, 
               'multitask_weights': [1], 'batchsize': 1, 'dynamic_batching': None,
               'datapath': '/Users/soyeon/Downloads/Project/chatbot/iitp-project-team8/ParlAI/data', 
               'model': None, 'model_file': '/Users/soyeon/Downloads/Project/chatbot/iitp-project-team8/ParlAI/data/models/tutorial_transformer_generator/model', 
               'init_model': None, 'dict_class': 'parlai.core.dict:DictionaryAgent', 'display_examples': False, 
               'display_prettify': False, 'display_ignore_fields': 'label_candidates,text_candidates', 
               'interactive_task': True, 'safety': 'all', 'local_human_candidates_file': None, 'single_turn': False, 'image_size': 256,
               'image_cropsize': 224, 'embedding_size': 300, 'n_layers': 2, 'ffn_size': 300, 'dropout': 0.0, 'attention_dropout': 0.0,
               'relu_dropout': 0.0, 'n_heads': 2, 'learn_positional_embeddings': False, 'embeddings_scale': True, 'n_positions': None,
               'n_segments': 0, 'variant': 'aiayn', 'activation': 'relu', 'output_scaling': 1.0, 'share_word_embeddings': True, 
               'n_encoder_layers': -1, 'n_decoder_layers': -1, 'model_parallel': False, 'beam_size': 1, 'beam_min_length': 1, 
               'beam_context_block_ngram': -1, 'beam_block_ngram': -1, 'beam_length_penalty': 0.65, 'skip_generation': False, 
               'inference': 'greedy', 'topk': 10, 'topp': 0.9, 'beam_delay': 30, 'beam_blacklist_filename': None, 'temperature': 1.0, 
               'compute_tokenized_bleu': False, 'interactive_mode': True, 'embedding_type': 'random', 'embedding_projection': 'random', 
               'fp16': False, 'fp16_impl': 'apex', 'force_fp16_tokens': False, 'optimizer': 'sgd', 'learningrate': 1, 'gradient_clip': 0.1, 
               'adam_eps': 1e-08, 'adafactor_eps': (1e-30, 0.001), 'momentum': 0, 'nesterov': True, 'nus': (0.7,), 'betas': (0.9, 0.999), 
               'weight_decay': None, 'rank_candidates': False, 'truncate': -1, 'text_truncate': None, 'label_truncate': None, 
               'history_size': -1, 'person_tokens': False, 'split_lines': False, 'use_reply': 'label', 'add_p1_after_newln': False, 
               'delimiter': '\n', 'history_add_global_end_token': None, 'gpu': -1, 'no_cuda': False, 'dict_file': None, 
               'dict_initpath': None, 'dict_language': 'english', 'dict_max_ngram_size': -1, 'dict_minfreq': 0, 'dict_maxtokens': -1, 
               'dict_nulltoken': '__null__', 'dict_starttoken': '__start__', 'dict_endtoken': '__end__', 'dict_unktoken': '__unk__', 
               'dict_tokenizer': 're', 'dict_lower': False, 'bpe_debug': False, 'dict_textfields': 'text,labels', 'bpe_vocab': None, 
               'bpe_merge': None, 'bpe_add_prefix_space': None, 'lr_scheduler': 'reduceonplateau', 'lr_scheduler_patience': 3, 
               'lr_scheduler_decay': 0.5, 'max_lr_steps': -1, 'invsqrt_lr_decay_gamma': -1, 'warmup_updates': -1, 'warmup_rate': 0.0001, 
               'update_freq': 1, 'parlai_home': '/Users/soyeon/Downloads/Project/chatbot/iitp-project-team8/ParlAI/', 
               'override': {'model_file': '/Users/soyeon/Downloads/Project/chatbot/iitp-project-team8/ParlAI/data/models/tutorial_transformer_generator/model'}, 'starttime': 'Jun04_17-34'}
        self.w=safe_interactive_custom.safe_interactive_custom(opt)

        self.excluded_words = kwargs.get('excluded_words')

    def process(self, input_statement, additional_response_selection_parameters=None):
        response = self.w.parley_custom(input_statement.text)
        response = Statement(text=response)
        return response
    
    #def history_add(self, input_statement, text_for_gen):
      #  self.w.parley_observe(input_statement.text, text_for_gen)
