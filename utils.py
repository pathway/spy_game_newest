import json

def load_json(filename: str) -> dict:
    with open("data/json/" + filename + ".json") as file:
        return json.load(file)

def load_text(filename:str) -> str:
    with open("data/strings/" + filename + ".txt") as file:
        return file

def clean_text(text: str) -> str:
    return text.replace("{", "").replace("}", "").replace("[").replace("]", "").replace("\"", "").replace("'", "").replace("_", " ")