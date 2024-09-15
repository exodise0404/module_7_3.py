import io
from pprint import pprint

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_names in self.file_names:
            with open(file_names, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for i in punc:
                    text = text.replace(i, "")
                    words = text.split()
                    all_words[file_names] = words
        return all_words

    def find(self, word):
        place = {}
        for key, value in self.get_all_words().items():
            place[key] = value.index(word.lower()) + 1
        return place

    def count(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
           counters[value] = key.count(word.lower())
        return counters



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего