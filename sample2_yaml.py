import yaml
from yaml import load, load_all

stream = open('smaple.yaml','r')
date = load_all(stream, Loader=yaml.FullLoader)

for doc in data:
    print("New Document:")
    for key, Value in doc.items():
         print(key + ":" + str(Value))
         if type(Value) is list:
            print(str(len(Value)))