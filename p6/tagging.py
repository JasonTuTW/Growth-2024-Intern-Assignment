import torch
from transformers import BertTokenizer, BertForTokenClassification
from transformers import pipeline

model_name = "ckiplab/bert-base-chinese-ner"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name)

# 使用pipeline进行命名实体识别
nlp_ner = pipeline("ner", model=model, tokenizer=tokenizer)

# 要进行NER的中文句子
sentence = "中央研究院是臺灣最高學術研究機構，成立於1928年。"

# 进行NER
ner_results = nlp_ner(sentence)

# 打印NER结果
print("命名实体识别结果：")
for entity in ner_results:
    print(f"Entity: {entity['word']}, Label: {entity['entity']}, Score: {entity['score']:.4f}")

# 将NER结果格式化输出
formatted_results = [(entity['word'], entity['entity'], entity['score']) for entity in ner_results]
print("\n格式化的NER结果：")
for word, label, score in formatted_results:
    print(f"Word: {word}, Label: {label}, Score: {score:.4f}")
