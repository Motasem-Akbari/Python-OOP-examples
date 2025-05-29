from abc import ABC, abstractmethod

import requests


class Joke(ABC):
    @abstractmethod
    def get_random_joke(self):
        pass


# api = "https://official-joke-api.appspot.com/random_joke"
class OfficialJoke(Joke):
    def get_random_joke(self):
        url = "https://api.chucknorris.io/jokes/random"
        result = requests.get(url)
        result1_json = result.json()
        return result1_json['value']


# api = "https://icanhazdadjoke.com/"
class IcanHazDadJoke(Joke):
    def get_random_joke(self):
        url = "https://icanhazdadjoke.com/"
        headers = {"Accept": "application/json"}
        result2 = requests.get(url, headers=headers)
        result2_json = result2.json()
        return result2_json['joke']

# api = "https://v2.jokeapi.dev/joke/Any"


class V2Joke(Joke):
    def get_random_joke(self):
        url = "https://v2.jokeapi.dev/joke/Any"
        result3 = requests.get(url)
        result3_json = result3.json()
        if result3_json["type"] == "single":
            return result3_json["joke"]
        elif result3_json["type"] == "twopart":
            return f"{result3_json['setup']} - {result3_json['delivery']}"
        else:
            return "Unexpected joke format!"


if __name__ == "__main__":
    while True:
        d = input("\n1: official\n2: Ican dad\n3: V2\npress: ")

        if d == "official":
            print(OfficialJoke().get_random_joke())
        elif d == "Ican dad":
            print(IcanHazDadJoke().get_random_joke())
        elif d == "V2":
            print(V2Joke().get_random_joke())
