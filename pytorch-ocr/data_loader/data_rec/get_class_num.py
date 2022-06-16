import codecs
import json


character_json_path = 'chinese_chars_6695.json'
with codecs.open(character_json_path, "r", "utf8") as f:
    char2idx = json.loads(f.read())
    # print(char2idx)

print(len(char2idx))