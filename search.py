import re
import json


class filenotfound(Exception):
    def __init__(self,filename):
        self.filename=filename


    def __str__(self):
        return f"{self.filename} not found"

class Search:
    def __init__(self, filename, word):
        self.word = word
        self.line_lists = []
        try:
            fobj=open(filename,"r")
            for para in fobj:
                sentances=para.split('.')
                for sentance in sentances:
                    self.line_lists.append(sentance)
        except:
            raise filenotfound(filename)

        self.clean(self.line_lists)

    def clean(self, data):
        pattern = "[^a-zA-Z0-9 ]"
        self.cleaned_data = list(map(lambda line: re.sub(pattern, "", line), data))
        self.getLines(self.cleaned_data)

    def getLines(self, cleaned_data):
        self.results = {}
        self.results[self.word] = []
        for index, sentance in enumerate(cleaned_data):
            if self.word in sentance:
                self.results[self.word].append((index+1, sentance))

        json_data=json.dumps(self.results)
        return json_data


Search("data.txt","word")