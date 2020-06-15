import json
from typing import NamedTuple, List

FILE_NAME = "high_score.json" 

class Score(NamedTuple):
    name: str
    value: float

def save_score(score: Score):
    with open(FILE_NAME, "r") as file_handle:
        scores = json.load(file_handle)   


    scores.append({"name": score.name, "value": score.value})
    scores.sort(key = lambda score: score["value"], reverse=True)

    with open(FILE_NAME, "w") as file_handle:
        json.dump(scores, file_handle, indent=4)   

def get_scores():
    with open(FILE_NAME, "r") as file_handle:
        scores = json.load(file_handle)
    return [Score(score['name'], score['value']) for score in scores]

if __name__ == '__main__':
    scores = get_scores()
    print(scores)
    save_score(Score("priyanka", 5))
    print(get_scores())