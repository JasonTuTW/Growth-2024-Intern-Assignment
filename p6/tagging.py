import torch
from transformers import BertTokenizerFast, BertForTokenClassification
from transformers import pipeline
import re

def extract_chinese(text):
    chinese_characters = re.findall(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]', text)
    return ''.join(chinese_characters)

def is_chinese_symbol(c):
    return (c >= u'\u3000' and c <= u'\u303f') or (c >= u'\uff00' and c <= u'\uffef')

def get_ner_results(sentence: str):
    model_name = "ckiplab/bert-base-chinese-ner"
    tokenizer = BertTokenizerFast.from_pretrained('bert-base-chinese')
    model = BertForTokenClassification.from_pretrained(model_name)

    nlp_ner = pipeline("ner", model=model, tokenizer=tokenizer)

    sentence = extract_chinese(sentence)
    # delete substring "aabb"
    sentence = re.sub(r'微軟正黑體', '', sentence)

    ner_results = []
    s = ''
    for i in range(0, len(sentence)):
        s += sentence[i]
        if len(s) >= 512 or is_chinese_symbol(sentence[i]):
            s = s[:-1]
            ner_results.extend(nlp_ner(s))
            print(s)
            print(nlp_ner(s))
            s = ''
        
    
    #print(ner_results)

    formatted_results = [(entity['word'], entity['entity'], round(entity['score'], 2)) for entity in ner_results]

    return formatted_results

if __name__ == '__main__':
    sentence = "中研院"
    print(get_ner_results(sentence))