import json

def load_data(filename: str) -> dict:
    with open("data/" + filename + ".json") as file:
        return json.load(file)

def load_text(filename:str) -> str:
    with open("data/strings/" + filename + ".txt") as file:
        return file