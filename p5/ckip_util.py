from ckip_transformers.nlp import CkipWordSegmenter

def ckip_word_segmenter(texts):
    ws_driver = CkipWordSegmenter()
    word_sentence_list = ws_driver(texts)
    return word_sentence_list